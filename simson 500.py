from pyexpat import native_encoding

class Human:
    def __init__(self, name, car = None, job = None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.wallet = 50 # $
        self.health = 100 # %
    def work(self):
        pass
    def sleep(self):
        pass
    def eat(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def info(self):
        pass
    def live(self):
        pass
    def is_live(self):
        if self.wallet < 0 or self.health < 0:
            return False
        else:
            return True



class House:
    def __init__(self):
        self.food = 0
        self.trash = 0
    def clean(self):
        pass
    def fridge(self):
        pass

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60 # L
        self.state = 100 # %
    def drive(self):
        pass
    def crash(self):
        pass


class Job:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
    def taking(self):
        pass
#car = Car("BMW")
job = Job("Programmer", 1000)
human = Human("Ivan", job = Job)