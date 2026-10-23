# number_one = float(input("Enter the first number"))
# number_two =  float(input("Enter the second number"))

# print("you entered:", number_one + number_two)

# number_one = float(input ("Enter the first number: "))

# number_two = float(input ("Enter the second number: "))




# print ("You entered:", number_one + number_two)

# print ("The sum of the two numbers is:", number_one + number_two)

# print ("The difference of the two numbers is:", number_one - number_two)

# print ("The product of the two numbers is:", number_one * number_two)

# #print ("The quotient of the two numbers is:", number_one / number_two)

# print ("The remainder of the two numbers is:", number_one % number_two)

# print ("The exponentiation of the two numbers is:", number_one ** number_two)

# print ("The floor division of the two numbers is:", number_one // number_two)





# print ("The minimum of the two numbers is:", min(number_one, number_two))

# nazars_age = 16

# if nazars_age > 18:
#     print("nazar buy energy drink")
# elif nazars_age == 18:
#     print("Nazar is allowed to buy energy drink with parental consent")
# else:
#     print("Nazar is not allowed to buy energy drink")

# for i in range(10):
#     print('Hello, World!',i)



# num = float(input("Enter a number:"))

# for i in range(1,11):
#  print(num, 'x',  i, '=', num * i)






# №1
# print("Конвертор температуры")
# print("1 — Цельсий в Фаренгейты")
# print("2 — Фаренгейты в Цельсий")

# choice = input("Выберите режим (1 или 2): ")

# if choice == "1":
#     celsius = float(input("Введите температуру в °C: "))
#     fahrenheit = (celsius * 9 / 5) + 32
#     print(f"{celsius} °C = {fahrenheit:.2f} °F")

# elif choice == "2":
#     fahrenheit = float(input("Введите температуру в °F: "))
#     celsius = (fahrenheit - 32) * 5 / 9
#     print(f"{fahrenheit} °F = {celsius:.2f} °C")

# else:
#     print("Ошибка: выберите 1 или 2")







# №2
# number = int(input("Введите целое число: "))

# if number % 2 == 0:
#     print("Число четное")
# else:
#     print("Число нечетное")


# домащняя работа 
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# # 2
# while True:
#     print("\nКалькулятор")
#     print("1 — Сложение")
#     print("2 — Вычитание")
#     print("3 — Умножение")
#     print("4 — Деление")
#     print("0 — Выход")

#     choice = input("Выберите операцию: ")

#     if choice == "0":
#         print("Выход из программы")
#         break

#     if choice in ("1", "2", "3", "4"):
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))

#         if choice == "1":
#             print("Результат:", a + b)

#         elif choice == "2":
#             print("Результат:", a - b)

#         elif choice == "3":
#             print("Результат:", a * b)

#         elif choice == "4":
#             if b == 0:
#                 print("Ошибка: деление на ноль")
#             else:
#                 print("Результат:", a / b)
#     else:
#         print("Неверный выбор. Попробуйте снова.")



# #3
# height = int(input("Введите высоту пирамиды: "))

# for i in range(height):
#     print("*" * (2 * i + 1))


# #4
# n = int(input("Введите число N: "))

# print("Простые числа до", n)

# for number in range(2, n + 1):
#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(number)



# #%5
# n = int(input("Введите число: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print(f"{n}! = {factorial}")
