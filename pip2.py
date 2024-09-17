# 1)написати функцію на замикання котра буде в собі зберігати список справ,
# вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


# 2) протипізувати перше завдання

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки
# (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
# продекорована цим декоратором, та буде виводити це значення після виконання функцій


dec_num = 0
def decor(func):
    def inner(*args,**kwargs):
        global dec_num
        dec_num += 1
        print('***************************************')
        result = func(*args,**kwargs)
        print('***************************************')
        return result
    return inner

@decor
def task_list():
    task_l = []

    def add_task(add_t):
        task_l.append(add_t)

    @decor
    def get_task():
        print(task_l)

    return add_task, get_task

add_task, get_task = task_list()

@decor
def menu_2():
    print('2')

@decor
def menu_3():
    print('3')

@decor
def menu_4():
    print(f'Decorator N: {dec_num}')

@decor
def menu():
    while True:
        print('Tz N 1)')
        print('Tz N 2)')
        print('Tz N 3)')
        print('Tz N 4)')
        print('Exit 9)')

        choice = input('choice - ')

        if choice == '1':
            while True:
                print('1) add___')
                print('2) print_')
                print('9) Exit__')
                menu_1_c = input('choice - ')
                if menu_1_c == '1':
                    new_task = input('new_task: ')
                    add_task(new_task)
                elif menu_1_c == '2':
                    get_task()
                elif menu_1_c == '9':
                    break
        elif choice == '2':
            menu_2()
        elif choice == '3':
            menu_3()
        elif choice == '4':
            menu_4()
        elif choice == '9':
            break

menu()
