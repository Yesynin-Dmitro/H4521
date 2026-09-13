import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 10
        self.energy = 50
        self.money = 100
        self.alive = True



    def study(self):
        print("я пішов до академії IT STEP")
        self.energy -= 5
        self.progress += 1
        self.gladness -= 1
        self.money -= 30

    def chill(self):
        print("Я пішов з друзяками гулять")
        self.gladness += 2
        self.energy -= 3
        self.progress -= 1
        self.money -= 40


    def sleep(self):
        print("Я пішов спати")
        self.energy += 6
        self.gladness += 1

    def eat(self):
        print("Я смачно поїв")
        self.energy += 3
        self.gladness += 1
        self.progress -= 0.2
        self.money -= 30
    def work(self):
        print("Я пішов на роботу")
        self.energy -= 5
        self.gladness -= 2
        self.money += 120
    def is_alive(self):
        if self.progress <= 0:
            print("В мене в голові одне сміття, життя не має сенсу")
            self.alive = False
        if self.gladness <= 0:
            print("В мене дипресія")
            self.alive = False
        if self.progress > 100:
            print("Я став академіком!")
        if self.energy <= 0:
            print("Я зовсім знесилений :(")
            self.alive = False
        if self.money <= 0:
            print("Я банкрут")
            self.alive = False



    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)
        rnd = random.randint(1,4)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.chill()
        elif rnd == 3:
            self.sleep()
        elif rnd == 4:
            self.work()
        else:
            self.eat()

        self.info()
        self.is_alive()
        print()

    def info(self):
        print(f"На сьогодні {self.name} має:")
        print(f"Задоволення {self.gladness}")
        print(f"Знання {self.gladness}")
        print(f"Енергія {self.energy}")
        print(f"Грощі {self.money}")




student = Student("Dima")
for d in range(365):
    if student.alive == False:
        break
    student.live(d)