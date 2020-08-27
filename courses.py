from course import Course
import json

class Courses:
    def __init__(self):
        try:
            with open("courses.json") as f:
                courses_list = json.load(f)

            self.courses = []
            for course_dict in courses_list:
                new_course = Course()
                new_course.from_dict(course_dict)
                self.courses += [new_course]
        except FileNotFoundError:
            self.courses = []

    def __set_course_id(self):
        if self.courses:
            ids = []
            for course in self.courses:
                ids.append(int(course.course_id[3:]))
            new_id = max(ids) + 1
            return "crs" + str(new_id)
        return "crs1000"

    def create_course(self):
        title = input("Course title: ")
        type = input("Course type (theory/lab): ")
        new_course = Course(title, type)
        new_course.set_id(self.__set_course_id())
        self.courses.append(new_course)
        return new_course

    def store_to_file(self):
        courses_list = []
        for course in self.courses:
            courses_list.append(course.to_dict())
        with open("courses.json", "w") as f:
            json.dump(courses_list, f)


    def find_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None


    def find_by_title(self, course_title):
        for course in self.courses:
            if course.title == course_title:
                return course
        return None

    def update(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                print(course)
                choice = int(input("Update 1.Title 2.Type: "))
                if choice == 1:
                    course.title = input("Give new title: ")
                elif choice == 2:
                    course.type = input("Give new type (Theory/Lab): ")
                return True
        return False


    def delete(self, course_id):
        for i in range(len(self.courses)):
            if self.courses[i].course_id == course_id:
                self.courses.pop(i)
                return True
        return False


    def print_courses(self):
        for course in self.courses:
            print(course)