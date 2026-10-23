contacts = {}

print("=" * 40)
print("Телефонный справочник")
print("=" * 40)

while True:
    print("\n--- МЕНЮ ---")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Найти контакт")
    print("4. Удалить контакт")
    print("5. Изменить контакт")
    print("6. Статистика")
    print("7. Выход")
    print("8. Введите переадрессацию")

    choice = input("Выберите действие: ")

    # 1. Показать все контакты
    if choice == '1':
        if contacts:
            print("\nСписок контактов:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("\nСправочник пуст.")

    # 2. Добавить контакт
    elif choice == '2':
        name = input("Введите имя контакта: ").strip()

        if name == "":
            print("Имя не может быть пустым.")
            continue

        if name in contacts:
            print("Контакт с таким именем уже существует.")
        else:
            phone = input("Введите номер телефона: ")
            contacts[name] = phone
            print(f"Контакт {name} добавлен.")
    # 3. Найти контакт
    elif choice == '3':
        name = input("Введите имя контакта для поиска: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Контакт не найден.")

    # 4. Удалить контакт
    elif choice == '4':
        name = input("Введите имя контакта для удаления: ")
        if name in contacts:
            del contacts[name]
            print(f"Контакт {name} удалён.")
        else:
            print("Контакт не найден.")

    # 5. Изменить контакт
    elif choice == '5':
        name = input("Введите имя контакта для изменения: ")
        if name in contacts:
            new_phone = input("Введите новый номер телефона: ")
            contacts[name] = new_phone
            print(f"Контакт {name} обновлён.")
        else:
            print("Контакт не найден.")

    # 6. Статистика
    elif choice == '6':
        print(f"Всего контактов: {len(contacts)}")

    # 7. Выход
    elif choice == '7':
        print("Выход из программы. Пока 👋")
        break
    
    else:
        print("Неверный выбор. Выберите пункт из меню.")

2




# ----------------------------------------------------------------------
# импорт всего модуля
import math
print(math.sqrt(16))

# импорт конкретной функции
from math import sqrt
print(sqrt(16))

# импорт нескольких функции
from math import sqrt, pi, pow
print(pi)

# импорт всего (не рекомендуется)
from math import *
print(sqrt(25))

# импорт с переименованием 
import math as m
print(m.sqrt(9))


from math import sqrt as square_root
print(square_root(16))



# # -----------------------------------------------------------------------------------------
# import random

# print (random. randint (1, 10))

# print (random. random ())

# print (random.uniform(1.5, 5.5))

# fruits = ["яблоко", "банан", "киви"]
# print( random. choice(fruits))

# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print (numbers)

# print (random. sample(fruits, 2))


import os

# Текущая рабочая директория
print(os.getcwd())



import os

# Найти все . txt файлы в текущей папке
for filename in os. listdir('.'):
    if filename.endswith(' txt'):
        print(f"Найден текстовый файл: {filename}")
        size = os.path.getsize(filename)
        print(f" Размер: {size} байт")


# -------------------------------------------------------------------
import sys
# Версия Python
print(sys.version)
# 3.11.5 (main, Sep 11 2023, ...)
# Аргументы командной строки
# Если запустить: python script.py arg1 arg2
print(sys.argv) # ['script.py', "arg1', "arg2']
# Платформа
print(sys.platform) # 'win32', 'linux', 'darwin' (Mac)
# Путь поиска модулей
print(sys.path) # Список директорий где Python ищет модули
# Выход из программы
# sys.exit() # Завершить программу
# sys. exit("Ошибка!") # Завершить с сообщением