from itertools import count


def the_biggest (num_1, num_2):
    return max (num_1, num_2)
print (the_biggest(1, 2))


def yes_no (number_1, number_2):
    if number_1 - number_2 == 135:
        print ('yes')
    else:
        print ('no')
yes_no (270, 135)


def month (month_number):
    if month_number == 1 or month_number == 2 or month_number == 12:
        print ('Зима')
    elif month_number in range (3, 6):
        print ('Весна')
    elif month_number in range(6, 9):
        print('Лето')
    elif month_number in range(9, 12):
        print('Осень')
    else:
        print ('Введите число от 1 до 12')
month(13)


def over_ten (number_1, number_2, number_3):
    if number_1 > 10 and number_2 > 10 and number_3 > 10:
        print ('yes')
    else:
        print ('no')
over_ten(10.5, 11, 12)


def positive_qty (list_numbers):
    return sum(1 for i in list_numbers if i > 0)
print(positive_qty([1, 2, -3, -4, 5]))


def days_qty (years:int, months:int):
    return years*12*29+months*29
print (days_qty(2, 5))