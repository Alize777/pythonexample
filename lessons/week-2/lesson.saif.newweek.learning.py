
# задача.  №1

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def get_password(self):
        return self.__password

    def change_password(self, new_password):
        self.__password = new_password


user1 = User("Ali", "12345")

print(user1.get_password())

user1.change_password("67890")

print(user1.get_password())


# №2


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price


product1 = Product("Laptop", 50000)

print(product1.get_price())



# №3

class Student:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 16 <= age <= 100:
            self.__age = age
        else:
            print("Errorеь age must be from 16 to 100")


student1 = Student(18)

print(student1.get_age())

student1.set_age(20)
print(student1.get_age())

student1.set_age(10)

# _________________________________#
class Rectangle:
    def __init__(self, widht, height):
        self.__widht = widht
        self.__height = height

    @property
    def widht(self):
        return self.__widht
    
    @widht.setter
    def widht(self, value):
        self.__widht = value
        return self.__widht
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            raise ValueError("Height must be greater than 0")

    @property
    def area(self):
        return self.__width * self.__height


rectangle = Rectangle(5, 3)

print(rectangle.width)
print(rectangle.height)
print(rectangle.area)

rectangle.width = 10

print(rectangle.area)






# ______________________________________________
for i in range(86):
    print("севен")


total = 2450
total = total-(200*3)

print(total)

