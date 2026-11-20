from manager import StudentManager

manager = StudentManager()
while True:
    print("\n1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update grade")
    print("5. Exit")
    try:
        choice = int(input("აირჩიეთ მოქმედება: "))
    except ValueError:
        print("გთხოვთ, შეიყვანოთ რიცხვი")
        continue
    if choice == 1:
        name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()
        if not name:
            print("სახელი არ უნდა იყოს ცარიელი")
            continue
        try:
            roll_number = int(input("შეიყვანეთ სტუდენტის ნომერი: "))
        except ValueError:
            print("გთხოვთ, შეიყვანოთ რიცხვი")
            continue
        if roll_number <= 0:
            print("ნომერი უნდა იყოს დადებითი")
            continue
        grade = input("შეიყვანეთ სტუდენტის შეფასება: ")
        try:
            manager.add_student(name, roll_number, grade)
        except ValueError as error:
            print(error)
            continue
    elif choice == 2:
        manager.show_students()
    elif choice == 3:
        try:
            roll_number = int(input("მოძებნეთ სტუდენტის ნომრით: "))
        except ValueError:
            print("გთხოვთ, შეიყვანოთ რიცხვი")
            continue
        manager.search_student(roll_number)
    elif choice == 4:
        try:
            roll_number = int(input("შეიყვანეთ სტუდენტის ნომერი: "))
        except ValueError:
            print("გთხოვთ, შეიყვანოთ რიცხვი")
            continue
        grade = input("შეიყვანეთ სტუდენტის ახალი შეფასება: ").strip().upper()

        try:
            manager.update_grade(roll_number, grade)
        except ValueError as error:
            print(error)
            continue
    elif choice == 5:
        break
    else:
        print("არასწორი არჩევანი")