from pyexpat import native_encoding

class Human:
    def __init__(self, name, job = None):
        self.name = name
        self.car_e = False # false = no car, true = have a car
        self.job = job
        self.wallet = 9999999999 # $
        self.health = 100 # %
        self.alive = True
    def work(self):
        self.wallet += job.cash
        self.health -= 2
    def sleep(self):
        if self.health < 100:
            self.health += 3
    def shopping(self):
        if self.health < 100:
            self.health += 5
        self.wallet -= 10 # $
        house.food += 5
        if self.wallet > 1000:
            self.car_e = True
            car.take = True
            self.wallet -= 1000
    def eat(self):
        if house.food > 0:
            house.food -= 1
        if self.health < 100:
            self.health += 3
        house.trash += 3
    def chill(self):
        if self.health < 100:
            self.health += 1
        self.wallet -= 3
    def info(self):
        print("- Human -")
        print(f"Wallet - {self.wallet}")
        print(f"Health - {self.health}")
        print("- House -")
        print(f"Food - {house.food}")
        print(f"Trash - {house.trash}")
        if self.car_e == True:
            print("-  Car  -")
            print(f"Fuel - {car.fuel}")
            print(f"State - {car.state}")

    def live(self):
        print("Enter any 3 actions: /work, /sleep, /shopping, /eat, /chill, /clean")
        if self.car_e == True:
            print("/drive, /fix, /oil")
        x1 = input()
        if x1  == "/work":
            self.work()
        elif x1  == "/sleep":
            self.sleep()
        elif x1  == "/shopping":
            self.shopping()
        elif x1  == "/eat":
            self.eat()
        elif x1  == "/sleep":
            self.sleep()
        elif x1  == "/chill":
            self.chill()
        elif x1  == "/clean":
            house.clean()
        if self.car_e == True:
            if x1  == "/drive":
                car.drive()
            if x1  == "/fix":
                car.fix()
            if x1 == "/oil":
                car.pay_oil()
            car.crash()
        if self.health > 100:
            self.health = 100
        if self.alive == True:
            print("-" * 30)
            self.info()
            print("-" * 30)
        if self.alive == False:
            print("Over of life")
class House:
    def __init__(self, have):
        self.have = have
        self.food = 0
        self.trash = 0
    def clean(self):
        if  self.trash > 0:
            self.trash -= 10
            human.health -= 1
        if self.trash < 0:
            self.trash = 0


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60 # L
        self.state = 100 # %
        self.take = False
    def drive(self):
        if self.take == True and self.fuel > 0:
           self.fuel -= 5
           self.state -= 5
    def crash(self):
        if self.state < 0 and self.take == True:
            human.car_e = False
            self.take = False
    def fix(self):
        if self.take == True:
            human.wallet -= 15
            human.health -= 3
            self.state += 15
    def pay_oil(self):
        if self.take == True:
            human.wallet -= 20
            self.fuel += 20
            if self.fuel > 60:
                self.fuel = 60



class Job:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

car = Car("BMW")
job = Job("Programmer", 50)
human = Human("Ivan", job = Job)
house = House("have")

while True:
    human.live()