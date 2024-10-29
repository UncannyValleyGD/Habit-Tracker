import datetime

class Habit:
    def __init__(self, name, periodicity):
        """
        Initialize a new habit with a name and periodicity.
        Periodicity can be 'daily', 'weekly', etc.
        """
        self.name = name
        self.periodicity = periodicity
        self.checkoff_dates = []
        self.streak = 0

    def complete_habit(self):
        """
        Mark the habit as completed for the current day.
        If already completed today, notify the user.
        """
        today = datetime.date.today()
        
        # Check if the habit has already been completed today
        if today in self.checkoff_dates:
            print(f"Habit '{self.name}' has already been completed today.")
        else:
            self.checkoff_dates.append(today)
            self.update_streak()
            print(f"Habit '{self.name}' completed for today!")

    def update_streak(self):
        """
        Update the habit's streak based on consecutive completions.
        If the habit was completed yesterday, increment the streak.
        If not, reset the streak.
        """
        if len(self.checkoff_dates) > 1:
            last_date = self.checkoff_dates[-2]
            today = datetime.date.today()
            delta = (today - last_date).days

            # For daily habits
            if self.periodicity == 'daily' and delta == 1:
                self.streak += 1
            # For weekly habits
            elif self.periodicity == 'weekly' and delta == 7:
                self.streak += 1
            else:
                self.streak = 1  # Reset streak if not consecutive
        else:
            self.streak = 1  # First completion starts the streak

    def reset_streak(self):
        """
        Reset the streak when the habit is not completed as expected.
        """
        self.streak = 0

    def get_streak(self):
        """
        Return the current streak of the habit.
        """
        return self.streak

    def get_checkoff_dates(self):
        """
        Return the list of dates when the habit was completed.
        """
        return self.checkoff_dates

    def __str__(self):
        """
        Return a string representation of the habit.
        """
        return f"Habit(name={self.name}, periodicity={self.periodicity}, streak={self.streak})"
