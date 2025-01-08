#1 Rectangle

class Rectangle:



    def __init__(self, width, height):
        self.width = width
        self.height = height


    def find_area(self):
        print(self.height * self.width)


    def find_perimeter(self):
        print(2 * (self.height + self.width))




object1 = Rectangle(2, 3)
object2 = Rectangle(3, 4)
object3 = Rectangle(6, 5)
object1.find_area()
object1.find_perimeter()
object2.find_area()
object2.find_perimeter()
object3.find_area()
object3.find_perimeter()




#2 Math

class Math:



    def __init__(self, a, b):
        self.a = a
        self.b = b


    def addition(self):
        print(self.a + self.b)


    def multiplication(self):
        print(self.a * self.b)


    def division(self):
        print(self.a / self.b)


    def subtraction(self):
        print(self.a - self.b)



numbers = Math(50, 50)
numbers.addition()
numbers.multiplication()
numbers.division()
numbers.subtraction()




#3 SideBar (https://demoqa.com/text-box)

class Sidebar:

    type: str = "Кнопка"

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc


    def click(self):
        print(f'Клик по кнопке {self.text}')



Text_Box = Sidebar('Text Box')
print(Text_Box.text)
Text_Box.click()
Check_Box = Sidebar('Check Box')
print(Check_Box.text)
Check_Box.click()
Radio_Button = Sidebar('Radio Button')
print(Radio_Button.text)
Radio_Button.click()
Web_Tables = Sidebar('Web Tables')
print(Web_Tables.text)
Web_Tables.click()
Buttons = Sidebar('Buttons')
print(Buttons.text)
Buttons.click()
Links = Sidebar('Links')
print(Links.text)
Links.click()
Broken_Links_images = Sidebar('Broken Links images')
print(Broken_Links_images.text)
Broken_Links_images.click()
Upload_and_Download = Sidebar('Upload and Download')
print(Upload_and_Download.text)
Upload_and_Download.click()
Dynamic_Properties = Sidebar('Dynamic Properties')
print(Dynamic_Properties.text)
Dynamic_Properties.click()









