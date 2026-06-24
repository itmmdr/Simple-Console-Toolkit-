import random

def guess_game():
    computer_choice = random.randint(1, 100)

    while True:
        try:
            choice = int(input("Guess a number (1-100): "))
        except ValueError:
            print("You should enter a number!")
            continue

        if choice > computer_choice:
            print("Your guess is too high.")
            print("Try again. ✖️")

        elif choice < computer_choice:
            print("Your guess is too low.")
            print("Try again. ✖️")

        else:
            print("That's correct! ✔️")

            while True:
                ask = input("Do you want to play again? (yes/no): ").lower()

                if ask == "yes":
                    print("Please wait...\n")
                    return guess_game()

                elif ask == "no":
                    print("Returning to the main menu...")
                    return 

                else:
                    print("Please enter 'yes' or 'no'.")

