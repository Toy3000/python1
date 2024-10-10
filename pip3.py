# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
# /////////////////////////////////////////////////////////////////////////////////////
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім('я, вік, та розмір знайденого черевичка, а також '
#                      'метод котрий буде приймати список попелюшок, та шукати ту саму)
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів
#   классу
# також має бути метод классу який буде виводити це значення
# /////////////////////////////////////////////////////////////////////////////////////
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який
#   наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити
#       перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати
#       додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print
#       абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print
#       абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance,
# приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
# /////////////////////////////////////////////////////////////////////////////////////

from abc import ABC, abstractmethod
from typing import Self
class Rectangle:
    def __init__(self, x,y):
        self.x = x
        self.y = y

        self.area = self.x * self.y
    def __add__(self, other:Self):
        return self.area + other.area
    def __sub__(self, other:Self):
        return self.area - other.area
    def __eq__(self, other:Self):
        return self.area == other.area
    def __ne__(self, other:Self):
        return self.area != other.area
    def __lt__(self, other:Self):
        return self.area < other.area
    def __gt__(self, other:Self):
        return self.area > other.area
    def __len__(self, other:Self):
        return (self.x + self.y)*2


# a = Rectangle(2, 4)
# b = Rectangle(3, 8)
# print(a.__add__(b))
# print(a.__gt__(b))
# print(a.__eq__(b))
# print(a.__len__(b))
# print(a.__sub__(b))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0
    def __init__(self, name, age, size_foot):
        super().__init__(name, age)
        self.size_foot = size_foot
        Cinderella.__count +=1
    @classmethod
    def get_count(cls):
        print(cls.__count)
    def __str__(self):
        return str(self.__dict__)


class Prince(Human):
    def __init__(self, name, age, size_shoe):
        super().__init__(name, age)
        self.size_shoe = size_shoe
    def find(self, cinderella_list:list[Cinderella]):
        for cinderella in cinderella_list:
            if cinderella.size_foot == self.size_shoe:
                print(cinderella)
                return

    def __str__(self):
        return str(self.__dict__)


prince_1:list[Prince] = [
    # Prince('Romeo', 14, 32),
    # Prince('Anton', 34, 34),
    # Prince('Victor', 34, 36),
    Prince('Den', 34, 33)
]
cinderella_1:list[Cinderella] = [
    Cinderella('Anna', 29, 36),
    Cinderella('Antonina', 23, 32),
    Cinderella('Maria', 31, 33),
    Cinderella('Katya', 36, 34)
]
# Cinderella.get_count()

class Printable (ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(f'This is book {self.name}')

class Magazine(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(f'This is magazine {self.name}')

class Main:
    __printable_list:list[Printable] = []
    @classmethod
    def add(cls, item:Book|Magazine):
        if isinstance(item, (Book, Magazine)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazine(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()
    @classmethod
    def show_all_book(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

Main.add(Magazine('magazine1'))
Main.add(Magazine('magazine2'))
Main.add(Magazine('magazine3'))
Main.add(Magazine('magazine4'))
Main.add(Book('book1'))
Main.add(Book('book2'))
Main.add(Book('book3'))
Main.add(Book('book4'))

Main.show_all_book()
print('===================================')
Main.show_all_magazine()