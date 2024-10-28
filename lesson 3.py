import random
class Student:

    def __init__(self, name):
        self.name = name
        self.mental = 100
        self.progress = 1
        self.energy = 100
        self.health = 100
        self.alive = True

    def study(self):
        self.progress += 1
        self.energy -= 5
        self.mental -= 1

    def sleep(self):
        if self.energy < 110:
            self.energy += 2
        if self.health < 110:
            self.health += 2

    def chill(self):
        if self.energy < 110:
            self.energy += 2
        if self.mental < 110:
            self.mental += 2

    def info(self):
        print(f"Now {self.name} have:")
        print(f"Mental - {self.mental}")
        print(f"Mind   - {self.progress}")
        print(f"Energy - {self.energy}")
        print(f"Health - {self.health}")

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
            self.energy -= 10
            self.health -= 10
        if self.energy < 0:
            self.mental -= 10
            self.health -= 10
        if self.progress > 150:
            print("Michail ia a GENUIS")
        if self.progress > 100:
            print("Michail ia a smart")
    def live(self, day):
        print(f"Day #{day} From - {self.name}")
        print("-"*30)
        rnd = random.randint(1, 3)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.sleep()
        elif rnd == 3:
            self.chill()
        self.info()
        self.is_alive()
        print()




hum = Student("Michail")
for d in range(1, 366):
    if hum.alive == False:
        break
    hum.live(d)