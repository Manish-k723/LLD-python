from association import Student

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        self.students.remove(student)

    def show_students(self) -> None:
        for student in self.students:
            print(student.name)

s1 = Student("John", 1)
s2 = Student("Mike", 2)

dept = Department("CS")
dept.add_student(s1)
dept.add_student(s2)
dept.show_students()

del dept

print(s1.name)


