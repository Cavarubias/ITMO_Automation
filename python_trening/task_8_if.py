num = -1
if num >=0:
    print('Число больше либо равно 0')
else:
    print ('Число отрицательное')


def task_yes_no (str_1, str_2):
    if str_1 in str_2:
        print ('Да')
    else:
        print ('Нет')

task_yes_no (str_1 = 'test', str_2 = 'test1')


num_float = 0
if num_float > 0:
    print ('Положительное число')
elif num_float == 0:
    print ('Ноль')
else:
    print ('Число отрицательное')


num = -1
permit_print = False
if num > 0 and permit_print:
    print ('num - положительное число')
elif not permit_print:
    print ('Печать запрещена')


def student_rank (course):
    if course == 1 or course == 2 or course == 3 or course == 4:
        print ('Вы - бакалавр')
    elif course in range (5, 7):
        print('Вы - Магистр')
    elif 7 <= course <= 9:
        print('Вы - Аспирант')
    else:
        print ('Введите корректный год обучения')
student_rank(7)


def plus_minus (num_2):
    if num_2 > 100 or num_2 < -100:
        print ('-')
    else:
        print ('+')
plus_minus (101)
