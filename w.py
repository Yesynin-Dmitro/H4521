class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "їсть")

    def sleep(self):
        print(self.name, "спить")


class Mammals(Animal):
    def __init__(self, name, age, fur):
        super().__init__(name, age)
        self.fur = fur

    def walk(self):
        print(self.name, "ходить")


class Cat(Mammals):
    def __init__(self, name, age, fur, breed):
        super().__init__(name, age, fur)
        self.breed = breed

    def meow(self):
        print(self.name, "мяукає")

    def walk(self):
        print(self.name, "гуляє")


class Dog(Mammals):
    def __init__(self, name, age, fur, breed):
        super().__init__(name, age, fur)
        self.breed = breed

    def bark(self):
        print(self.name, "гавкає")


class Fish(Animal):
    def __init__(self, name, age, water):
        super().__init__(name, age)
        self.water = water

    def swim(self):
        print(self.name, "плаває")


class GoldFish(Fish):
    def __init__(self, name, age, water, size):
        super().__init__(name, age, water)
        self.size = size

    def eat(self):
        print(self.name, "їсть корм")


cat = Cat("егор", 3, "м'яке", "персидський")
dog = Dog("бобік", 5, "коротке", "вівчарка")
fish = GoldFish("олег", 1, "прісна", "маленька")

cat.meow()
cat.walk()

dog.sleep()
dog.bark()

fish.swim()
fish.eat()