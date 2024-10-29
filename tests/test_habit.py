import unittest
from habit import Habit

class TestHabit(unittest.TestCase):
    def setUp(self):
        self.habit = Habit(name="Exercise", periodicity="daily")

    def test_complete_habit(self):
        self.habit.complete_habit()
        self.assertEqual(self.habit.get_streak(), 1)

    def test_streak_resets(self):
        self.habit.complete_habit()
        # Simulate a missed day for daily habit
        self.habit.reset_streak()
        self.assertEqual(self.habit.get_streak(), 0)

if __name__ == '__main__':
    unittest.main()
