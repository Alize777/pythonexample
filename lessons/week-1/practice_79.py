# user_name = 'Alize'
# user_height = 1.65
# is_employed = True
# user_birth_year = 1993


# user_age = 2026 - user_birth_year
# print("Age:", user_age)

# Программа приветствия






# # ----------------------1
# print("Привет!")  
# name = input("Как тебя зовут? ")  
# age = input("Сколько тебе лет")
# print(f"Очень приятно познакомиться,", {name}, {age}, "!")



# # ----------------------2
# total = 0

# for i in range(1, 101):
#     total += i

# print("Сумма:", total)


# # ----------------------3
# number = int(input("Введите число: "))

# if number % 2 == 0:
#     print("Чётное число")
# else:
#     print("Нечётное число")




# # ----------------------4
# number = int(input("Введите число: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")




# # ----------------------5
# text = input("Введите строку: ")

# letters = 0
# digits = 0
# spaces = 0

# for char in text:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1
#     elif char == " ":
#         spaces += 1

# print("Буквы:", letters)
# print("Цифры:", digits)
# print("Пробелы:", spaces)



# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix [1][2])

# for row in matrix:
#     for num in row:
#         print(num, end=' ')

# table = [[i * j for j in range(1, 6)] for i in range(1, 6)]



# # Базовая распаковка
# a, b, c = [1, 2, 3]
# # a=1, b=2, c=3

# # С "остатком" (*)
# first, *middle, last = [1, 2, 3, 4, 5]
# # first=1, middle=[2, 3, 4], last=5

# # Игнорируем ненужное (_)
# first, _, third = [10, 20, 30]
# # first=10, third=30








# # 1. Создай список чисел от 1 до 10
# # Твой код:
# numbers = list(range(1, 11))
# print(numbers)

# # 2. Оставь только числа больше 5
# # Твой код:
# filtered = []

# for num in numbers:
#     if num > 5:
#         filtered.append(num)

# print(filtered)


# # 3. Возведи каждое число в квадрат
# # Твой код:
# squared = []

# for num in filtered:
#     squared.append(num ** 2)

# print(squared)

# # 4. Найди сумму всех чисел
# # Твой код:
# total = sum(squared)
# print(total)


# # total
# numbers = list(range(1, 11))

# filtered = [num for num in numbers if num > 5]

# squared = [num ** 2 for num in filtered]

# total = sum(squared)

# print(total)
# # ooo


shopping = ["apple", "banana", "watermalon", "pineapple", "strawberry"]
a, b, c, d, r = shopping
print(shopping)


shopping.append("raspberry") 
print(shopping)


shopping.insert(5, "pomelo")   
print(shopping)

shopping.pop(3)
print(shopping)

shopping.sort()
print(shopping)

shopping.reverse()
print(shopping)



pythonnumbers = [3, 7, 12, 5, 18, 9, 22, 4, 15]
evens = [...]
big_numbers = [...]
squares = [...]



# -----------------------------------------------------
# массив чисел
numbers = [1, 2, 5, 7, 8, 10, 787, 3]

# Сумма массива
total = sum(numbers)

# Ср ариф
average = total / len(numbers)

print(f"Сумма массива: {total}")
print(f"Среднее арифметическое: {average}")




array = [1,2,3,4,5,6,7,8,9]
total = sum(array)
print(f"Среднее арифметическое: {average}")

# Задача №334. Остаток
a = int(input("Введите a :"))
b = int(input("Введите b :"))
c = int(input("Введите c :"))
d = int(input("Введите d :"))
for i in range (a, b+1):
    if i % d ==c:
        print(i, end='')


