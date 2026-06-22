from main import main

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
            try:
                number_1 = float(input("Enter first number: "))
                number_2 = float(input("Enter second number: "))
            except ValueError:
                print("You must enter a number.")
                continue
            print(f"Result: {number_1 + number_2}")

        elif ask_choice in ["2", "subtraction"]:
            try:
                number_1 = float(input("Enter first number: "))
                number_2 = float(input("Enter second number: "))
            except ValueError:
                print("You must enter a number.")
                continue
            print(f"Result: {number_1 - number_2}")

        elif ask_choice in ["3", "multiplication"]:
            try:
                number_1 = float(input("Enter first number: "))
                number_2 = float(input("Enter second number: "))
            except ValueError:
                print("You must enter a number.")
                continue
            print(f"Result: {number_1 * number_2}")

        elif ask_choice in ["4", "division"]:
            try:
                number_1 = float(input("Enter first number: "))
                number_2 = float(input("Enter second number: "))
            except ValueError:
                print("You must enter a number.")
                continue

            if number_2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"Result: {number_1 / number_2}")

        elif ask_choice in ["5", "exit"]:
            print("Goodbye!")
            return main()
            

        else:
            print("Invalid option! Try again.")


calculator()