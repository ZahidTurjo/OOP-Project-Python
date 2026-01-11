class StudentDatabase:
    def __init__(self):
        self.students_list = []

    def add_student(self, student):
        self.students_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"{self.__name} is successfully enrolled")
        else:
            raise ValueError(f"{self.__name} is already enrolled")

    def drop_student(self):
        self.__is_enrolled = False
        print(f"{self.__name} is dropped")

    def view_student_info(self):
        print(
            f"Name: {self.__name}, "
            f"ID: {self.__student_id}, "
            f"Dept: {self.__department}, "
            f"Enrolled: {self.__is_enrolled}"
        )


# usage
db = StudentDatabase()

s1 = Student(1, "ok", "am")
s2 = Student(2, "oka", "ama")

db.add_student(s1)
db.add_student(s2)

for student in db.students_list:
    print(student)
    student.view_student_info()
