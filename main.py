students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = int(input("Enter marks: "))

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\n📋 Student List:")
    for s in students:
        print(f"Name: {s['name']} | Roll: {s['roll']} | Marks: {s['marks']}")

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"🔍 Found: {s}")
            return
    print("❌ Student not found!")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("🗑 Student deleted!")
            return
    print("❌ Student not found!")

def show_topper():
    if not students:
        print("No data available.")
        return

    topper = max(students, key=lambda x: x["marks"])
    print(f"🏆 Topper: {topper['name']} with {topper['marks']} marks")

def show_average():
    if not students:
        print("No data available.")
        return

    avg = sum(s["marks"] for s in students) / len(students)
    print(f"📊 Average Marks: {avg:.2f}")

while True:
    print("\n===== SMART SCHOOL MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Show Topper")
    print("6. Show Average Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        show_topper()
    elif choice == "6":
        show_average()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
