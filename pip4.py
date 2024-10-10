# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли
#   з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
# =====================================================================
import json

try:
    with open('emails.txt') as source:
        with open('gmail.txt', 'w') as target:
            for line in source:
                email = line.split()[-1]
                if email.endswith('@gmail.com'):
                    print(email,file=target)
except Exception as e:
    print(e)
# =====================================================================
# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналом:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь-якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)
# =====================================================================
class Purchases:
    def __init__(self, file_name:str):
        self.__file_name = file_name
        self.__purchases_list = []
        self.__read_file()
        self.__id = self.__gen_id()

    def __show_all(self):
        for purchase in self.__purchases_list:
            print(f'{purchase["id"]} {purchase["name"]} {purchase["price"]}')

    def __add(self):
        name = input('Enter name: ')

        while True:
            try:
                price = float(input('Enter price: '))
                break
            except (Exception,):
                pass

        new_purchase = {'id':next(self.__id), 'name':name, 'price':price}
        self.__purchases_list.append(new_purchase)
        self.__write_file()

    def __find_by(self):
        value = input('Enter value: ')

        for purchase in self.__purchases_list:
            if value in [str(item) for item in purchase.values()]:
                print(purchase)

    def __most_expensive(self):
        print(max(self.__purchases_list, key=lambda x: x.get('price')))

    def __delete_by_id(self):
        self.show_all()

        while True:
            try:
                _id = int(input('Enter id: '))
                break
            except (Exception,):
                pass

        index = next((i for i, v in enumerate(self.__purchases_list) if v['id'] == _id), None)

        if index:
            del self.__purchases_list[index]
            self.__write_file()
            return
        print('Error')

    def __write_file(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__purchases_list, file)
        except Exception as e:
            print(e)

    def __read_file(self):
        try:
            with open(self.__file_name) as file:
                self.__purchases_list = json.load(file)
        except (Exception,):
            self.__write_file()

    def __gen_id(self):
        _id = self.__purchases_list[-1]['id']+1 if self.__purchases_list else 1
        while True:
            yield _id
            _id += 1

    def menu(self):
        while True:
            print('*' * 50, end='\n\n')
            print('1) Show all')
            print('2) Create')
            print('3) Find by')
            print('4) Most expensive')
            print('5) Delete by id')
            print('9) Exit')

            choice = input('Make a choice')
            print('*'*50, end='\n\n')
            match choice:
                case '1':
                    self.__show_all()
                case '2':
                    self.__add()
                case '3':
                    self.__find_by()
                case '4':
                    self.__most_expensive()
                case '5':
                    self.__delete_by_id()
                case '9':
                    return

purchases = Purchases('notebook.txt')
purchases.menu()
# =====================================================================
# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
# data = [
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1111, "field": {}},
#         {"id": 1112, "field": {}},
#         {"id": 1113, "field": {}},
#         {"id": 1114, "field": {}},
#         {"id": 1115, "field": {}},
#     ],
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1120, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1123, "field": {}},
#         {"id": 1124, "field": {}},
#         {"id": 1125, "field": {}},
#
#     ],
#     [
#         {"id": 1130, "field": {}},
#         {"id": 1131, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1132, "field": {}},
#         {"id": 1133, "field": {}},
#
#     ]
# ]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]