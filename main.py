from functions import add_user, add_habit, log_habit, show_habits, show_streak, show_all_habits

def main():
    user = None
    while True:
        print("\n--- Habit Tracker Menu ---")
        print("1. Add user")
        print("2. Add habit")
        print("3. Log habit")
        print("4. Show habits")
        print("5. Show streak")
        print("6. Show all habits")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user = add_user()
        elif choice == "2":
            if not user:
                print(" First create/select a user.")
                continue
            add_habit(user)
        elif choice == "3":
            if not user:
                print(" First create/select a user.")
                continue
            log_habit(user)
        elif choice == "4":
            if not user:
                print("First create/select a user.")
                continue
            show_habits(user)
        elif choice == "5":
            show_streak()
        elif choice == "6":
            show_all_habits()
        elif choice == "0":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()
