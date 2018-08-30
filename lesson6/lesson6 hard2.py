# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Craft:

    def __init__(self):
        self.name = ''
        self.color = ''
        self.data()
        self._purchase_of_materials()
        self._sewing()
        self._painting()

    def _purchase_of_materials(self):
        print('Закупаем материалы')

    def _sewing(self):
        print('Шьем')

    def _painting(self):
        print('Окрашиваем')

    def data(self):
        self.type = ''
        while self.type != 'животное' and self.type != 'персонаж мультфильма':
            self.type = input('Введите тип игрушки: животное или персонаж мультфильма')
        if self.type == 'животное':
            self = Animal()
        else:
            self = Cartoon()


class Animal(Craft):

    def __init__(self):
        self.name_color()
        self.back()


    def name_color(self):
        self.name = input('Введите название игрушки:')
        self.color = input('Введите цвет игрушки:')

    def back(self):
        return self

class Cartoon(Craft):

    def __init__(self):
        self.name_color()
        self.back()

    def name_color(self):
        self.name = input('Введите название игрушки:')
        self.color = input('Введите цвет игрушки:')

    def back(self):
        return self

answer = ''
while True:
    answer = input('Хотите создать игрушку? да/нет')
    if answer == 'да':
        toy = Craft()
        print('Игрушка успешно создана!')
    elif answer == 'нет':
        break
    else:
        print('некорректное значение')





