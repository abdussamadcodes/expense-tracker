import json
import datetime
import time


def getValidChoice():
    choice = int()
    while True:
        try:
            choice = int(input("enter your choice: "))
        except:
            print("wrong choice. input should be string.")
        else:
            return choice


choice = getValidChoice()
