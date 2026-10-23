from abc import ABC, abstractmethod



# # def say_hello ():


# #     print('Привет Мир!')
# #     print('How are you')

# # say_hello ()
# # say_hello ()
# # say_hello ()
# # print()

# # def greet(name):
# #     print(f"Hello {name}")
# #     print(f"Ты кто")

# # greet('Опоздавший Али')
# # greet('Дами')

# # def introduce(name, age, city, food, dream):
# #     print(f"My name is {name}")
# #     print(f"i'm {age}")
# #     print(f"i live in {city}")
# #     print(f"my fav food {food}")
# #     print(f"my dream is {dream}")

# # introduce('Alize', 16, 'Makkah', 'fricase', 'dyson')
# # introduce('Ali', 21, 'Medina', 'pasta', 'Alize')

# # def add(a, b):
# #     return a + b
# # result = add(5, 10)
# # print(result)  # 

# # def add(a, b):
# #     return a / b
# # result = add(50, 10)
# # sum
# # print(result)  # 

# # def add(a,b):
# #     result + a + b
# #     return result
# # sum1 = add(10,20)
# # print(f"10+20")
# # print(f"10+20={sum1}")





# # sum2 = add (10, 20)
# # print(f"10 + 20 = {sum2}")
# # print (f"Сумма: {add (100, 200) }")
# # print ()






# # def multiply(a, b):
# #    return a * b

# # result = multiply(7, 8)
# # print (f"7 ½ 8 = {result}")

# # (print)
# # def divide(a, b) :
# #     if b == 0:
# #         return a / b
# #         return "Ошибка: деление на ноль!"
# # print (divide(10, 2))
# # print (divide (10,0))
# # print ()



# # array = [10, 20, 30, 40, 50]

# # def show_array_info(arr):
# #     print("Массив:", arr)
# #     print("Минимум:", min(arr))
# #     print("Максимум:", max(arr))

# # show_array_info(array)



# # def get_min_max(arr):
# #     return min(arr), max(arr)

# # mn, mx = get_min_max(array)
# # print("Минимум:", mn)
# # print("Максимум:", mx)





# class BankAccount:
#     def __init__(self, owner: str, balance: float = 0):
#         self.owner = owner          # публичный атрибут
#         self._currency = "USD"      # защищённый атрибут
#         self.__balance = balance    # приватный атрибут

#     @property
#     def balance(self):
#         return self.__balance

#     def deposit(self, amount: float):
#         if amount <= 0:
#             raise ValueError("Сумма должна быть положительной")
#         self.__balance += amount
#         print(f"Пополнено: +{amount} {self._currency}. Баланс: {self.__balance}")

#     def withdraw(self, amount: float):
#         if amount <= 0:
#             raise ValueError("Сумма должна быть положительной")
#         if amount > self.__balance:
#             raise ValueError("Недостаточно средств")
#         self.__balance -= amount
#         print(f"Снято: -{amount} {self._currency}. Баланс: {self.__balance}")

#     def __str__(self):
#         return f"Счёт {self.owner}: {self.__balance} {self._currency}"




# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance   # приватный атрибут

#     # метод пополнения
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Пополнено: +{amount} USD. Баланс: {self.__balance}")

#     # метод снятия
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Недостаточно средств!")
#         else:
#             self.__balance -= amount
#             print(f"Снято: -{amount} USD. Баланс: {self.__balance}")

#     # property для безопасного доступа к балансу
#     @property
#     def balance(self):
#         return self.__balance

#     # красивый вывод объекта
#     def __str__(self):
#         return f"Счёт [{self.owner}]: {self.__balance} USD"


# # Использование
# account = BankAccount("Алексей", 1000)

# account.deposit(500)
# account.withdraw(200)

# print(account.balance)   # через property
# print(account)           # через __str__

# # Попытка прямого доступа к приватному атрибуту
# try:
#     print(account._balance)
# except AttributeError as e:
#     print(f"Ошибка: {e}")











# # ---------------------------------------------------------------------------------------------------------
# from abc import ABC, abstractmethod

# # Абстрактный класс Animal
# class Animal(ABC):
#     @abstractmethod
#     def speak(self) -> str:
#         pass

#     @abstractmethod
#     def move(self) -> str:
#         pass


# # Класс Dog
# class Dog(Animal):
#     def speak(self) -> str:
#         return "Гав!"

#     def move(self) -> str:
#         return "Бежит на четырёх лапах"


# # Класс Bird
# class Bird(Animal):
#     def speak(self) -> str:
#         return "Чирик!"

#     def move(self) -> str:
#         return "Летит, махая крыльями"


# # Класс Fish
# class Fish(Animal):
#     def speak(self) -> str:
#         return "..."

#     def move(self) -> str:
#         return "Плывёт, виляя хвостом"


# # Создаём список животных
# animals: list[Animal] = [Dog(), Bird(), Fish()]

