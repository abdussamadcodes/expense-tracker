import json
import datetime
import time

expenses = []


def load_data():
    with open("data.json") as f:
        if not f.read().strip():
            expenses[:] = []
        else:
            f.seek(0)
            value = json.load(f)
            expenses[:] = value


def store_data():
    with open("data.json", "w") as f:
        json.dump(expenses, f, indent=4)


def getValidAmount():
    while True:
        try:
            amount = int(input("enter the price: "))
        except:
            print("price should be int")
        else:
            if amount > 0:
                return amount
            else:
                print("price should be greater than 0")


def add_expense():
    while True:
        name = input("enter product name: ")
        if name == "":
            print("name should not be empty")
        else:
            break
    amount = getValidAmount()
    while True:
        category = input("enter your category: ")
        if category == "":
            print("name should not be empty")
        else:
            break

    date = datetime.datetime.now().strftime("%d-%m-%Y")
    expenses.append(
        {"name": name, "amount": amount, "category": category, "date": date}
    )
    store_data()
    time.sleep(0.5)


def getValidChoice(index):
    choice = int()
    while True:
        try:
            choice = int(input("enter your choice: "))
        except:
            print("wrong choice. input should be string.")
        else:
            if choice in range(1, index):
                return choice
            else:
                print(f"wrong choice. input should be between 1 to {index-1}")


def view_all_expense():
    print(f"{"Name":<15}{"Amount":<13}{"Category":<20}{"date":<12}")
    print("=" * 58)
    for value in expenses:
        print(
            f"{value["name"]:<15}{value["amount"]:<13.2f}{value["category"]:<20}{value["date"]:<12}"
        )
    time.sleep(0.5)


def mainMenu():
    while True:
        load_data()
        print("")
        print("===== Expense Tracker =====")
        print("")
        print("""1.Add expense
2.View all expense
3.Search expenses
4.Filter by category
5.Show total spending
6.Export data
7.Exit""")
        load_data()
        choice = getValidChoice(8)
        match choice:
            case 1:
                add_expense()
            case 2:
                view_all_expense()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass


mainMenu()
