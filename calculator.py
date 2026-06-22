def calculator():
    while True:
        print("\n=== Calculator ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        ask_choice = input(
            "Choose an option (write number or operation name): "
        ).lower()

        if ask_choice in ["1", "addition"]:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            print(f"Result: {number_1 + number_2}")

        elif ask_choice in ["2", "subtraction"]:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            print(f"Result: {number_1 - number_2}")

        elif ask_choice in ["3", "multiplication"]:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            print(f"Result: {number_1 * number_2}")

        elif ask_choice in ["4", "division"]:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if number_2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"Result: {number_1 / number_2}")

        elif ask_choice in ["5", "exit"]:
            print("Goodbye!")
            break

        else:
            print("Invalid option! Try again.")


calculator()