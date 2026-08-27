# Personal Expense Tracker

A simple **terminal-based Personal Expense Tracker** built with Python.

This project was created to practice combining Python fundamentals into a small, working application. It allows users to record expenses, view them, search by amount or date, filter by category, and permanently store the data in a JSON file.

## Features

- Add a new expense
- Automatically record the current date
- View all recorded expenses in a formatted table
- Filter expenses by category
- Search expenses:
  - Before or equal to a specific date
  - After or equal to a specific date
  - Below or equal to a specific amount
  - Above or equal to a specific amount

- Calculate total spending
- Validate user input
- Handle invalid dates and amounts
- Save expenses to a JSON file
- Load previously saved expenses when the program starts

## Expense Data

Each expense is stored as a dictionary:

```python
{
    "name": "Lunch",
    "amount": 120,
    "category": "Food",
    "date": "27-08-2026"
}
```

All expenses are stored inside a list:

```python
expenses = []
```

## Menu

```text
===== Expense Tracker =====

1. Add expense
2. View all expense
3. Search expenses
4. Filter by category
5. Show total spending
6. Exit
```

### Search Options

The search menu provides four options:

```text
1. Search expenses before a specific date
2. Search expenses after a specific date
3. Search expenses below or equal to an amount
4. Search expenses above or equal to an amount
```

## Data Storage

The application uses a `data.json` file to store expenses.

When the program starts, it loads previously saved expenses from the file.

When a new expense is added, the updated expense list is saved to the JSON file.

This allows the data to remain available even after the program is closed.

## Technologies Used

- Python
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- `match` statements
- Exception handling
- JSON
- `datetime`
- String formatting

## Project Structure

The project intentionally uses a **single Python file** to keep the implementation simple and focused on Python fundamentals.

```text
expense_tracker/
│
├── expense_tracker.py
├── data.json
└── README.md
```

## How to Run

Make sure Python is installed, then run:

```bash
python expense_tracker.py
```

The program will create/use `data.json` for storing expenses.

## Future Improvements

This is a basic Version 1 implementation. Possible improvements include:

### Functionality

- Edit an expense
- Delete an expense
- Search by expense name or category
- Sort expenses by amount or date
- Show highest and lowest expense
- Show average spending
- Show daily or monthly spending
- Add a monthly budget and budget warnings

### Data & Project Improvements

- Export/import expenses using CSV
- Add unique IDs to expenses
- Add automated tests
- Improve error handling
- Improve the terminal interface
- Split the program into multiple modules

### Version 2 — OOP

Rebuild the project using **Object-Oriented Programming**.

For example:

```python
class Expense:
    ...

class ExpenseTracker:
    ...
```

The goal would be to redesign the application using classes rather than simply converting every function into a class method.

## Learning Goal

The main purpose of this project is **not the expense tracker itself**.

The goal is to practice turning individual Python concepts into a complete working program.

Instead of following a complete solution, try designing your own implementation and use documentation or small references only when you get stuck.
