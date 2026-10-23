# def add (a,b):
#     result = a + b
#     return result

# sum1 = add(5,3)
# print(f"5 + 3 = {sum1}")


# sum2 = add(10, 20)
# print(f"10 + 20 = {sum2}")

# print(f"Сумма: {add(100, 200)}")

# print()

# def multiply(a,b):
#     return a*b

# result = multiply(7, 8)
# print(f"7 * 8 = {result}")

# print()

# def divide (a,b):
#     if b == 0:
#         return "Ошибка деление на ноль!"
    

# print(divide(10, 2))
# print(divide(10, 2))
# print()

# def get_min_max(numbers):
#     minimum = min(numbers)
#     maximum = max(numbers)
#     return minimum, maximum

# nums = [10, 3, 5, 2, 7]
# min_val, max_val = get_min_max(nums)
# print(f"Максимум: {min_val}")
# print(f"Минимум: {max_val}")






# # ---------------------------------------------------------------------------------

# username = ' Nurs'

# def greet_user(name):
#     username = name
#     return username


# print (greet_user ('Nurgigit'))
# print (username) 

# counter = 0

# def show_counter():
#     global counter
#     counter += 1
#     return counter

# print(show_counter())
# print(show_counter())

scope = 0

def add_point():
    global scope
    scope = scope + 1
    print(f"Счет: {scope}")

add_point()
add_point()
add_point()

def add_scope(current_scope, points):
    return current_scope + points


my_scope = 0
my_scope = add_scope(my_scope, 10)
print(f"Счёт: {my_scope}")

my_scope = add_scope(my_scope, 5)
print(f"Счёт: {my_scope}")