filename = "expenses.txt"
def add_expense():
    try:
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category (Food/Travel/Shopping/etc.): ")
        amount = float(input("Enter Amount: "))
        with open(filename, "a") as file:
            file.write(f"{date},{category},{amount}")
        print("Expense Added Successfully!")
    except ValueError:
        print("Invalid Amount! Please enter a number.")
def view_expenses():
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            if len(data) == 0:
                print("No Expenses Found.")
            else:
                print("Expense List")
                for line in data:
                    print(line.strip())
    except FileNotFoundError:
        print("Expense file not found!")
def summary():
    try:
        totals = {}
        with open(filename, "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                amount = float(amount)
                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount
        print("Expense Summary")
        for category, total in totals.items():
            print(category, ":", total)
    except FileNotFoundError:
        print("Expense file not found!")
while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        summary()
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")