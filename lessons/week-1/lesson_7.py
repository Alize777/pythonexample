class human:
    age: "12"


class student (human):
    grade: "11"
    age: "19"
    group: "11_25"

# class theacher: 
#     experience: "7"
    


# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age

#     def bark(self):   # ← внутри класса (с отступом!)
#         print(f"{self.name} говорит гав гав!")

#     def info(self):   # ← внутри класса
#         print(f"Имя: {self.name}, порода: {self.breed}, возраст: {self.age} лет")


# dog1 = Dog("Бобик", "Хаски", 3)
# dog2 = Dog("Рекс", "Немецкая овчарка", 5)

# dog1.bark()
# dog2.info()

# print(dog1.name)

# dog1.age = 4
# print(dog1.age)


# class Person:
#     def __init__(self, name, age, city="Almaty"):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.friends = []

#     def add_friend(self, friend_name):
#         self.friends.append(friend_name)

#     def introduce(self):
#         print(f"Привет! Я {self.name}, мне {self.age} лет, из {self.city}.")
#         if self.friends:
#             print(f"Мои друзья: {', '.join(self.friends)}")

# # Создаем объекты
# amir = Person("Амир", 20)          
# dana = Person("Дана", 19, "Астана") 


# amir.add_friend("Дана")


# amir.introduce()





# __________________________________________Блок 1 задание 1
# class Human:
#     def __init__(self, name, age, city="Paris", grade="10", portfoliourl="UI/UX"):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.grade = grade
#         self.portfoliourl = portfoliourl
#         self.friends = []

#     def add_friend(self, friend_name):  
#         self.friends.append(friend_name)

#     def introduce(self):
#         print(f"Привет! Я {self.name}, мне {self.age} лет, из {self.city}, работаю в {self.portfoliourl} класс {self.grade}.")
#         if self.friends:
#             print(f"Мои друзья: {', '.join(self.friends)}")

# alice = Human("Алина", 19, "Bishkek")
# bob = Human("мрп", 16, "London")

# alice.add_friend("Алиш")
# alice.introduce()
    

# ______________________________2 задание



# _____________________________________ 

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Привет! Я {self.name}, мне {self.age} лет."


class Programmer(Human):
    def __init__(self, name, age, language, experience):
        super().__init__(name, age)
        self.language = language
        self.experience = experience

    def introduce(self):
        text = super().introduce()
        return f"{text} Я программист и пишу на {self.language}. Опыт: {self.experience}."


class SeniorProgrammer(Programmer):
    def __init__(self, name, age, language, experience, team_size):

        if experience < 3:
            raise ValueError("Для Senior нужно мин 3-года опыта")

        super().__init__(name, age, language, experience)
        self.team_size = team_size

    def mentor(self, junior_name):
        return f"{self.name}код-ревью для {junior_name} "

    def introduce(self):
        text = super().introduce()
        return f"{text} Я Senior программист и president команды из {self.team_size} человек."


# обжек
alize = Human("Ализе", 18)
karim = Programmer("Карим", 20, "Python", "7 месяцев")
nafisa = SeniorProgrammer("Нафиса", 27, "Java", 5, 4)


print(alize.introduce())
print(karim.introduce())
print(nafisa.introduce())
print(nafisa.mentor("Карим"))


# ___________________________________________
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Привет! Я {self.name}, мне {self.age} лет."

    def get_info(self):
        return {
            "name": self.name,
            "age": self.age
        }


class Programmer(Human):
    def __init__(self, name, age, language, experience):
        super().__init__(name, age)
        self.language = language
        self.experience = experience

    def introduce(self):
        return f"{super().introduce()} Я программист, пишу на {self.language}."

    def get_info(self):
        info = super().get_info()
        info["language"] = self.language
        info["experience"] = self.experience
        return info


class Designer(Human):
    def __init__(self, name, age, specialty, portfolio_url):
        super().__init__(name, age)
        self.specialty = specialty
        self.portfolio_url = portfolio_url

    def create_design(self, project):
        return f"{self.name} создаёт дизайн для {project} "

    def introduce(self):
        return f"{super().introduce()} Я дизайнер: {self.specialty}."


class SeniorProgrammer(Programmer):
    def __init__(self, name, age, language, experience, team_size):
        if experience < 3:
            raise ValueError("Для Senior минимум 3 года experience")
        super().__init__(name, age, language, experience)
        self.team_size = team_size

    def mentor(self, junior_name):
        return f"{self.name} код-ревью для {junior_name} "

    def introduce(self):
        return f"{super().introduce()} Я Senior программист и руковожу командой из {self.team_size} человек."


