from courses import Courses
from students import Students
from teachers import Teachers


# Methods for managing students
def create_student(students):
    student = students.create_student()
    print(f"Student with id {student.student_id} has been successfully created")
    print(student)


def add_course_to_student(students, courses):
    student_id = input("Give student id: ")
    student = students.find_by_id(student_id)
    if student is None:
        print(f"There is no student with id {student_id}")
        return
    print(student)
    print("Available Courses")
    print(f"{20 * '-'}")
    for course in courses.courses:
        print(course)
    course_id = input("Pick a course: ")
    course = courses.find_by_id(course_id)
    if course is None:
        print(f"There is no course with id {course_id}")
        return
    student.add_course(course)


def update_student(students):
    student_id = input("Give student id: ")
    student_update = students.update(student_id)
    if not student_update:
        print("An error occured. Student did not updated successfully")
        return
    print(f"Student updated successfully")


def delete_student(students):
    student_id = input("Give student id: ")
    student_update = students.delete(student_id)
    if not student_update:
        print("An error occured. Student did not deleted successfully")
        return
    print(f"Student deleted successfully")


# Methods for managing teacher
def insert_teacher(teachers):
    teacher = teachers.create_teacher()
    print(f"Teacher with id {teacher.teacher_id} has been successfully created")
    print(teacher)


def add_course_to_teacher(teachers, courses):
    teacher_id = input("Give teacher id: ")
    teacher = teachers.find_by_id(teacher_id)
    if teacher is None:
        print(f"There is no student with id {teacher_id}")
        return
    print(teacher)
    print("Available Courses")
    print(f"{20 * '-'}")
    for course in courses.courses:
        print(course)
    course_id = input("Pick a course: ")
    course = courses.find_by_id(course_id)
    if course is None:
        print(f"There is no course with id {course_id}")
        return
    teacher.add_course(course)


def update_teacher(teachers):
    teacher_id = input("Give teacher id: ")
    teacher_update = teachers.update(teacher_id)
    if not teacher_update:
        print("An error occured. Teacher did not updated successfully")
        return
    print(f"Teacher updated successfully")


def delete_teacher(teachers):
    teacher_id = input("Give teacher id: ")
    teacher_deleted = teachers.delete(teacher_id)
    if not teacher_deleted:
        print("An error occured. Teacher did not deleted successfully")
        return
    print(f"Teacher deleted successfully")


# Methods for managing courses
def create_course(courses):
    course = courses.create_course()
    print(f"The course {course.title} has been successfully created")
    print(course)


def update_course(courses):
    course_id = input("Give course id: ")
    update = courses.update(course_id)
    if not update:
        print(f"Update Failed")
        return
    print(f"The course with id {course_id} has been successfully updated")


def delete_course(courses):
    course_id = input("Give course id: ")
    delete = courses.delete(course_id)
    if not delete:
        print(f"Delete Failed")
        return
    print(f"The course with id {course_id} has been successfully deleted")


