# fruits = ("apple", "banana", "orange")
# s, k, r = fruits
# print(f"My apples: {s}, {k}, {r}")
# # Способ 1: прямой перебор
# for fruit in fruits:
#     print(fruit)
#     # Способ 2: с индексом
# for i in range(len(fruits)):
#     print(f"{i}: {fruits[i]}")
#     # Способ 3: enumerate (ЛУЧШИЙ!)
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")
#     # Способ 4: enumerate с начальной позиции
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")


#     fruits = ("apple", "egg", "sl")
#     d, v, n = fruits
#     print(f"my td: {d}, {v}, {n}")
# # 1
# for fruit in fruits:
#     print(fruit)
# # 2
#     for i in range(len(fruits)):
#         print(f"{i}: {fruits[i]}")
# # 3
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")
# # 4
# for index, fruit in enumerate(fruits, start=98765):
#     print(f"{index}. {fruit}")


# empty_dict = {}
# also_empty = dict()

# person = (object)

# person = {
#     "name": "Иван",
#     "age": 25,
#     "city": "Москва",
#     "is_student": True
# }
# print(person)

# print(person["name"])        
# print(person["age"])

# print(person.get("name"))   
# print(person.get("phone"))  
# print(person.get("phone", "Не указан"))

# # перезаписали его возраст !!!!!
# person["age"] = 26
# print(person["age"])

# person["email"] = "ivan2666вап@icloud.com"
# print(person)





# student = {
#     "name": "Alz",
#     "grade": 10,
#     "subjects": ["математика", "физика", "химия"],
#     "is_honor_student": True
# }

# keys = student.keys()
# values = student.values()
# items = student.items()

# print(keys)
# print(values)
# print(items)

# if "name" in student:
#     print("ключ 'name' есть ли в словаре")

#     if "phone" not in student:
#         print("Ключ 'phone' отсувствует с словаре!")

#         student.update({"grade":75, "email": "gmail.com"})
#         print(student)

person = {
    "name": "Saulla",
    "age": 16,
    "city": "Санкт-Петербург"
}
for key in person :
     print(key, person[key])

     for key in person.keys():
          print(key, person[key])

          for value in person.values():
               print(value)

               for key, value in person.items():
                    print(key, value)