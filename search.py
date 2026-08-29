import datetime 
import time
import get_valid as get

def search_by_amount(ch: str,expenses:list):
    amount = get.getValidAmount()
    print(f"{"Name":<15}{"Amount":<13}{"Category":<25}{"date":<12}")
    print("=" * 63)
    for expense in expenses:
        if ch == ">":
            if expense["amount"] >= amount:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<25}{expense["date"]:<12}"
                )
        else:
            if expense["amount"] <= amount:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<25}{expense["date"]:<12}"
                )
    time.sleep(0.5)


def search_by_date(ch: str,expenses:list):
    date = get.getValidDate()
    search_date = datetime.datetime.strptime(date, "%d-%m-%Y")
    print(f"{"Name":<15}{"Amount":<13}{"Category":<25}{"date":<12}")
    print("=" * 63)
    for expense in expenses:
        expense_time = datetime.datetime.strptime(expense["date"], "%d-%m-%Y")
        if ch == ">":
            if expense_time >= search_date:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<25}{expense["date"]:<12}"
                )
        else:
            if expense_time <= search_date:
                print(
                    f"{expense["name"]:<15}{expense["amount"]:<13.2f}{expense["category"]:<25}{expense["date"]:<12}"
                )
    time.sleep(0.5)