# Функц полиморфизма
def print_all_introductions(people):
    for person in people:
        print(person.introduce())


#  объекты
human = Human("Нафиса", 20)

programmer1 = Programmer("Карим", 22, "Python", 2)
programmer2 = Programmer("Ализе", 23, "Java", 7)

designer = Designer("Алина", 25, "UI/UX", "alina.design")

senior = SeniorProgrammer("Дмитрий", 28, "Python", 5, 4)


# Проверка 
print(designer.create_design("мобильного приложения"))
print(programmer2.get_info())
print(senior.mentor("Илья"))

print("\nВсе представления:")
people = [human, programmer1, programmer2, designer, senior]
print_all_introductions(people)


# Фильтрация п
programmers = [p for p in people if isinstance(p, Programmer)]

print("\nПрограммисты:")
for p in programmers:
    print(p.name)

# high experience
most_experienced = max(programmers, key=lambda p: p.experience)
print(f"\nСамый опытный программист: {most_experienced.name} ({most_experienced.experience} лет опыта)")

# edcrejj-------------------------------------------------------
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Привет! Я {self.name}, мне {self.age} лет."


class Employee(Human):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age)
        self.salary = salary
        self.department = department

    def work(self):
        print(f"{self.name} работает в отделе {self.department}")


class Programmer(Employee):
    def __init__(self, name, age, salary, department, language, experience):
        super().__init__(name, age, salary, department)
        self.language = language
        self.experience = experience

    def work(self):
        print(f"{self.name} пишет код на {self.language}")

    def code(self):
        print(f"{self.name} программирует на {self.language}")

# ---------- Магичес методы ----------
    def __str__(self):
        return f"Programmer: {self.name}, {self.language}, {self.experience} лет опыта"

    def __repr__(self):
        return f"Programmer('{self.name}', {self.age}, {self.salary}, '{self.department}', '{self.language}', {self.experience})"

    def __eq__(self, other):
        return self.language == other.language and self.experience == other.experience

    def __lt__(self, other):
        return self.experience < other.experience

    def __add__(self, other):
        new_exp = self.experience + other.experience
        return Programmer(
            self.name + "-" + other.name,
            self.age,
            self.salary,
            self.department,
            self.language,
            new_exp
        )


class Designer(Employee):
    def __init__(self, name, age, salary, department, tools):
        super().__init__(name, age, salary, department)
        self.tools = tools

    def work(self):
        print(f"{self.name} создаёт дизайн")

    def design(self):
        print(f"{self.name} работает в программах: {', '.join(self.tools)}")


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary, department)
        self.team = []

    def add_member(self, employee):
        self.team.append(employee)

    def show_team(self):
        print("Команда:")
        for member in self.team:
            print(member.introduce())

    def get_salary_fund(self):
        total = 0
        for member in self.team:
            total += member.salary
        return total
    



p1 = Programmer("Анна", 25, 2000, "IT", "Python", 3)
p2 = Programmer("Иван", 30, 2500, "IT", "Python", 5)

team = [p2, p1]

team.sort()   # сортировка через __lt__

print(team)

print(p1 + p2)


class Company:
    def __init__(self):
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        print(employee.name, "принят на работу")

    def fire(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                print(name, "уволен")
                return

    def promote(self, programmer):
        if programmer.experience < 3:
            raise ValueError("Недостаточно опыта для Senior")

        senior = Programmer(
            programmer.name,
            programmer.age,
            programmer.salary + 1000,
            programmer.department,
            programmer.language,
            programmer.experience
        )

        print(programmer.name, "повышен до Senior")
        return senior

    def monthly_report(self):
        print("\n Отчет компании")

        total_salary = 0
        best_dev = None

        for emp in self.employees:
            print(emp.introduce())
            total_salary += emp.salary

            if isinstance(emp, Programmer):
                if best_dev is None or emp.experience > best_dev.experience:
                    best_dev = emp

        print("\nФонд зарплат:", total_salary)

        if best_dev:
            print("Лучший разработчик:", best_dev.name, "-", best_dev.experience, "лет опыта")





class Person:
    def __init__(self, name, age, balance):
        self.name = name
        self._age = age
        self.__balance = balance


        # getter
        def get_age(self):
            return self._age
        
        # setter
        def set_age(self, age):
            self._age=age
            return self._age
        
        # getter
        @property
        def balance(self):
            return self.__balance
        

        # setter
        @balance.setter 
        def balance(self,balance):
            self.__balance += balance
            return self.__balance        
