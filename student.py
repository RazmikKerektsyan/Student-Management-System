# class Person:
#     def __init__(self, name: str):
#         self.name = name
#     @property
#     def name(self) -> str:
#         return self.__name
#     @name.setter
#     def name(self, value: str):
#         if not value or not value.strip(): raise ValueError("სახელი არ შეიძლება იყოს ცარიელი!")
#         else:
#             self.__name = value.strip()
#     def get_info(self) -> str:
#         return f"სახელი: {self.__name}"

class Student:
    def __init__(self, name: str, roll_number: int, grade: str):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

