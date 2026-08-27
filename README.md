# Personal Expense Tracker

## Project Difficulty

**Easy → Medium**

## Project Overview

Build a terminal-based **Personal Expense Tracker** using Python.

The goal of this project is to practice Python by building a complete small application rather than solving isolated programming exercises.

The application should allow a user to record expenses, view and search their expenses, filter them by category, calculate spending statistics, and store their data permanently using JSON.

---

## Basic Interface

The program should provide a menu similar to:

```text
===== EXPENSE TRACKER =====

1. Add expense
2. View all expenses
3. Search expenses
4. Filter by category
5. Show total spending
6. Show spending by category
7. Export data
8. Exit
```

You may design the interface differently. The menu above is only a suggested starting point.

---

## Expense Data

Each expense can be represented using a dictionary:

```python
{
    "name": "Lunch",
    "amount": 120,
    "category": "Food",
    "date": "2026-08-26"
}
```

The application can initially store expenses in a list:

```python
expenses = []
```

You should decide how to organize and validate the data as you build the project.

---

# Version 1 — Functional Implementation

Do **not** use classes initially.

Build the first version using:

- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- User input
- Exception handling
- Modules

### Required Features

### 1. Add Expense

Allow the user to enter:

- Expense name
- Amount
- Category
- Date

Example:

```text
Expense name: Lunch
Amount: 120
Category: Food
Date: 2026-08-26
```

Validate the user's input.

For example:

- Amount should be a valid number.
- Expense name should not be empty.
- Date should follow the expected format.
- Category should not be empty.

---

### 2. View All Expenses

Display all recorded expenses in a readable format.

For example:

```text
Name        Amount      Category       Date
------------------------------------------------
Lunch       120.00      Food           2026-08-26
Bus fare     40.00      Transport      2026-08-26
Book        500.00      Education      2026-08-25
```

You may design your own formatting.

---

### 3. Search Expenses

Allow the user to search expenses.

Possible searches include:

- Expense name
- Category
- Partial text

For example:

```text
Search: lunch
```

could find:

```text
Lunch - 120 - Food - 2026-08-26
```

The search should ideally be case-insensitive.

---

### 4. Filter by Category

Allow the user to enter a category and display only expenses belonging to that category.

Example:

```text
Category: Food
```

Output:

```text
Lunch       120
Dinner      250
Snacks       80
```

---

### 5. Show Total Spending

Calculate the total amount spent.

Example:

```text
Total spending: 4,750.00
```

---

### 6. Show Spending by Category

Calculate how much money has been spent in each category.

Example:

```text
===== SPENDING BY CATEGORY =====

Food:        1,850
Transport:     700
Education:   1,200
Shopping:    1,000
```

The categories should be calculated from the stored expenses rather than manually hard-coded.

---

### 7. Export Data

Allow the user to export their expense data.

For the first version, JSON is recommended.

Example:

```json
[
  {
    "name": "Lunch",
    "amount": 120,
    "category": "Food",
    "date": "2026-08-26"
  }
]
```

You can optionally add another export format later, such as CSV.

---

### 8. Exit

When the user chooses Exit, the program should terminate cleanly.

---

# Persistent Storage

The program should not lose all expenses when it closes.

Store the expenses in a JSON file.

For example:

```text
data.json
```

When the application starts:

1. Check whether the JSON file exists.
2. If it exists, load the saved expenses.
3. If it does not exist, start with an empty list.

When the application exits:

1. Save the current expenses to the JSON file.

This allows the program to remember expenses between different executions.

---

# Input Validation

The program should handle invalid user input gracefully.

For example:

```text
Amount: abc

Invalid amount. Please enter a valid number.
```

The program should not crash simply because the user entered invalid data.

Use appropriate exception handling such as:

```python
try:
    ...
except ValueError:
    ...
```

Think about other invalid inputs that your program should handle.

---

# Date Handling

Use Python's `datetime` functionality to work with dates.

The program should validate dates instead of simply accepting any string.

