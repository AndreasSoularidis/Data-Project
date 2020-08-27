from student import Student
import json


class Students:
    def __init__(self):
        try:
            self.students = []
            with open("students.json") as f:
                students_dict = json.load(f)

            for student_dict in students_dict:
                new_student = Student()
                new_student.from_dict(student_dict)
                self.students += [new_student]
        except FileNotFoundError:
            self.students = []

    def __set_student_id(self):
        if self.students:
            ids = []
            for student in self.students:
                ids.append(int(student.student_id[3:]))
            new_id = max(ids) + 1
            return "std" + str(new_id)
        return "std1000"

    def create_student(self):
        name = input("Name: ")
        surname = input("Surname: ")
        fathers_name = input("Father's name: ")
        age = input("Age: ")
        semester = input("Semester: ")
        card_id = input("Card id: ")
        new_student = Student(name, surname, fathers_name, age, semester, card_id)
        new_student.set_id(self.__set_student_id())
        self.students += [new_student]
        return new_student

    def find_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update(self, student_id):
        student = self.find_by_id(student_id)
        if student is None:
            print(f"There is not student with id {student_id}")
            return False
        while True:
            choice = input("Update: 1.Name, 2.Surname, 3.Fathers name, 4.Age, 5.Semester, 6.Card id: ")
            if not choice.isdigit():
                print("Give a number please")
                continue
            choice = int(choice)
            if choice < 1 or choice > 6:
                print("Index out of borders")
            else:
                break

        if choice == 1:
            student.name = input("Give student name: ")
        elif choice == 2:
            student.surname = input("Give student surname: ")
        elif choice == 3:
            student.fathers_name = input("Give student father's name: ")
        elif choice == 4:
            student.age = input("Give student age: ")
        elif choice == 5:
            student.semester = input("Give student semester: ")
        elif choice == 6:
            student.card_id = input("Give student card id: ")

        return True


    def delete(self, student_id):
        student = self.find_by_id(student_id)
        if student is None:
            print(f"There is not student with id {student_id}")
            return False

        for i in range(len(self.students)):
            if self.students[i].student_id == student_id:
                self.students.pop(i)
                return True
        return False

    def store_to_file(self):
        student_list = []
        for student in self.students:
            student_list.append(student.to_dict())
        with open("students.json", "w") as f:
            json.dump(student_list, f)