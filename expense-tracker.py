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
    name = input("enter your name: ")
    amount = getValidAmount()
    category = input("enter your category: ")
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    expenses.append(
        {"name": name, "amount": amount, "category": category, "date": date}
    )
    store_data()


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


def mainMenu():
    while True:
        load_data()
        print("===== Expense Tracker =====")
        print("""1.Add expense
2.View all expense
3.Search expenses
4.Filter by category
5.Show total spending
6.Export data
7.Exit
""")
        load_data()
        choice = getValidChoice(8)
        match choice:
            case 1:
                add_expense()
            case 2:
                pass
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
