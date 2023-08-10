class Widget():
    #властивості класа (в конструкторі)
    def __init__(self, text, x, y):
        self.text=text
        self.x=x
        self.y=y
            #методи

    def print_info(self):
        print("Напис:", self.text)
        print("Розташування", self.x, self.y)

class Button(Widget):
    def __init__(self, text, x, y, is_clicked):
        super().__init__(text, x, y,)
        self.is_clicked = is_clicked
    #доповнені властивості класа (в конструкторі)

    #нові методи
    def click(self):
        self.is_clicked = True

#створи екземпляр класа Button
a = Button("Брати Участь", 100, 100, False)
a.print_info()
#якщо на питання «Хочете зареєструватися?» користувач відповів «так», то застосуйте метод click
i = input("зареєстрований?")
i = i.lower()
if i == 'так':
    a.click()
else:
    print('сумно')