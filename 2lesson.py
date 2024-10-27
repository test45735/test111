class Data:
    print("Dogs")
    count = 0
    def __init__(self, name = "dog", size = 10, age = 0, color = "white", species = "dog"):
        self.name = name
        self.size = size
        self.age = age
        self.color = color
        self.species = species
        Data.count += 1
    def addYear(self):
        if self.age < 20:
            self.age += 1
    def info(self):
        print(f"Name - {self.name}")
        print(f"Size - {self.size}")
        print(f"Age - {self.age}")
        print(f"Color - {self.color}")
        print(f"Species - {self.species}")
    def __str__(self):
        return f"Name - {self.name}\n" + f"Size - {self.size}\n" + f"Age - {self.age}\n" + f"Color - {self.color}\n" + f"Species - {self.species}"


print("------------")
dog1 = Data("Dog1", 20, age = 1, color = "brown", species = "Bulldog")
dog1.addYear()
dog1.addYear()
dog1.addYear()
dog1.info()
print("Count -", dog1.count)
print("------------")
dog2 = Data("Dog2", 30, age = 5, color = "black", species = "Shepherd")
dog2.addYear()
dog2.info()
print("Count -", dog2.count)
print("------------")
dog3 = Data()
dog3.info()
print("Count -", dog3.count)
print("------------")