For example:

```text
2026-08-26
```

is valid if that is the format you choose.

You may later add features such as:

- Today's expenses
- Expenses from a specific date
- Expenses from a date range
- Monthly spending

These are optional extensions.

---

# Project Structure

Once the program becomes larger, separate the code into modules.

A possible structure is:

```text
expense_tracker/
│
├── main.py
├── expenses.py
├── utils.py
├── data.json
└── README.md
```

Possible responsibilities:

### `main.py`

Responsible for:

- Running the application
- Displaying the menu
- Getting the user's choice
- Calling the appropriate functions

### `expenses.py`

Responsible for expense-related operations such as:

- Adding expenses
- Searching
- Filtering
- Calculating totals
- Calculating category statistics

### `utils.py`

Responsible for reusable utility functions such as:

- Input validation
- Date validation
- Formatting
- JSON loading/saving

You may organize the modules differently if you have a better design.

---

# Important Rule

**Do not use classes in Version 1.**

Use functions and dictionaries first.

The purpose is to understand how to build the application using the Python fundamentals you have learned.

---

# Version 2 — Object-Oriented Version

After completing Version 1, rebuild the project using OOP.

Possible classes:

```python
class Expense:
    ...
```

and:

```python
class ExpenseTracker:
    ...
```

You should decide yourself:

- What data belongs inside each class
- What methods each class should have
- How the classes should interact
- How JSON data should be converted into objects
- How objects should be saved back to JSON

Do not simply copy Version 1 and put everything inside classes.

Try to redesign the application using proper object-oriented thinking.

---

# Optional Challenges

After completing the required features, you can make the project more advanced.

Possible extensions:

- Delete an expense
- Edit an expense
- Sort expenses by amount
- Sort expenses by date
- Search by date
- Filter by date range
- Show daily spending
- Show monthly spending
- Set a monthly budget
- Warn when the budget is exceeded
- Show the highest expense
- Show the lowest expense
- Show average expense
- Export to CSV
- Import expenses from CSV
- Add recurring expenses
- Add unique expense IDs
- Add pagination for large datasets
- Add confirmation before deleting an expense
- Add a configuration file
- Add automated tests

---

# Recommended Development Order

Do not try to build everything at once.

Build incrementally:

```text
1. Create the menu
        ↓
2. Add expenses to a list
        ↓
3. View expenses
        ↓
4. Calculate total spending
        ↓
5. Add searching
        ↓
6. Add category filtering
        ↓
7. Add spending-by-category statistics
        ↓
8. Add input validation
        ↓
9. Add date handling
        ↓
10. Add JSON saving/loading
        ↓
11. Split code into modules
        ↓
12. Improve the user interface
        ↓
13. Rebuild using OOP
        ↓
14. Add optional advanced features
```

---

# Learning Goals

This project is designed to practice:

- Variables
- Data types
- Strings
- Lists
- Dictionaries
- Loops
- Conditional statements
- Functions
- Function arguments
- `*args` / `**kwargs` where appropriate
- Exception handling
- Modules
- File handling
- JSON
- Date/time handling
- String formatting
- Input validation
- Searching and filtering
- Basic program architecture
- Object-oriented programming

---

# Challenge Philosophy

Do not copy a complete solution from the internet.

The purpose of this project is to make you think about how different Python concepts work together in a real program.

It is completely fine to look up:

- Python documentation
- Syntax you forgot
- How a library function works
- Error messages
- Small implementation details

But try to design and implement the solution yourself.

If you get stuck, break the problem into smaller functions and solve one piece at a time.

---

# Final Goal

By the end of the project, you should have a functional terminal application that can:

```text
Add expenses
      ↓
Store expenses
      ↓
Search / filter expenses
      ↓
Calculate statistics
      ↓
Save data
      ↓
Load data later
```

Then rebuild the same application using **object-oriented programming**.

The real objective is not the expense tracker itself.

The objective is to learn how to turn individual Python concepts into a complete, maintainable program.
