# numbers = [1, 2, 3, 0.5, False, 10]
# # print(numbers[::-1])
# numbers.append(5)
# print(numbers)

# numbers.insert(3, 67)
# print(numbers)


# numbers.append(1)
# print(numbers)

# numbers.remove(3)
# print(numbers)

empty_dict = ()
empty = set()
# students = [
#      "Amina",
#       "Nazar",
#       "Ali"
# ]
numbers = {1, 2, 3, 4, 5}
fruits = {"яблоко", "банан", "апельсин"}
print(numbers)  
print(type(fruits))
print(fruits)

numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5}
print(numbers)

emails = ["user@mail.ru", "test@mail.ru", "user@mail.ru"]
unique_emails = set(emails)

print(unique_emails)
back_to_list = list(unique_emails)
print(unique_emails)


visitors = ["Иван", "Мария", "Пётр", "Иван", "Анна", "Мария"]
print(f"Всего посещений: {len(visitors)}")

unique_visitors = list(set(visitors))
print(f"Уникальных посетителей: {len(unique_visitors)}")
print(unique_visitors)

print('='*500)