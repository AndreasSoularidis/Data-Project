class Course:
    def __init__(self, title="", type=""):
        self.title = title
        self.type = type

    def set_id(self, course_id):
        self.course_id = course_id

    def from_dict(self, courses_dict):
        self.course_id = courses_dict["course_id"]
        self.title = courses_dict["title"]
        self.type = courses_dict["type"]

    def to_dict(self):
        course_dict = {
            "course_id": self.course_id,
            "title": self.title,
            "type": self.type
        }
        return course_dict


    def __str__(self):
        return f"{self.course_id} {self.title} ({self.type})"
