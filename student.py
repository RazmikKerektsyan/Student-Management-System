class Student:
    def __init__(self, name: str, roll_number: int, grade: str):
        self.__name = name
        self.__roll_number = roll_number
        self.grade = grade

    @property
    def name(self):
        return self.__name

    @property
    def roll_number(self):
        return self.__roll_number

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, new_grade):
        new_grade = new_grade.strip().upper()

        if new_grade not in ["A", "B", "C", "D", "E", "F"]:
            raise ValueError("შეფასება უნდა იყოს ერთი ასო A, B, C, D, E ან F")

        self.__grade = new_grade
