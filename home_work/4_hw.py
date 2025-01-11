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


text_box = Sidebar('Text Box')
print(text_box.text)
text_box.click()
check_box = Sidebar('Check Box')
print(check_box.text)
check_box.click()
radio_button = Sidebar('Radio Button')
print(radio_button.text)
radio_button.click()
web_tables = Sidebar('Web Tables')
print(web_tables.text)
web_tables.click()
buttons = Sidebar('Buttons')
print(buttons.text)
buttons.click()
links = Sidebar('Links')
print(links.text)
links.click()
broken_links_images = Sidebar('Broken Links images')
print(broken_links_images.text)
broken_links_images.click()
upload_and_download = Sidebar('Upload and Download')
print(upload_and_download.text)
upload_and_download.click()
dynamic_properties = Sidebar('Dynamic Properties')
print(dynamic_properties.text)
dynamic_properties.click()
