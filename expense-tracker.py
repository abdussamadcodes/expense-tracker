import json
import datetime
import time

expenses = []


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
        print("===== Expense Tracker =====")
        print("""1.Add expense
2.View all expense
3.Search expenses
4.Filter by category
5.Show total spending
6.Export data
7.Exit
""")
        choice = getValidChoice(8)


mainMenu()
