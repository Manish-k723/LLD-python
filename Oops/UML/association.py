class Teacher:
    def __init__(self, name: str) -> None:
        self.name = name

    def teach(self, student: "Student") -> None:
        print(f"{self.name} teaches {student.name}")


class Student:
    def __init__(self, name: str, roll: int) -> None:
        self.name = name
        self.roll = roll

    def __str__(self) -> str:
        return f"{self.name} {self.roll}"

s1 = Student("John", 1)
t1 = Teacher("Mike")
t1.teach(s1)