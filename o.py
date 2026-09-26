
class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def drive(self, length):
        rashid = length * 0.1

        if self.car.fuel - rashid > 0:
            print(f"Ми проїхали {length} км, і витратили {rashid} л пального")
            self.car.fuel -= rashid
            self.car.state -= length * 0.01
            return True
        else:
            print("Подорож не можлива. Не вистачає пального")
            return False

    def add_fuel(self):
        if self.car != None:
            self.car.fuel = 60
            self.money -= 20
            print("Ми заправили машину")

    def __str__(self):
        return f"Dima: {self.name}"

    def work(self):
        if self.job != None:
            self.money += self.job.salary
            print(f"{self.name} працює та отримує {self.job.salary} грн")
        else:
            print("У Dima немає роботи")

    def shopping(self):
        money = random.randint(1, 10)
        food = random.randint(1, 10)

        self.money -= money
        self.house.food += food

        if self.car == None:
            print("Пішли на шопінг пішки")
        else:
            if self.drive(random.randint(1, 10)):
                print("Поїхали на шопінг на авто")
            else:
                print("Пішли на шопінг пішки")

    def eat(self):
        if self.house.food > 0:
            self.house.food -= 1
            print("Dima поїв")
        else:
            print("Немає їжі")

    def chill(self):
        self.house.pollution += 1
        print("Dima відпочиває")

    def cleaning(self):
        if self.house.pollution > 0:
            self.house.pollution -= 1
            print("Dima прибрав будинок")
        else:
            print("Будинок вже чистий")

    def info(self):
        print("Ім'я:", self.name)
        print("Гроші:", self.money)
        print("Їжа:", self.house.food)
        print("Забруднення:", self.house.pollution)

        if self.car != None:
            print("Машина:", self.car.model)
            print("Пальне:", self.car.fuel)
            print("Стан машини:", self.car.state)

        if self.job != None:
            print("Робота:", self.job.name)
            print("Зарплата:", self.job.salary)

    def live(self, day):
        print(f"День {day}")
        self.work()
        self.shopping()
        self.eat()
        self.chill()
        self.cleaning()
        self.info()

    def is_alive(self):
        if self.money > 0 and self.house.food > 0:
            return True
        else:
            return False


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Робота: {self.name}, зарплата: {self.salary}"


class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"Їжа: {self.food}, забруднення: {self.pollution}"