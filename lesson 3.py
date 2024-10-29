import random
class Student:

    def __init__(self, name):
        self.name = name
        self.mental = 100
        self.progress = 1
        self.energy = 100
        self.health = 100
        self.cash = 10
        self.fullness = 100
        self.aqua = 100
        self.alive = True

    def study(self):
        self.progress += 1.5
        self.energy -= 5
        self.mental -= 1.5
        self.fullness -= 5.5
        self.aqua -= 5

    def sleep(self):
        if self.energy < 110:
            self.energy += 10
        if self.health < 110:
            self.health += 5

    def chill(self):
        if self.energy < 110:
            self.energy += 2.5
        if self.mental < 110:
            self.mental += 2.5
    def job(self):
        self.energy -= 5
        self.fullness -= 10
        self.aqua -= 10
        self.mental -= 1
        self.cash += 30.5
        self.health -= 5
    def shopping(self):
        if self.fullness < 200:
            self.fullness += 30.5
        if self.aqua < 200:
            self.aqua += 30.5
        self.energy += 10
        self.cash -= 20
        if self.mental < 110:
            self.mental += 5
        self.health += 3.5

    def info(self):
        print(f"Now {self.name} have:")
        print(f"Mental - {self.mental}")
        print(f"Mind   - {self.progress}")
        print(f"Energy - {self.energy}")
        print(f"Health - {self.health}")
        print(f"Cash - {self.cash}")
        print(f"Fullness - {self.fullness}")
        print(f"Aqua - {self.aqua}")

    def is_alive(self):
        if self.progress < 0:
            self.study()
        if self.progress < -50:
            print("Brain of Michail is a brick")
            self.alive = False
        if self.health < 0:
            print("Michail is died")
            self.alive = False
        if self.mental < 0:
            print("Michail in the depression")
            self.energy -= 5
            self.health -= 10
        if self.energy < 0:
            self.mental -= 10
            self.health -= 10
        if self.progress > 110:
            print("Michail ia a GENUIS")
        if self.progress > 100:
            print("Michail ia a smart")
        if self.fullness < 0:
            print("Michail is died of hunger")
            self.alive = False
        if self.aqua < 0:
            print("Michail is died of dehydration")
            self.alive = False
    def live(self, day):
        print(f"Day #{day} From - {self.name}")
        print("-"*30)
        rnd = random.randint(1, 5)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.sleep()
        elif rnd == 3:
            self.chill()
        elif rnd == 4:
            self.job()
        elif rnd == 5:
            self.shopping()
        self.info()
        self.is_alive()
        print()




hum = Student("Michail")
for d in range(1, 366):
    if hum.alive == False:
        break
    hum.live(d)