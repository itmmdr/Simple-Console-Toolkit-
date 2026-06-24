grades = []

def grade_manager():
    while True:
        print("\n=== Grade Management System ===")
        print("1. Add Grade")
        print("2. Show Grades")
        print("3. Average Grade")
        print("4. Highest Grade")
        print("5. Lowest Grade")
        print("6. Exit")

        choice = input("Choose an option: ").strip().lower()

        if choice in ["1", "add grade"]:
            try:
                grade = float(input("Enter grade: "))
                grades.append(grade)
                print("Grade added successfully.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice in ["2", "show grades"]:
            if not grades:
                print("No grades available.")
            else:
                print("Grades:")
                for grade in grades:
                    print(f"- {grade}")

        elif choice in ["3", "average grade", "average"]:
            if not grades:
                print("No grades available.")
            else:
                print(f"Average Grade: {sum(grades) / len(grades):.2f}")

        elif choice in ["4", "highest grade"]:
            if not grades:
                print("No grades available.")
            else:
                print(f"Highest Grade: {max(grades)}")

        elif choice in ["5", "lowest grade"]:
            if not grades:
                print("No grades available.")
            else:
                print(f"Lowest Grade: {min(grades)}")

        elif choice in ["6", "exit"]:
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")


