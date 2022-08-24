
import csv
from pprint import pprint

from pathlib import Path

cars_data_base = open("/Users/macbookpro/Desktop/doc.csv")
cars_data_base_reader = csv.reader(cars_data_base)
cars_data = list(cars_data_base_reader)
# for i in cars_data:
#     print(i)
def search_car(cars_data: list):
    year= int(input("Whitch is the mininum year of manufacture that you prefer? "))
    budget = int(input("What's your budget? "))
    fuel = input("What fuel do you prefer? ")
    horsepower = int(input("What is the minimum horsepower you want? "))
    list_of_cars=[]
    for row in cars_data:
        if year <= int(row[5]) and budget >= int(row[4]) and fuel == row[7] and horsepower <= int(row[8]):
            list_of_cars.append([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]])
            print(f"Your budget includes the next car: {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]}")

    if len(list_of_cars)==0:
           for row in cars_data:
                if year <= int(row[5]) and budget + 2000 >= int(row[4]) and fuel == row[7] and horsepower <= int(row[8]):
                    print(f"You don't have enough budget for a car but found these matches : {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]}")
                    list_of_cars.append([row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]])

    if len(list_of_cars) == 0:
         print("Sorry, we don't have any cars for your requests")



answer=input("Welcome,Do you want to buy a car? ")
if answer.casefold() == "yes" :
    search_car(cars_data)

elif answer.casefold() == "no" :
    print("thank you for visiting us , see you again")
else:
     while True :
         wrong_answer = input("wrong answer, please try again")
         if wrong_answer.casefold() == "yes" :
            search_car(cars_data)
            break
         elif wrong_answer.casefold() == "no" :
            print("thank you for visiting us , see you again")
            break












