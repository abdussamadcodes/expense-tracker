import datetime
import time

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

