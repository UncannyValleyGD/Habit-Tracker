from user import User

def main_menu():
    print("\n--- Goal Digger Habit Tracker ---")
    print("1. Add a New Habit")
    print("2. Complete a Habit")
    print("3. View Habits and Streaks")
    print("4. Exit")

def add_habit(user):
    name = input("Enter habit name: ")
    periodicity = input("Enter periodicity (daily/weekly): ")
    user.add_habit(name, periodicity)
    print(f"Habit '{name}' added.")

def complete_habit(user):
    habits = user.get_habits()

    if not habits:
        print("You have no active habits to complete.")
        return

    print("\nWhich habit would you like to complete?")
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit.name}")

    try:
        choice = int(input("\nEnter the number of the habit: "))
        if 1 <= choice <= len(habits):
            selected_habit = habits[choice - 1]
            selected_habit.complete_habit()
            print(f"Habit '{selected_habit.name}' marked as complete.")
        else:
            print("Invalid choice, please select a valid habit number.")
    except ValueError:
        print("Please enter a valid number.")

def view_habits(user):
    print("\nYour Habits:")
    for habit in user.get_habits():
        print(f"Habit: {habit.name}, Streak: {habit.get_streak()} days")
        
def main():
    username = input("Enter your username: ")
    user = User(username)
    
    while True:
        main_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            add_habit(user)
        elif choice == '2':
            complete_habit(user)
        elif choice == '3':
            view_habits(user)
        elif choice == '4':
            print("Exiting the Goal Digger Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
