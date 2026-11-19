from student import Student
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        self.students.append(Student(name, roll_number, grade))

