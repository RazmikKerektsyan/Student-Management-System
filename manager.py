from student import Student
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        for student in self.students:
            if student.roll_number == roll_number:
                print("ასეთი ნომრის მქონე სტუდენტი უკვე არსებობს")
                return
        self.students.append(Student(name, roll_number, grade))

    def show_students(self):
        if len(self.students) == 0:
            print("სტუდენტების სია ცარიელია!")
        else:
            for student in self.students:
                print(student.name, student.roll_number, student.grade)

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(student.name, student.roll_number, student.grade)
                break
        else:
            print("სტუდენტი არ მოიძებნა")

    def update_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("შეფასება წარმატებით განახლდა")
                break
        else:
            print("სტუდენტი არ მოიძებნა")
