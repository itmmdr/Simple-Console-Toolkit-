from calculator import calculator
from converter import converter
from grade_manager import grade_manager
from guess_game import guess_game


def main():
    while True:
        print("\n" + "=" * 30)
        print("      PYTHON TOOLKIT MENU")
        print("=" * 30)
        print("1. Calculator")
        print("2. Converter")
        print("3. Grade Manager")
        print("4. Guess Game")
        print("5. Exit")
        print("=" * 30)

        ask_chose = input("Choose an option: ").strip().lower()

        if ask_chose in ['1', 'calculator']:
            calculator()

        elif ask_chose in ['2', 'converter']:
            converter()

        elif ask_chose in ['3', 'grade manager', 'grade']:
            grade_manager()

        elif ask_chose in ['4', 'guess game', 'guess']:
            guess_game()

        elif ask_chose in ['5', 'exit', 'quit']:
            print("\nGoodbye 👋 Thanks for using Toolkit!")
            break

        else:
            print("\n❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()