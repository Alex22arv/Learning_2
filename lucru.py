
import csv
from pprint import pprint

from pathlib import Path

cars_data_base = open("/Users/macbookpro/Desktop/doc.csv")
cars_data_base_reader = csv.reader(cars_data_base)
cars_data = list(cars_data_base_reader)
# for i in cars_data:
#     print(i)
def search_car(cars_data: list):
    answer1 = int(input("Whitch is the mininum year of manufacture that you prefer? "))
    answer2 = int(input("What's your budget?"))
    answer3 = input("What fuel do you prefer?")
    answer4 = int(input("What is the minimum horsepower you want?"))
    for row in cars_data:
        if answer1 <= int(row[5]) and answer2 >= int(row[4]) and answer3 == row[7] and answer4 <= int(row[8]):
            print(f"Your budget includes the next car: {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]}")
        elif answer1 <= int(row[5]) and answer3 == row[7] and answer4 <= int(row[8]):
                print(f"You don't have enough budget for a car but found these matches{row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]}")

answer=input("Welcome,Do you want to buy a car?")
if answer.casefold() == "yes" :
    search_car(cars_data)

elif answer.casefold() == "no" :
    print("thank you for visiting us , see you again")
else:
     while True :
         answer5 = input("wrong answer, please try again")
         if answer5 == "yes" or answer5 == "YES" or answer5 == "Yes":
            search_car(cars_data)
            break
         elif answer5 == "no" or answer5 == "NO" or answer5 == "No":
            print("thank you for visiting us , see you again")
            break











