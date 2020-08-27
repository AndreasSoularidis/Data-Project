class Teacher:
    def __init__(self, name="", surname="", card_id="", courses=None):
        self.name = name
        self.surname = surname
        self.card_id = card_id
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def from_dict(self, teachers_dict):
        self.teacher_id = teachers_dict["teacher_id"]
        self.name = teachers_dict["name"]
        self.surname = teachers_dict["surname"]
        self.card_id = teachers_dict["card_id"]
        self.courses = teachers_dict["courses"]

    def to_dict(self):
        teacher_dict = {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "surname": self.surname,
            "card_id": self.card_id,
            "courses": self.courses
        }
        return teacher_dict

    def set_id(self, teacher_id):
        self.teacher_id = teacher_id

    def add_course(self, course):
        self.courses.append(course.course_id)
        print(f"Teacher {self.surname} {self.name} ({self.teacher_id}) has been successfully "
              f" connected with course {course.title}")

    def __str__(self):
        string = f"{self.surname} {self.name} {self.card_id}\n"
        string += "Teaching Courses\n"
        string += f"{20 * '-'}\n"
        if not self.courses:
            string += "Teacher has not course to teach"
        else:
            for course in self.courses:
                string += f"{course}\n"
        return string
