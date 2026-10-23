# empty_List = []
# also_empty = list()

# numbers = [1, 2, 3, 4, 5]
# names = ["nazar", "jcnx", "hckjwncxw"]
# mixed = [1, "Heloo" , 3.14, True]


# print(numbers(-1)
# print(names(-1))
# print(mixed(-1))


# numbers = [0,10, 20, 30, 40, 50]
# print ("Before append:", numbers)

# numbers. append (60)

# print ("After append: ", numbers)

# numbers. insert (4,4)
# print ("After insert at index 0:", numbers)

# numbers. extend ([70, 80, 901])
# print("After extend:", numbers)

# numbers. remove (4)
# print("After remove 2:",numbers)

# last = numbers.pop (0)
# print (last)
# print ("After pop:", numbers)


# numbers. reverse()
# print ("After reverse:", numbers)

# numbers. sort()
# print ("After sort:", numbers)

# print ("Length of numbers list:", len (numbers))

# count = numbers. count (10)
# print ("Count of 10 in numbers list:", count)

# по названию


# numbers = [1,2,3,4,5, 6,7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print (numbers [2:5])
# # Slicing from index 5 to 14
# print (numbers [:10])
# # Slicing from start to index 9
# print (numbers [10:])
# # Slicing from index 10 to end
# print (numbers [::2])
# # Slicing with step of 2
# print (numbers [::-1])
# # Reversing the list using slicing
# print (numbers [-5:-1]) # Slicing last 5 to last 2 elements
# copy = numbers[:] # Creating a shallow copy of the list
# print ("Copy of numbers list:", copy)

movies = ["anjell", "mrak", "dentismrbe", "bollas", "rarity"]
print(movies)

movies.append ("hannn")
print(movies)

movies.append ("546378gfdhsjn")
print(movies)


movies. insert (5,8)
print ("After insert at index 0:", movies)

count = movies. count ("anjell")
print(movies)

movies.insert(1, "Dune")
print(movies)

movies.remove("Dune")
print(movies)

print(len(movies))

movies.remove("anjell")  
print(movies)

print(len(movies))
print(movies)

movies.remove("bollas")
print(movies)

if "mrak" in movies:
    print("yes")

print(len(movies))
print(movies)

print(movies[-1])
print(movies)

movies.remove("hannn")
print(movies)

movies.append("SSSSr")
print(movies)


movies.remove("546378gfdhsjn")
print(movies)



movies.remove("dentismrbe")
print(movies)


movies.remove("rarity")
print(movies)

movies.remove("mrak")
print(movies)

movies. insert (5,8)
print ("After insert at index 0:", movies)

movies.insert(1, "Dune")
print(movies)

print(movies)
print(movies)


for movie in movies:
    print(movies)

movies.insert(3, "Dune")
print(movies)



friends = ["Amina", "Nazar", "Ali"]

print("У меня", len(friends), "друга")

friends.append("Sara")

for friend in friends:
    print("Мой друг:", friend)



color = (0, 128, 255)  # синий цвет
r, g, b, = color
print(f"Red: {r}, Green: {g}, Blue: {b}")




color = (3423, 6347,78)
r, g, b, = color
print(f"Red: {r}, Green: {g}, Blue: {b} ")


color = (47583902, 439, 6457389275489)
r, g, b, = color
print("fRed: {r}, Green: {g}, Blue:{b}")


# правильная версия
coordinates = (34.0522, -118.2437)

# Распаковка кортежа
lat, lon = coordinates

# f-строка
print(f"Latitude: {lat}, Longitude: {lon}")


coordinates = (422.09889, -456.8899)
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")


person = ("Donalds", 77, "Teacher")
mame, age, profecion = person
print(person)




person = ("Charlie", 40, "Teacher")
name, age, profecion = person
print("f.")



# fruits = ("apple", "banana", "watermalon")
# a, b, c = fruits
# print(fruits)


task = ("Formacy", "driver", "schoool")
helth, car, children = task
a, b, c = task
print(f"Mine center: {a}, {b}, {c}")

fruits = ("apple", "banana", "orange")
s, k, r = fruits
print(f"My apples: {s}, {k}, {r}")

# Способ 1: прямой перебор
for fruit in fruits:
    print(fruit)
    # Способ 2: с индексом
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
    # Способ 3: enumerate (ЛУЧШИЙ!)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # Способ 4: enumerate с начальной позиции
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")