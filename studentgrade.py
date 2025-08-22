students = []
grades = []

def add():
    name = input("Enter name: ")
    grade = float(input("Enter grade: "))
    students.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}")

def update():
    name = input("Enter student name to update his/her grade: ")
    if name in students:
        new_grade = float(input("Enter new grade: "))
        index = students.index(name)
        grades[index] = new_grade
        print(f"Updated {name}'s grade to {new_grade}")
    else:
        print(f"{name} not found")

def remove():
    name = input("Enter name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"Removed {name}")
    else:
        print(f"{name} not found")

def avg():
    if grades:
        average = sum(grades) / len(grades)
        print(f"Average Grade: {average:.2f}")
    else:
        print("No grades available")

while True:
    print("\n-- Student Management --")
    print("1. Add")
    print("2. Update Grade")
    print("3. Remove")
    print("4. Average Grade")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        update()
    elif choice == "3":
        remove()
    elif choice == "4":
        avg()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