# # Выводим информацию о каждом животном
# for animal in animals:
#     print(f"{animal.__class__.__name__}: {animal.speak()} | {animal.move()}")



class Vehicle:
    def speak(self):
        pass

class Car(Vehicle):
    def speak(self):
        return "wmmmm"
    
    def move(self):
        return "Машина едет"
    
class Bicycle (Vehicle):
    def speak(self):
        return "tyntyn"
    
    def move(self):
        return "Велосипед крутит педалями"
    
class Airplane(Vehicle):
    def speak(self):
        return "viyuuuu"
    
    def move(self):
        return "Самолет летит"
    
Vehicle: list = [Car(), Bicycle(), Airplane()]

for Vehicle in Vehicle:

    print(Vehicle.speak())

    print(Vehicle.move())




import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius **2 * math.pi

class Rectangle:
    def __init__(self, widht, height):
        self.width = widht
        self.height = height
    def area(self):
        return self.height * self.width
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side **2 
    
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)

print(circle.area())
print(rectangle.area())
print(square.area())






# _________________________________________________________
class CashPayment:
    def pay(self, amount):
        print(f"аличными {amount} com. Спасибо!")

class CardPayment:
    def pay(self, amount):
        print(f"та картой списано {amount} рубюя успешна.")

class OnlinePayment:
    def pay(self, amount):
        print(f"Онлайн-оплата  {amount} lkjn. ектронный кошелёк.")


cash = CashPayment()
card = CardPayment()
online = OnlinePayment()

payment_methods = [cash, card, online]
amount_to_pay = 1500

for method in payment_methods:
    method.pay(amount_to_pay)





# ________________________________________________
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price


class Electronics(Product):
    def calculate_price(self):
        return self.price * 1.05
class Clothig(Product):
    def calculate_price(self):
        return self


laptop = Electronics("Laptop", 1000)

print(laptop.name)
print(laptop.calculate_price())

    




#     def balance(self):
#         return self.__balance

#     class Rectangle:
#     def __init__(self, widht, height):
#         self.__widht = widht
#         self.__height = height

#     @property
#     def widht(self):
#         return self.__widht
    
#     @widht.setter
#     def widht(self, value):
#         self.__widht = value
#         return self.__widht
#     @property
#     def height(self):
#         return self.__height
#     @height.setter
#     def height(self, value):
#         if value > 0:
#             self.__height = value
#         else:
#             raise ValueError("Height must be greater than 0")

#     @property
#     def area(self):
#         return self.__width * self.__height


# rectangle = Rectangle(5, 3)

# print(rectangle.width)
# print(rectangle.height)
# print(rectangle.area)

# rectangle.width = 10

# print(rectangle.area)





# Задача 15. Система сотрудников
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, name, position, hours, stavka):
        super().__init__(name, position)
        self.hours = hours
        self.stavka = stavka

    def calculate_salary(self):
        return self.hours * self.stavka


class Freelancer(Employee):
    def __init__(self, name, position, project, moneyforoneproject):
        super().__init__(name, position)
        self.project = project
        self.moneyforoneproject = moneyforoneproject

    def calculate_salary(self):
        return self.moneyforoneproject * self.project


employees = [
    FullTimeEmployee("bekk", "chef", 546487),
    PartTimeEmployee("hanzada", "manager", 54, 49387),
    Freelancer("marem", "assistant", 85, 7594397)
]


total = 0

for e in employees:
    salary = e.calculate_salary()
    print(e.name, "-", e.position, "-", salary)
    total += salary

print("Общая зарплата:", total)



# Система оплаты__________________________________

from abc import ABC, abstractmethod
# abstrac method
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):
    def pay(self, amount):
        if amount <= 0:
            print("Payment cancelled")
            return None #return None  сообщаем что оплаты не произошло.
        else:
            return amount



class CardPayment(Payment):
    def pay(self, amount):
        if amount <= 0:
            print("Payment cancelled")
            return None   
        else:
            return amount + amount * 0.02
    

class WalletPayment(Payment):
    def pay(self, amount):
        if amount <=0:
            print("Payment cancelled")
            return None
        else:
            return amount + amount * 0.01
        
def make_payment(payment, amount):
    return payment.pay(amount)


cash = CashPayment()
card = CardPayment()
wallet = WalletPayment()


print(make_payment(cash, 107880))
print(make_payment(card, 108980))
print(make_payment(wallet, 897100))







# _______________________________________________________ ex 18
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side


circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)

print("Circle area:", circle.calculate_area())
print("Circle perimeter:", circle.calculate_perimeter())

print("Rectangle area:", rectangle.calculate_area())
print("Rectangle perimeter:", rectangle.calculate_perimeter())

print("Square area:", square.calculate_area())
print("Square perimeter:", square.calculate_perimeter())


c = circle.calculate_area()
r = rectangle.calculate_area()
s = square.calculate_area()

if c > r and c > s:
    print("Circle has the biggest area")
elif r > s:
    print("Rectangle has the biggest area")
else:
    print("Square has the biggest area")