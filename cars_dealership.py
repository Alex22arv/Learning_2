import csv
from project_extension import buying_the_car, max_value_hp, min_value_consump
from pathlib import Path




cars_db_doc_path = Path(r"/Users/macbookpro/Desktop/doc.csv")
cars_data_base = open(cars_db_doc_path)
cars_data_base_reader = csv.reader(cars_data_base)
cars_data = list(cars_data_base_reader)
cars_data[0][0]='1'



def search_car(cars_data: list):
    while True:
        try:
            year= int(input("Which is the mininum year of manufacture that you prefer? "))
            break
        except ValueError:
            print("Wrong answer, please try again ")

    while True:
        try:
            budget = int(input("What's your budget? "))
            break
        except ValueError:
            print("Wrong answer, please try again ")

    while True:
            fuel = input("What fuel do you prefer? ")
            fuel = fuel.casefold()
            if fuel in ["petrol","diesel","hybrid"] :
                break
            else:
                print("Wrong answer, please try again ")

    while True:
        try:
            horsepower = int(input("What is the minimum horsepower you want? "))
            break
        except ValueError:
            print("Wrong answer, please try again ")

    list_of_cars=[]


    for row in cars_data:
           if year <= int(row[5]) and budget >= int(row[4]) and fuel == row[7] and horsepower <= int(row[8]):
            list_of_cars.append([row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]])
            print(f"Your budget includes the next car: --{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]}")


    if len(list_of_cars)==0:
           for row in cars_data:
                if year <= int(row[5]) and budget + 2000 >= int(row[4]) and fuel == row[7] and horsepower <= int(row[8]):
                    print(f"You don't have enough budget for a car but found these matches : --{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]}")
                    list_of_cars.append([row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]])

    if len(list_of_cars) == 0:
         print("Sorry, we don't have any cars for your requests")

    if len(list_of_cars)>0:

        list_of_maxHpValues=max_value_hp(list_of_cars)
        top_five_hp_cars=[]
        for car in list_of_cars:
            if int(car[8]) in list_of_maxHpValues:
                top_five_hp_cars.append([car[0],car[1], car[2], car[3], car[4], car[5], car[6], car[7], car[8], car[9], car[10]])

        min_cons=min_value_consump(top_five_hp_cars)

        for car in top_five_hp_cars:
            if float(car[9])==min_cons :
                print(f'Our top choice/choices : --{car[0]} {car[1]} {car[2]} {car[3]} {car[4]} {car[5]} {car[6]} {car[7]} {car[8]} {car[9]} {car[10]}')

        return list_of_cars





if __name__=='__main__':
    answer=input("Welcome to the Audi Dealership , are you interested to buying a car? ")
    if answer.casefold() == "yes" :
        list_of_sorted_cars=search_car(cars_data)
        if list_of_sorted_cars!= None:
            buying_the_car(cars_data, list_of_sorted_cars)

    elif answer.casefold() == "no" :
        print("Thank you for visiting us , see you again")
    else:
         while True :
             wrong_answer = input("Wrong answer, please try again ")
             if wrong_answer.casefold() == "yes" :
                list_of_sorted_cars=search_car(cars_data)
                if list_of_sorted_cars != None:
                    buying_the_car(cars_data, list_of_sorted_cars)
                break
             elif wrong_answer.casefold() == "no" :
                print("Thank you for visiting us , see you again")
                break