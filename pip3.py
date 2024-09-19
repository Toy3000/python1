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

class Human:
    # __slots__ = ('name', 'age', 'size')
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
class Prince(Human):
    # __slots__ = ('name', 'age', 'size')
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    def __str__(self):
        return str(self.__dict__)
class Cinderella(Human):
    # __slots__ = ('name', 'age', 'size')
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size
    def __str__(self):
        return str(self.__dict__)

prince_1 = Prince('Victor', 34, 36)
cinderella_1 = Cinderella('Anna', 29, 36)

print(prince_1)
print(cinderella_1)