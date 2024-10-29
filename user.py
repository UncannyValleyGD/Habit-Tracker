from habit import Habit

class User:
    def __init__(self, username):
        self.username = username
        self.habits = []

    def add_habit(self, name, periodicity):
        new_habit = Habit(name, periodicity)
        self.habits.append(new_habit)

    def complete_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                habit.complete_habit()

    def get_habits(self):
        return self.habits
