class Student:
    def __init__(self, name="", surname="", fathers_name="", age="", semester="", card_id="", enrolled_courses=None):
        self.name = name
        self.surname = surname
        self.fathers_name = fathers_name
        self.age = age
        self.semester = semester
        self.card_id = card_id
        if enrolled_courses is None:
            self.enrolled_courses = []
        else:
            self.enrolled_courses = enrolled_courses

    def from_dict(self, student_dict):
        self.student_id = student_dict["student_id"]
        self.name = student_dict["name"]
        self.surname = student_dict["surname"]
        self.fathers_name = student_dict["fathers_name"]
        self.age = student_dict["age"]
        self.semester = student_dict["semester"]
        self.card_id = student_dict["card_id"]
        self.enrolled_courses = student_dict["enrolled_courses"]

    def to_dict(self):
        student_dict = {
            "student_id": self.student_id,
            "name": self.name,
            "surname": self.surname,
            "fathers_name": self.fathers_name,
            "age": self.age,
            "semester": self.semester,
            "card_id": self.card_id,
            "enrolled_courses": self.enrolled_courses
        }
        return student_dict

    def set_id(self, student_id):
        self.student_id = student_id

    def add_course(self, course):
        self.enrolled_courses.append(course.course_id)
        print(
            f"Student {self.surname} {self.name} ({self.student_id}) has been successfully "
            f"enrolled at course {course.title}")

    def __str__(self):
        string = f"{self.student_id} {self.name} {self.fathers_name[0]}. {self.surname}\n"
        string += f"Age: {self.age} Semester: {self.semester} Card id: {self.card_id}\n"
        string += "Enrolled Courses\n"
        string += f"{20 * '-'}\n"
        if not self.enrolled_courses:
            string += "No courses enrolled"
        else:
            for course in self.enrolled_courses:
                string += str(course) + "\n"
        return string
