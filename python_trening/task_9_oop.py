class Button:

    type: str = "Кнопка"

    def __init__(self, text, link):
        self.text = text
        self.link = link



home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')


print(home.text)
print('Кнопка ' + home.text + ' Имеет ссылку ' + home.link)

print('/n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)




class ButtonTwo:



    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc


    def click(self):
        return "Клик по локатору - {}".format(self.loc)



home_two = ButtonTwo('Домой', '/home', 'button#home')


print(home_two.click())



class Input:



    def __init__(self, text, loc):
        self.text = text
        self.loc = loc




search = Input('text', 'input#search')


print(search.text ,search.loc)



class Button:



    def __init__(self, text, loc):
        self.text = text
        self.loc = loc




element1 = Button('button_text', 'button_element1')


class Title:



    def __init__(self, text, loc):
        self.text = text
        self.loc = loc



element2 = Title('title_text', 'title_element1')



class Link:



    def __init__(self, text, loc):
        self.text = text
        self.loc = loc



element3 = Link('link_text', 'link_element1')


print(search.text, search.loc, element1.text, element1.loc, element2.text, element2.loc, element3.text, element3.loc)