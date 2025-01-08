class Page:




    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)



home = Page('https://dirgroup.ru/members/courses/course622733505846/4-zanatie-sintaksis-python-oop-572229295599')


print(home.url)
home.get()



