import csv

def max_value_hp(list_of_cars):
    list_of_max_value_horsepower = []
    for row in list_of_cars:
        list_of_max_value_horsepower.append(int(row[8]))
    list_of_max_value_horsepower.sort()
    list_of_max_value_horsepower.reverse()
    list_of_max_value_hp = list_of_max_value_horsepower[0:5]
    return list_of_max_value_hp




def min_value_consump(list_of_cars):
    list_of_min_value_consumption = []
    for row in list_of_cars:
        list_of_min_value_consumption.append(float(row[9]))
    list_of_min_value_consumption.sort()
    min_value_consump=list_of_min_value_consumption[0]
    return min_value_consump

def buying_the_car(cars_data,sorted_list):
    list_of_id = []
    for car in sorted_list:
        list_of_id.append(int(car[0]))

    while True:
        try:
            answer_interestBuying = input("Are you interested in any of these cars? ")
            if answer_interestBuying.casefold() == "yes":
                car_id = int(input("Which is the id of the car you want? "))
                if car_id in list_of_id:
                    print("You bought the car . This car is no longer available in our stock ")
                    for car in cars_data:
                        if int(car[0]) == car_id:
                            cars_data.remove(car)
                    with open("/Users/macbookpro/Desktop/Book3.csv", 'w') as f:
                        write = csv.writer(f)
                        write.writerows(cars_data)
                    break
                else:
                    print("We haven't found any cars with this id ")
                    break
            elif answer_interestBuying.casefold() == "no":
                print("Thank you for visiting us , see you again")
                break
            print('Wrong answer, please try again')

        except ValueError:
            print('Wrong answer, please try again')

