def converter():

    # ---------- LENGTH ----------
    def length():
        while True:
            print("\n-- Length --")
            print("1. Meter ↔ Centimeter")
            print("2. Meter ↔ Millimeter")
            print("3. Kilometer ↔ Meter")
            print("4. Kilometer ↔ Mile")
            print("5. Back")

            op = input("Choose: ")

            try:
                num = float(input("Enter value: "))
            except ValueError:
                print("Invalid number!")
                continue

            if op == '1':
                print(f"{num} m = {num * 100} cm")
                print(f"{num} cm = {num / 100} m")

            elif op == '2':
                print(f"{num} m = {num * 1000} mm")
                print(f"{num} mm = {num / 1000} m")

            elif op == '3':
                print(f"{num} km = {num * 1000} m")
                print(f"{num} m = {num / 1000} km")

            elif op == '4':
                print(f"{num} km = {num * 0.621371} miles")
                print(f"{num} miles = {num / 0.621371} km")

            elif op == '5':
                return converter()


    # ---------- WEIGHT ----------
    def weight():
        while True:
            print("\n-- Weight --")
            print("1. Kilogram ↔ Gram")
            print("2. Kilogram ↔ Milligram")
            print("3. Kilogram ↔ Pound")
            print("4. Back")

            op = input("Choose: ")

            try:
                num = float(input("Enter value: "))
            except ValueError:
                print("Invalid number!")
                continue

            if op == '1':
                print(f"{num} kg = {num * 1000} g")
                print(f"{num} g = {num / 1000} kg")

            elif op == '2':
                print(f"{num} kg = {num * 1_000_000} mg")
                print(f"{num} mg = {num / 1_000_000} kg")

            elif op == '3':
                print(f"{num} kg = {num * 2.20462} lb")
                print(f"{num} lb = {num / 2.20462} kg")

            elif op == '4':
                break


    # ---------- TIME ----------
    def time():
        while True:
            print("\n-- Time --")
            print("1. Hour ↔ Minute")
            print("2. Minute ↔ Second")
            print("3. Day ↔ Hour")
            print("4. Back")

            op = input("Choose: ")

            try:
                num = float(input("Enter value: "))
            except ValueError:
                print("Invalid number!")
                continue

            if op == '1':
                print(f"{num} hr = {num * 60} min")
                print(f"{num} min = {num / 60} hr")

            elif op == '2':
                print(f"{num} min = {num * 60} sec")
                print(f"{num} sec = {num / 60} min")

            elif op == '3':
                print(f"{num} day = {num * 24} hr")
                print(f"{num} hr = {num / 24} day")

            elif op == '4':
                break


    # ---------- TEMPERATURE ----------
    def temperature():
        while True:
            print("\n-- Temperature --")
            print("1. Celsius ↔ Fahrenheit")
            print("2. Celsius ↔ Kelvin")
            print("3. Back")

            op = input("Choose: ")

            try:
                num = float(input("Enter value: "))
            except ValueError:
                print("Invalid number!")
                continue

            if op == '1':
                print(f"{num} C = {(num * 9/5) + 32} F")
                print(f"{num} F = {(num - 32) * 5/9} C")

            elif op == '2':
                print(f"{num} C = {num + 273.15} K")
                print(f"{num} K = {num - 273.15} C")

            elif op == '3':
                break


    # ---------- VOLUME ----------
    def volume():
        while True:
            print("\n-- Volume --")
            print("1. Liter ↔ Milliliter")
            print("2. Liter ↔ Cubic Meter")
            print("3. Liter ↔ Gallon")
            print("4. Back")

            op = input("Choose: ")

            try:
                num = float(input("Enter value: "))
            except ValueError:
                print("Invalid number!")
                continue

            if op == '1':
                print(f"{num} L = {num * 1000} ml")
                print(f"{num} ml = {num / 1000} L")

            elif op == '2':
                print(f"{num} L = {num / 1000} m³")
                print(f"{num} m³ = {num * 1000} L")

            elif op == '3':
                print(f"{num} L = {num * 0.264172} gallon")
                print(f"{num} gallon = {num / 0.264172} L")

            elif op == '4':
                break


    # ---------- MAIN MENU ----------
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Length")
        print("2. Weight")
        print("3. Time")
        print("4. Temperature")
        print("5. Volume")
        print("6. Exit")

        ask = input("Choose: ")

        if ask == '1':
            length()
        elif ask == '2':
            weight()
        elif ask == '3':
            time()
        elif ask == '4':
            temperature()
        elif ask == '5':
            volume()
        elif ask == '6':
            print("Goodbye 👋")
            break
        else:
            print("Invalid option!")
