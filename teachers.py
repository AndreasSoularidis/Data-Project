from teacher import Teacher
import json


class Teachers:
    def __init__(self):
        try:
            self.teachers = []
            with open("teachers.json") as f:
                teachers_dict = json.load(f)
                for teacher_dict in teachers_dict:
                    new_teacher = Teacher()
                    new_teacher.from_dict(teacher_dict)
                    self.teachers += [new_teacher]
        except FileNotFoundError:
            self.teachers = []

    def __set_teacher_id(self):
        if self.teachers:
            ids = []
            for teacher in self.teachers:
                ids.append(int(teacher.teacher_id[3:]))
            new_id = max(ids) + 1
            return "prf" + str(new_id)
        return "prf1000"

    def find_by_id(self, teacher_id):
        for teacher in self.teachers:
            if teacher.teacher_id == teacher_id:
                return teacher
        return None

    def create_teacher(self):
        name = input("Name: ")
        surname = input("Surname: ")
        card_id = input("Card id: ")
        new_teacher = Teacher(name, surname, card_id)
        new_teacher.set_id(self.__set_teacher_id())
        self.teachers += [new_teacher]
        return new_teacher

    def update(self, teacher_id):
        teacher = self.find_by_id(teacher_id)
        if teacher is None:
            print(f"There is not student with id {teacher_id}")
            return False
        print(teacher)
        while True:
            choice = input("Update: 1.Name, 2.Surname, 3.Card id: ")
            if not choice.isdigit():
                print("Give a number please")
                continue
            choice = int(choice)
            if choice < 1 or choice > 3:
                print("Index out of borders")
            else:
                break

        if choice == 1:
            teacher.name = input("Give teacher name: ")
        elif choice == 2:
            teacher.surname = input("Give teacher surname: ")
        elif choice == 3:
            teacher.card_id = input("Give teacher card id: ")

        return True

    def delete(self, teacher_id):
        teacher = self.find_by_id(teacher_id)
        if teacher is None:
            print(f"There is not teacher with id {teacher_id}")
            return False

        for i in range(len(self.teachers)):
            if self.teachers[i].teacher_id == teacher_id:
                self.teachers.pop(i)
                return True
        return False

    def store_to_file(self):
        teachers_list = []
        for teacher in self.teachers:
            teachers_list.append(teacher.to_dict())
        with open("teachers.json", "w") as f:
            json.dump(teachers_list, f)
