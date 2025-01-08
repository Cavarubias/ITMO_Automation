# class Soda:
#
#
#
#     def __init__(self, addition):
#         self.addition = addition
#
#
#     def show_my_drink(self):
#         if self.addition != '':
#             return 'Газировка и {}'.format(self.addition)
#         else:
#             return 'Обычная газировка'
#
#
#
# if_addition = Soda('клубника')
#
#
# print(if_addition.show_my_drink())




class Soda:



    def __init__(self, addition=None):
        self.addition = addition


    def show_my_drink(self):
        if self.addition:
            print (f'Газировка и {self.addition}')
        else:
            print ('Обычная газировка')



drink1 = Soda('клубника')
drink2 = Soda('')
drink1.show_my_drink()
drink2.show_my_drink()