from student import Student
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        self.students.append(Student(name, roll_number, grade))

    def show_students(self):
        if len(self.students) == 0:
            print("სტუდენტების სია ცარიელია!")
        else:
            for student in self.students:
                print(student.name, student.roll_number, student.grade)

