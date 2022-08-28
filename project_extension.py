

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