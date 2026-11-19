from student import Student
from manager import StudentManager
s1 = Student("gajo", 2, "A")
s2 = Student("gerg", 3, "B")
s3 = Student("james", 4, "C")
# print(s1.name, s1.roll_number, s1.grade)
# print(s2.name, s2.roll_number, s2.grade)
# print(s3.name, s3.roll_number, s3.grade)


manager = StudentManager()
manager.add_student("Razmik", 1, "A")
manager.add_student("Bob", 2, "B")

for student in manager.students:
    print(student.name)
    print(student.roll_number)
    print(student.grade)
