# **Goal Digger \- Habit Tracking App**

**Goal Digger** is a command-line habit tracking app developed in Python. It allows users to create, manage, and track daily or weekly habits while monitoring streaks and providing basic analytics.

## **Features**

* **Create New Habits**: Track daily and weekly habits by setting a habit name and periodicity.  
* **Complete Habits**: Mark habits as complete to maintain streaks.  
* **Track Streaks**: View the longest streaks for your habits.  
* **Basic Analytics**: Access insights, such as longest habit streak, active habits, and habits by periodicity.

## **Installation**

**Clone the Repository**:

`git clone https://github.com/UncannyValleyGD/Habit-Tracker`  
`cd goal-digger`

1. **Install Requirements**:  
   * The project uses built-in Python libraries, so no external dependencies are required.  
   * Ensure you’re using **Python 3.7+**.

## **Usage**

Run the main script from the command line:

`python main.py`

Follow the prompts to create habits, mark them complete, and view streaks and analytics.

### **Example Commands**

* **Add a Habit**: Choose to add a new habit, set its name, and define periodicity (daily or weekly).  
* **Complete a Habit**: Select a habit from a numbered list to mark it as complete.  
* **View Habits and Analytics**: Access insights, longest streaks, and other analytics.

## **Project Structure**

`goal-digger/`  
`├── habit.py             # Contains the Habit class for individual habit tracking`  
`├── user.py              # Contains the User class for managing multiple habits`  
`├── main.py              # CLI for user interaction`  
`├── storage.py           # (Optional) Data storage handling (e.g., JSON saving/loading)`  
`├── tests/               # Unit tests for habit functionality and analytics`  
`├── data/                # Predefined habit data for testing (4 weeks of sample data)`  
`└── README.md            # Project documentation`

## **Analytics Module**

The analytics module includes:

* **Active Habits**: View all current habits.  
* **Habits by Periodicity**: Get habits grouped by daily/weekly periodicity.  
* **Longest Streaks**: View the longest streak across all habits or a specific habit.

## **Predefined Data for Testing**

The app includes 4 weeks of sample habit data located in the `data/` folder, useful for verifying streak calculations and analytics functions.

## **Contributing**

Contributions are welcome\! If you’d like to make improvements, feel free to fork the project and submit a pull request.

## **License**

This project is licensed under the MIT License.

