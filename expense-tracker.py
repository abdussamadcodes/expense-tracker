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


def getValidChoice(index: int):
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
    print(f"{"#":<5}{"Name":<15}{"Amount":<13}{"Category":<20}{"date":<12}")
    print("=" * 63)
    i=0
    for expense in expenses:
        i+=1
        print(
            f"{i:<5}{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<20}{expense["date"]:<12}"
        )
    time.sleep(0.5)


def getValidDate():
    while True:
        try:
            dd, mm, yyyy = map(int, input("enter the date like dd-mm-yyyy: ").split())
        except:
            print("input should be int")
        else:
            try:
                date = datetime.datetime(yyyy, mm, dd).strftime("%d-%m-%Y")
            except:
                print(
                    "Invalid date input.Like month is between 1-12 and day is between 1-31 except february"
                )
            else:
                return date


def filter_by_category():
    uniq_category = set()
    for expense in expenses:
        uniq_category.add(expense["category"])
    i = 1
    for expense in uniq_category:
        print(f"{i}.", expense, sep="")
        i += 1
    category = list(uniq_category)
    choice = getValidChoice(len(category) + 1)
    print(f"{"Name":<15}{"Amount":<13}{"Category":<20}{"date":<12}")
    print("=" * 58)
    for expense in expenses:
        if expense["category"] == category[choice - 1]:
            print(
                f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<20}{expense["date"]:<12}"
            )
    time.sleep(0.5)


def search_by_amount(ch: str):
    amount = getValidAmount()
    print(f"{"Name":<15}{"Amount":<13}{"Category":<20}{"date":<12}")
    print("=" * 58)
    for expense in expenses:
        if ch == ">":
            if expense["amount"] >= amount:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<20}{expense["date"]:<12}"
                )
        else:
            if expense["amount"] <= amount:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<20}{expense["date"]:<12}"
                )
    time.sleep(0.5)


def search_by_date(ch: str):
    date = getValidDate()
    search_date = datetime.datetime.strptime(date, "%d-%m-%Y")
    print(f"{"Name":<15}{"Amount":<13}{"Category":<20}{"date":<12}")
    print("=" * 58)
    for expense in expenses:
        expense_time = datetime.datetime.strptime(expense["date"], "%d-%m-%Y")
        if ch == ">":
            if expense_time >= search_date:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<20}{expense["date"]:<12}"
                )
        else:
            if expense_time <= search_date:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<20}{expense["date"]:<12}"
                )
    time.sleep(0.5)

def delete_expense():
    view_all_expense()
    choice=getValidChoice(len(expenses)+1)
    expenses.pop(choice-1)
    store_data()

def show_total():
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    print(f"The total amount is {sum}")


def search():
    print("""1.Search expenses before a  specific date
2.Search expenses after a specific date
3.Search expenses below or equal the amount
4.Search expenses above or equal the amount""")
    choice = getValidChoice(5)
    match choice:
        case 1:
            search_by_date("<")
        case 2:
            search_by_date(">")
        case 3:
            search_by_amount("<")
        case 4:
            search_by_amount(">")


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
6.Delete Expense
7.Exit""")
        load_data()
        choice = getValidChoice(8)
        match choice:
            case 1:
                add_expense()
            case 2:
                view_all_expense()
            case 3:
                search()
            case 4:
                filter_by_category()
            case 5:
                show_total()
            case 6:
                delete_expense()
            case 7:
                pass


mainMenu()
