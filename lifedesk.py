# ==========================================
# LifeDesk - Personal Management System
# ==========================================

# List to store all registered users
user = []

# Starting ID for new users
next_user_id = 1000

# List to store all expenses
expenses = []

# Starting ID for new expenses
next_expense_id = 5000

# Monthly budget (None means no budget has been set)
monthly_bud = None

# List to store all tasks
task = []

# Starting ID for new tasks
new_task_id = 100

# List to store all goals
goals = []

# Starting ID for new goals
next_goal_id = 200


# ==========================================
# Main Menu
# ==========================================

while True:

    print("""
=============== LifeDesk ===============
          Welcome to LifeDesk!!!

What it does?
It is a terminal-based personal management application that helps
you manage your personal activities.

Choose an option:

1. User Management
2. Expense Manager
3. Budget Manager
4. Task Manager
5. Goal Tracker
6. Dashboard
7. Exit
========================================
""")

    try:
        choice = int(input("Enter your choice: "))

        # ==========================================
        # OPTION 1: USER MANAGEMENT
        # ==========================================

        if choice == 1:

            while True:

                print("""
========== User Management ==========

1. Register New User
2. View All Users
3. Search User by ID
4. Delete User by ID
5. Back to Main Menu

=====================================
""")

                option = int(input("Enter your option: "))

                # OPTION 1: REGISTER NEW USER
                if option == 1:

                    user_id = next_user_id
                    next_user_id += 1

                    name = input("Enter your name: ")

                    while True:
                        try:
                            age = int(input("Enter your age: "))
                            if age > 0:
                                break
                            else:
                                print("Age should be greater than zero!")

                        except ValueError:
                            print("Please enter a valid age!")

                    city = input("Enter your city: ")

                    user_profile = {
                        "user_id": user_id,
                        "user_name": name,
                        "user_age": age,
                        "user_city": city
                    }

                    user.append(user_profile)

                    print("\\nUser registered successfully!")
                    print(f"Your User ID is: {user_id}")

                # OPTION 2: VIEW ALL USERS
                elif option == 2:

                    if not user:
                        print("No User registered yet!")

                    else:
                        print("\\n========== Registered Users ==========")

                        for details in user:

                            print(f"""
User ID: {details['user_id']}
User Name: {details['user_name']}
User Age: {details['user_age']}
City: {details['user_city']}
---------------------------------------
""")

                # OPTION 3: SEARCH USER BY ID
                elif option == 3:

                    if not user:
                        print("No users registered yet!")

                    else:

                        user_id = int(input("Enter User ID: "))

                        found = False

                        for details in user:

                            if user_id == details['user_id']:

                                found = True

                                print(f"""
========== User Details ==========

User ID: {details['user_id']}
User Name: {details['user_name']}
User Age: {details['user_age']}
City: {details['user_city']}

==================================
""")

                        if not found:
                            print("Invalid User ID!")

                # OPTION 4: DELETE USER BY ID
                elif option == 4:

                    if not user:
                        print("No users registered yet!")

                    else:

                        user_id = int(input("Enter User ID: "))

                        found = False

                        for details in user:

                            if user_id == details['user_id']:

                                found = True

                                print(f"""
========== User Details ==========

User ID: {details['user_id']}
User Name: {details['user_name']}
User Age: {details['user_age']}
City: {details['user_city']}

==================================
""")

                                print("Are you sure you wanna delete your details?")

                                ans = input("Please enter (yes/no): ")

                                if ans.lower() == "yes":

                                    user.remove(details)

                                    print("User deleted successfully!")

                                else:
                                    print("Deletion Cancelled!")

                                break

                        if not found:
                            print("Invalid User ID!")

                # OPTION 5: BACK TO MAIN MENU
                elif option == 5:
                    break

                else:
                    print("Invalid User Management option!")


        # ==========================================
        # OPTION 2: EXPENSE MANAGER
        # ==========================================

        elif choice == 2:

            while True:

                print("""
========== Expense Manager ==========

1. Add New Expense
2. View All Expenses
3. Search Expense by ID
4. Update Expense
5. Delete Expense
6. View Expense Summary
7. Back to Main Menu

=====================================
""")

                option = int(input("Enter your option: "))

                # OPTION 1: ADD NEW EXPENSE
                if option == 1:

                    exp_id = next_expense_id
                    next_expense_id += 1

                    exp_name = input(
                        "Enter Expense name (for e.g. Groceries, Electricity, etc): "
                    )

                    amount = int(input("Enter Amount: "))

                    exp_cate = input(
                        "Enter Category (for e.g. Food, Travel, etc): "
                    )

                    date = input("Enter Date (format: dd-mm-yyyy): ")

                    exp = {
                        "exp_id": exp_id,
                        "exp_name": exp_name,
                        "exp_amount": amount,
                        "exp_category": exp_cate,
                        "date": date
                    }

                    expenses.append(exp)

                    print("\\nExpense added successfully!")
                    print(f"Expense ID: {exp_id}")

                # OPTION 2: VIEW ALL EXPENSES
                elif option == 2:

                    if not expenses:
                        print("No expenses recorded yet!")

                    else:

                        print("\\n========== All Expenses ==========")

                        for details in expenses:

                            print(f"""
Expense ID: {details['exp_id']}
Expense Name: {details['exp_name']}
Amount: ₹{details['exp_amount']}
Category: {details['exp_category']}
Date: {details['date']}
""")

                            print("-----------------------------------")

                # OPTION 3: SEARCH EXPENSE BY ID
                elif option == 3:

                    if not expenses:
                        print("No expenses recorded yet!")

                    else:

                        exp_id = int(input("Enter Expense ID: "))

                        found = False

                        for details in expenses:

                            if exp_id == details['exp_id']:

                                found = True

                                print(f"""
========== Expense Details ==========

Expense ID: {details['exp_id']}
Expense Name: {details['exp_name']}
Amount: ₹{details['exp_amount']}
Category: {details['exp_category']}
Date: {details['date']}

=====================================
""")

                        if not found:
                            print("Invalid Expense ID!")

                # OPTION 4: UPDATE EXPENSE
                elif option == 4:

                    if not expenses:
                        print("No expenses recorded yet!")

                    else:
                        exp_id = int(input("Enter Expense ID: "))

                        found = False

                        for details in expenses:

                            if exp_id == details['exp_id']:

                                found = True

                                print(f"""
========== Expense Details ==========

Expense ID: {details['exp_id']}
Expense Name: {details['exp_name']}
Amount: ₹{details['exp_amount']}
Category: {details['exp_category']}
Date: {details['date']}

=====================================
""")

                                while True:

                                    print("""Which details you want to update:
1. Update Expense Name
2. Update Amount
3. Update Category
4. Update Date
5. Exit
""")

                                    new_option = int(input("Enter your option: "))

                                    if new_option == 1:
                                        name = input("Enter the new name: ")
                                        details['exp_name'] = name
                                        print("Name Updated Successfully!")

                                    elif new_option == 2:
                                        amount = int(input("Enter the new amount: "))
                                        details['exp_amount'] = amount
                                        print("Amount Updated Successfully!")

                                    elif new_option == 3:
                                        category = input("Enter the new category: ")
                                        details['exp_category'] = category
                                        print("Category Updated Successfully!")

                                    elif new_option == 4:
                                        date = input("Enter the new date: ")
                                        details['date'] = date
                                        print("Date Updated Successfully!")

                                    elif new_option == 5:
                                        break

                                    else:
                                        print("Invalid option!")

                        if not found:
                            print("Invalid Expense ID!")

                # OPTION 5: DELETE EXPENSE
                elif option == 5:

                    if not expenses:
                        print("No expenses recorded yet!")

                    else:

                        exp_id = int(input("Enter Expense ID: "))

                        found = False

                        for details in expenses:

                            if exp_id == details['exp_id']:

                                found = True

                                print(f"""
========== Expense Details ==========

Expense ID: {details['exp_id']}
Expense Name: {details['exp_name']}
Amount: ₹{details['exp_amount']}
Category: {details['exp_category']}
Date: {details['date']}

=====================================
""")

                                print("Are you sure you wanna delete the details?")
                                ans = input("Please enter (yes/no): ")

                                if ans.lower() == "yes":

                                    expenses.remove(details)

                                    print("Expense deleted successfully!")

                                else:
                                    print("Deletion Cancelled!")

                                break

                        if not found:
                            print("Invalid Expense ID!")

                # OPTION 6: EXPENSE SUMMARY
                elif option == 6:

                    if not expenses:
                        print("No expenses recorded yet!")

                    else:
                        total_expenses = len(expenses)

                        total_amount = sum(
                            details['exp_amount'] for details in expenses
                        )

                        average_expense = total_amount / total_expenses

                        highest_expense = max(
                            details['exp_amount'] for details in expenses
                        )

                        lowest_expense = min(
                            details['exp_amount'] for details in expenses
                        )

                        category_totals = {}

                        for details in expenses:

                            category_name = details['exp_category']

                            if category_name in category_totals:
                                category_totals[category_name] += details['exp_amount']

                            else:
                                category_totals[category_name] = details['exp_amount']

                        print("""
========== EXPENSE SUMMARY ==========
""")

                        print(f"Total Expenses: {total_expenses}")
                        print(f"Total Amount Spent: ₹{total_amount:.2f}")
                        print(f"Average Expense: ₹{average_expense:.2f}")
                        print(f"Highest Expense: ₹{highest_expense:.2f}")
                        print(f"Lowest Expense: ₹{lowest_expense:.2f}")

                        print("""
------ Category-wise Spending ------
""")

                        for category_name, amount in category_totals.items():
                            print(f"{category_name}: ₹{amount:.2f}")

                        print("""
=====================================
""")

                # OPTION 7: BACK TO MAIN MENU
                elif option == 7:
                    break

                else:
                    print("Invalid Expense Manager option!")


        # ==========================================
        # OPTION 3: BUDGET MANAGER
        # ==========================================

        elif choice == 3:

            while True:

                print("""
========== Budget Manager ==========

1. Set Monthly Budget
2. View Budget
3. Update Monthly Budget
4. Check Budget Status
5. Back to Main Menu

====================================
""")

                option = int(input("Enter your option: "))

                # OPTION 1: SET MONTHLY BUDGET
                if option == 1:

                    while True:
                        try:
                            budget = int(input("Enter your budget: "))

                            if budget > 0:
                                monthly_bud = budget
                                print("The budget is saved successfully!")
                                break

                            else:
                                print("The budget should be greater than zero!")

                        except ValueError:
                            print("Please enter a valid budget amount!")

                # OPTION 2: VIEW BUDGET
                elif option == 2:

                    if monthly_bud is None:
                        print("No budget has been set yet!")

                    else:
                        print(f"Monthly Budget: ₹{monthly_bud}")

                # OPTION 3: UPDATE MONTHLY BUDGET
                elif option == 3:

                    if monthly_bud is None:
                        print("No budget has been set yet!")

                    else:

                        while True:
                            try:
                                new_bud = int(input("Enter your new budget: "))

                                if new_bud > 0:
                                    monthly_bud = new_bud
                                    print("The new budget is saved successfully!")
                                    break

                                else:
                                    print("The budget should be greater than zero!")

                            except ValueError:
                                print("Please enter a valid budget amount!")

                # OPTION 4: CHECK BUDGET STATUS
                elif option == 4:

                    if monthly_bud is None:
                        print("No budget has been set yet!")

                    else:

                        # Calculate the total number of expense records
                        total_expenses = len(expenses)

                        # Calculate the total amount spent
                        total_amount = sum(
                            details['exp_amount'] for details in expenses
                        )

                        # Calculate remaining budget
                        rem_bud = monthly_bud - total_amount

                        print(f"""
========== BUDGET STATUS ==========

Monthly Budget: ₹{monthly_bud}
Number of Expenses: {total_expenses}
Total Expenses: ₹{total_amount}
""")

                        # Check whether the budget is underspent
                        if total_amount < monthly_bud:

                            print(f"Remaining Budget: ₹{rem_bud}")
                            print(
                                f"You are under budget! "
                                f"You have ₹{rem_bud} remaining."
                            )

                        # Check whether the entire budget is spent
                        elif total_amount == monthly_bud:

                            print("Remaining Budget: ₹0")
                            print(
                                "You have spent your entire budget. "
                                "No balance remaining!"
                            )

                        # Check whether the user has overspent
                        else:

                            rem_amt = total_amount - monthly_bud

                            print(f"Overspent Amount: ₹{rem_amt}")
                            print(f"You have overspent by ₹{rem_amt}!")

                        print("""
===================================
""")

                # OPTION 5: BACK TO MAIN MENU
                elif option == 5:
                    break

                else:
                    print("Invalid Budget Manager option!")


        # ==========================================
        # OPTION 4: TASK MANAGER
        # ==========================================

        elif choice == 4:

            while True:

                print("""
========== Task Manager ==========

1. Add New Task
2. View All Tasks
3. Mark Task as Completed
4. Delete Task
5. Back to Main Menu

==================================
""")

                option = int(input("Enter your option: "))

                # OPTION 1: ADD NEW TASK
                if option == 1:

                    task_id = new_task_id
                    new_task_id += 1

                    task_name = input("Enter Task Name: ")
                    task_status = "Pending"

                    tasks = {
                        "task_id": task_id,
                        "task_name": task_name,
                        "task_status": task_status
                    }

                    task.append(tasks)

                    print("Task added successfully!")

                    print(f"""
Task ID: {tasks['task_id']}
Task Name: {tasks['task_name']}
Task Status: {tasks['task_status']}
""")

                # OPTION 2: VIEW ALL TASKS
                elif option == 2:

                    if not task:
                        print("No task added yet!")

                    else:

                        for details in task:

                            print(f"""
Task ID: {details['task_id']}
Task Name: {details['task_name']}
Task Status: {details['task_status']}
""")

                            print("-------------------------------")

                # OPTION 3: MARK TASK AS COMPLETED
                elif option == 3:

                    if not task:
                        print("No task added yet!")

                    else:

                        task_id = int(input("Enter Task ID: "))

                        found = False

                        for details in task:

                            if task_id == details['task_id']:

                                found = True

                                if details['task_status'] == "Pending":

                                    details['task_status'] = "Completed"

                                    print("Task marked as completed successfully!")

                                elif details['task_status'] == "Completed":

                                    print("The task is already completed!")

                        if not found:
                            print("Invalid Task ID!")

                # OPTION 4: DELETE TASK
                elif option == 4:

                    if not task:
                        print("No task added yet!")

                    else:

                        task_id = int(input("Enter Task ID: "))

                        found = False

                        for details in task:

                            if task_id == details['task_id']:

                                found = True

                                print(f"""
Task ID: {details['task_id']}
Task Name: {details['task_name']}
Task Status: {details['task_status']}
""")

                                new_option = input(
                                    "Do you want to delete this task (yes/no): "
                                )

                                if new_option.lower() == "yes":

                                    task.remove(details)

                                    print("Task deleted successfully!")

                                else:
                                    print("Deletion Cancelled!")

                                break

                        if not found:
                            print("Invalid Task ID!")

                # OPTION 5: BACK TO MAIN MENU
                elif option == 5:
                    break

                else:
                    print("Invalid Task Manager option!")


        # ==========================================
        # OPTION 5: GOAL TRACKER
        # ==========================================

        elif choice == 5:

            while True:

                print("""
========== Goal Tracker ==========

1. Add New Goal
2. View All Goals
3. Update Goal Progress
4. Delete Goal
5. Back to Main Menu

=================================
""")

                option = int(input("Enter your option: "))

                # OPTION 1: ADD NEW GOAL
                if option == 1:

                    goal_id = next_goal_id
                    next_goal_id += 1

                    goal_name = input("Enter goal name: ")
                    goal_target = int(input("Enter your target: "))

                    if goal_target > 0:

                        goal_progress = 0

                        goal_details = {
                            "goal_id": goal_id,
                            "goal_name": goal_name,
                            "goal_target": goal_target,
                            "goal_progress": goal_progress
                        }

                        goals.append(goal_details)

                        print("Goal added successfully!")
                        print(f"Your Goal ID is: {goal_id}")

                    else:
                        print("Target should be greater than zero!")

                # OPTION 2: VIEW ALL GOALS
                elif option == 2:

                    if not goals:
                        print("No goals have been added yet!")

                    else:

                        for details in goals:

                            percentage = (
                                details["goal_progress"] / details["goal_target"]
                            ) * 100

                            print(f"""
---------------------------------
Goal ID: {details['goal_id']}
Goal Name: {details['goal_name']}
Target: {details['goal_target']}
Progress: {details['goal_progress']}
Completion: {percentage:.1f}%
---------------------------------
""")

                # OPTION 3: UPDATE GOAL PROGRESS
                elif option == 3:

                    if not goals:
                        print("No goals available to update!")

                    else:

                        search_id = int(input("Enter Goal ID: "))
                        found = False

                        for details in goals:

                            if details["goal_id"] == search_id:

                                found = True

                                print("Goal Name:", details["goal_name"])
                                print("Current Progress:", details["goal_progress"])

                                new_progress = int(
                                    input("Enter updated progress: ")
                                )

                                if (new_progress >= 0 and
                                        new_progress <= details["goal_target"]):

                                    details["goal_progress"] = new_progress
                                    print("Goal progress updated successfully!")

                                else:
                                    print(
                                        "Progress must be between 0 and your target!"
                                    )

                                break

                        if not found:
                            print("Invalid Goal ID!")

                # OPTION 4: DELETE GOAL
                elif option == 4:

                    if not goals:
                        print("No goals available to delete!")

                    else:

                        search_id = int(input("Enter Goal ID: "))
                        found = False

                        for details in goals:

                            if details["goal_id"] == search_id:

                                found = True

                                print("Goal Name:", details["goal_name"])

                                ans = input(
                                    "Are you sure you want to delete this goal? (yes/no): "
                                )

                                if ans.lower() == "yes":

                                    goals.remove(details)
                                    print("Goal deleted successfully!")

                                else:
                                    print("Goal deletion cancelled!")

                                break

                        if not found:
                            print("Invalid Goal ID!")

                # OPTION 5: BACK TO MAIN MENU
                elif option == 5:
                    break

                else:
                    print("Invalid Goal Tracker option!")


        # ==========================================
        # OPTION 6: DASHBOARD
        # ==========================================

        elif choice == 6:

            print("""
=================================
       LIFEDESK DASHBOARD
=================================
""")

            # USER OVERVIEW
            print("\n----- USER OVERVIEW -----")
            print("Total Registered Users:", len(user))

            # EXPENSE OVERVIEW
            print("\n----- EXPENSE OVERVIEW -----")
            total_expenses = len(expenses)
            total_amount = sum(
                details["exp_amount"] for details in expenses
            )

            print("Total Number of Expenses:", total_expenses)
            print(f"Total Amount Spent: ₹{total_amount}")

            # BUDGET OVERVIEW
            print("\n----- BUDGET OVERVIEW -----")

            if monthly_bud is None:
                print("No monthly budget has been set yet!")

            else:
                print(f"Monthly Budget: ₹{monthly_bud}")

                remaining_budget = monthly_bud - total_amount

                if remaining_budget > 0:
                    print(f"Remaining Budget: ₹{remaining_budget}")
                    print("Budget Status: Within Budget")

                elif remaining_budget == 0:
                    print("Remaining Budget: ₹0")
                    print("Budget Status: Budget Fully Used")

                else:
                    overspent = abs(remaining_budget)
                    print(f"Overspent Amount: ₹{overspent}")
                    print("Budget Status: Budget Exceeded")

            # TASK OVERVIEW
            print("\n----- TASK OVERVIEW -----")

            total_tasks = len(task)
            pending_tasks = 0
            completed_tasks = 0

            for details in task:

                if details["task_status"] == "Pending":
                    pending_tasks += 1

                elif details["task_status"] == "Completed":
                    completed_tasks += 1

            print("Total Tasks:", total_tasks)
            print("Pending Tasks:", pending_tasks)
            print("Completed Tasks:", completed_tasks)

            # GOAL OVERVIEW
            print("\n----- GOAL OVERVIEW -----")

            total_goals = len(goals)
            completed_goals = 0

            for details in goals:
                if details["goal_progress"] == details["goal_target"]:
                    completed_goals += 1

            print("Total Goals:", total_goals)
            print("Completed Goals:", completed_goals)
            print("In-progress Goals:", total_goals - completed_goals)

            print("\n=================================")
            print("          END OF DASHBOARD")
            print("=================================")


        # ==========================================
        # OPTION 7: EXIT
        # ==========================================

        elif choice == 7:

            print("Thankyou for using LifeDesk!!!")

            break


        # INVALID MAIN MENU OPTION
        else:
            print("Invalid choice!!!")

    except ValueError:
        print("Please enter a valid number!")


# Displaying final data (for testing)
print(user)
print(expenses)
print(task)
print(goals)
