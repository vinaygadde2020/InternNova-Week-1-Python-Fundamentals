students = []
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        branch = input("Enter branch: ")
        student = {
            "Name": name,
            "Roll No": roll_no,
            "Branch": branch
        }
        students.append(student)
        print("Student added successfully.")
    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)
    elif choice == "3":
        name = input("Enter student name to search: ")
        found = False
        for student in students:
            if student["Name"].lower() == name.lower():
                print("Student found:", student)
                found = True
                break
        if not found:
            print("Student not found.")
    elif choice == "4":
        name = input("Enter student name to delete: ")
        found = False
        for student in students:
            if student["Name"].lower() == name.lower():
                students.remove(student)
                print("Student deleted successfully.")
                found = True
                break
        if not found:
            print("Student not found.")
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")