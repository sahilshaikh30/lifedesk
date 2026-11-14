# LifeDesk

A terminal-based personal management application that brings several everyday tools into one program: user profiles, expense tracking, a monthly budget, a task list, goal tracking, and a combined dashboard. Built as a larger beginner project to practice structuring a bigger program with many connected parts.

## Features
- **User management:** register, view, search, and delete users
- **Expense manager:** add, view, search, update, and delete expenses, plus a summary with total, average, highest, lowest, and category-wise spending
- **Budget manager:** set, view, and update a monthly budget, and check whether you are under, at, or over budget
- **Task manager:** add tasks, mark them as completed, and delete them
- **Goal tracker:** set a target, update progress, and see the completion percentage
- **Dashboard:** one screen with the overview of users, expenses, budget, tasks, and goals

## Tech used
- Python 3
- Standard library only (no installs needed)

## How to run
1. Make sure Python 3 is installed
2. Download or clone this repo
3. Run:
   ```
   python lifedesk.py
   ```
4. Use the main menu by typing a number from 1 to 7

## What I practiced
- Storing records as dictionaries inside lists, with auto-generated IDs
- Nested menus using `while` loops
- Full create, read, update, and delete (CRUD) operations for several data types
- `try/except` for invalid menu input and validation loops for age and budget
- Using `sum()`, `max()`, and `min()` with generator expressions to build summaries
- Grouping data with dictionaries (category-wise spending)

## Known issues
- Data is stored in memory only, so everything is lost when the program closes
- Invalid input inside a sub-menu (for example, text instead of a number) sends you back to the main menu
- Some `print` statements show a literal `\n` instead of a blank line
- Dates are stored as plain text and are not validated
- Expense categories are free text, so "food" and "Food" count as different categories
- Expenses are not linked to a user or to a month, so the budget check counts every expense ever added
- The program prints all stored data again when it exits (left in for testing)
- The repeated menu and display code could be shortened with functions

## Planned improvements
- Break the code into functions and separate modules
- Save and load data using SQLite or JSON files
- Link expenses, tasks, and goals to specific users
- Filter expenses by month so the budget check is accurate
- Validate all numeric and date input
- Add charts for spending using pandas and matplotlib