def main():
    courses = Courses()
    students = Students()
    teachers = Teachers()
    while True:
        print("\nMain Menu")
        print(f"{20 * '-'}")
        print("1. Manage Students")
        print("2. Manage Teachers")
        print("3. Manage Course")
        print("4. Exit")
        while True:
            choice = input("Pick one: ")
            if not choice.isdigit():
                print("Give a number please")
                continue
            choice = int(choice)
            if choice < 1 or choice > 4:
                print("Index out of borders")
            else:
                break
        if choice == 1:
            while True:
                print("\nManage Students")
                print(f"{20 * '-'}")
                print("1. Create Student")
                print("2. Add Course to Students")
                print("3. Read Students")
                print("4. Update Students")
                print("5. Delete Students")
                print("6. Back to Main Menu")
                while True:
                    manage_student_choice = input("Pick one: ")
                    if not manage_student_choice.isdigit():
                        print("Give a number please")
                        continue
                    manage_student_choice = int(manage_student_choice)
                    if manage_student_choice < 1 or manage_student_choice > 6:
                        print("Index out of borders")
                    else:
                        break

                if manage_student_choice == 1:  # CREATE STUDENT
                    print("\nINSERT STUDENT")
                    print(f"{20 * '-'}")
                    create_student(students)
                elif manage_student_choice == 2:  # ADD COURSE TO STUDENT
                    print("\nADD COURSE TO STUDENT")
                    print(f"{20 * '-'}")
                    add_course_to_student(students, courses)
                elif manage_student_choice == 3:  # READ STUDENTS
                    while True:
                        print("\nREAD STUDENTS")
                        print(f"{20 * '-'}")
                        print("1. Read a student id")
                        print("2. Read all students")
                        print("3. Back to Students Menu")
                        while True:
                            read_students_choice = input("Pick one: ")
                            if not read_students_choice.isdigit():
                                print("Give a number please")
                                continue
                            read_students_choice = int(read_students_choice)
                            if read_students_choice < 1 or read_students_choice > 3:
                                print("Index out of borders")
                            else:
                                break
                        if read_students_choice == 1:  # READ STUDENT BY ID
                            student_id = input("Give student id: ")
                            student = students.find_by_id(student_id)
                            if student is None:
                                print(f"There is no student with id {student_id}")
                            else:
                                print(student)
                        elif read_students_choice == 2:  # READ ALL STUDENTS
                            for student in students.students:
                                print(student)
                                print(f"{20 * '='}")
                        elif read_students_choice == 3:  # BACK TO STUDENTS MENU
                            break
                elif manage_student_choice == 4:  # UPDATE STUDENTS
                    print("\nUPDATE STUDENTS")
                    print(f"{20 * '-'}")
                    update_student(students)
                elif manage_student_choice == 5:  # DELETE STUDENTS
                    print("\nDELETE STUDENTS")
                    print(f"{20 * '-'}")
                    delete_student(students)
                elif manage_student_choice == 6:  # BACK TO MAIN MENU
                    break

        elif choice == 2:
            while True:
                print("\nManage Teachers")
                print(f"{20 * '-'}")
                print("1. Create Teacher")
                print("2. Add Course to Teacher")
                print("3. Read Teachers")
                print("4. Update Teachers")
                print("5. Delete Teachers")
                print("6. Back to Main Menu")
                while True:
                    manage_teacher_choice = input("Pick one: ")
                    if not manage_teacher_choice.isdigit():
                        print("Give a number please")
                        continue
                    manage_teacher_choice = int(manage_teacher_choice)
                    if manage_teacher_choice < 1 or manage_teacher_choice > 6:
                        print("Index out of borders")
                    else:
                        break
                if manage_teacher_choice == 1:  # CREATE TEACHER
                    print("\nINSERT ΤΕΑCHER")
                    print(f"{20 * '-'}")
                    insert_teacher(teachers)
                elif manage_teacher_choice == 2:  # ADD COURSE TO TEACHER
                    print("\nADD COURSE TO TEACHER")
                    print(f"{20 * '-'}")
                    add_course_to_teacher(teachers, courses)
                elif manage_teacher_choice == 3:  # READ TEACHER
                    while True:
                        print("\nREAD TEACHERS")
                        print(f"{20 * '-'}")
                        print("1. Read a teacher by id")
                        print("2. Read all teachers")
                        print("3. Back to Teachers Menu")
                        while True:
                            read_teachers_choice = input("Pick one: ")
                            if not read_teachers_choice.isdigit():
                                print("Give a number please")
                                continue
                            read_teachers_choice = int(read_teachers_choice)
                            if read_teachers_choice < 1 or read_teachers_choice > 3:
                                print("Index out of borders")
                            else:
                                break
                        if read_teachers_choice == 1:  # READ TEACHER BY ID
                            teacher_id = input("Give teacher id: ")
                            teacher = teachers.find_by_id(teacher_id)
                            if teacher is None:
                                print(f"There is no student with id {teacher_id}")
                            else:
                                print(teacher)
                        elif read_teachers_choice == 2:  # READ ALL TEACHERS
                            for teacher in teachers.teachers:
                                print(teacher)
                                print(f"{20 * '='}")
                        elif read_teachers_choice == 3:  # BACK TO STUDENTS MENU
                            break
                elif manage_teacher_choice == 4:  # UPDATE TEACHER
                    print("\nUPDATE TEACHER")
                    print(f"{20 * '-'}")
                    update_teacher(teachers)
                elif manage_teacher_choice == 5:  # DELETE TEACHER
                    print("\nDELETE TEACHER")
                    print(f"{20 * '-'}")
                    delete_teacher(teachers)
                elif manage_teacher_choice == 6:  # BACK TO MAIN MENU
                    break

        elif choice == 3:
            while True:
                print("\nManage Course")
                print(f"{20 * '-'}")
                print("1. Create Course")
                print("2. Read Courses")
                print("3. Update Course")
                print("4. Delete Course")
                print("5. Back to Main Menu")
                while True:
                    manage_course_choice = input("Pick one: ")
                    if not manage_course_choice.isdigit():
                        print("Give a number please")
                        continue
                    manage_course_choice = int(manage_course_choice)
                    if choice < 1 or choice > 5:
                        print("Index out of borders")
                    else:
                        break
                if manage_course_choice == 1:
                    print("\nCREATE COURSE")
                    print(f"{20 * '-'}")
                    create_course(courses)
                elif manage_course_choice == 2:
                    while True:
                        print("\nREAD COURSES")
                        print(f"{20 * '-'}")
                        print("1. Read a course by id")
                        print("2. Read a course by title")
                        print("3. Read all courses")
                        print("4. Back to Courses Menu")
                        while True:
                            read_courses_choice = input("Pick one: ")
                            if not read_courses_choice.isdigit():
                                print("Give a number please")
                                continue
                            read_courses_choice = int(read_courses_choice)
                            if choice < 1 or choice > 4:
                                print("Index out of borders")
                            else:
                                break

                        if read_courses_choice == 1:  # read course by id
                            course_id = input("Give course id: ")
                            course = courses.find_by_id(course_id)
                            if course is None:
                                print(f"There is no course with id {course_id}")
                            else:
                                print(course)
                        elif read_courses_choice == 2:  # Read course by title
                            course_title = input("Give course title: ")
                            course = courses.find_by_title(course_title)
                            if course is None:
                                print(f"There is no course with title {course_title}")
                            else:
                                print(course)
                        elif read_courses_choice == 3:  # Read all courses
                            print("University Courses")
                            print(f"{20 * '-'}")
                            courses.print_courses()
                        elif read_courses_choice == 4:  # Go back to courses menu
                            break
                elif manage_course_choice == 3:  # UPDATE COURSE
                    print("\nUPDATE COURSE")
                    print(f"{20 * '-'}")
                    update_course(courses)
                elif manage_course_choice == 4:  # DELETE COURSE
                    print("\nDELETE COURSE")
                    print(f"{20 * '-'}")
                    delete_course(courses)
                elif manage_course_choice == 5:
                    break

        elif choice == 4:
            courses.store_to_file()
            teachers.store_to_file()
            students.store_to_file()
            print("Bye bye")
            break


main()
