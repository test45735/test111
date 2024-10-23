class Data:
    print("oop")
    count = 0
    def __init__(self, name = "no found", giga = 100, age = 0):
        self.name = name
        self.giga = giga
        self.age = age
        Data.count += 1
    def addYear(self):
        if self.age < 20:
            self.age += 1


    def process(self):
        print("-Working-")
    def info(self):
        print(f"Name - {self.name}")
        print(f"Giga - {self.giga}")
        print(f"Age - {self.age}")
    def __str__(self):
        return f"Name - {self.name}\n" + f"Giga - {self.giga}\n" + f"Age - {self.age}"


print(Data.count)
print("------------")
data1 = Data("server", 991)
#print(data1.name)
#print(data1.giga)
data1.addYear()
data1.addYear()
data1.addYear()
data1.giga = 1080
#print(data1.giga)
#print(data1.age)
data1.info()
print(data1.count)
data1.process()
print("------------")
data2 = Data("server2", 554)
data2.info()
print(data1.count)
#print(data2.name)
#print(data2.giga)
print("------------")
data3 = Data()
print(data3)
print(data1.count)
#print(data3.name)
#print(data3.giga)
