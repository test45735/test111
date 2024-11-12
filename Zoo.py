class Zoo():
    def __init__(self, name):
        self.__name = name
    def info(self):
        print("Class -", self.__name)

class Flying(Zoo):
    def __init__(self, name, size):
        self.__size = size
        super().__init__(name)
    def info(self):
        print("Flying")
        super().info()
        print("Size -", self.__size)

class Walking(Zoo):
    def __init__(self, name, size):
        self.__size = size
        super().__init__(name)
    def info(self):
        print("Walking")
        super().info()
        print("Size -", self.__size)
class Swimming(Zoo):
    def __init__(self, name, size):
        self.__size = size
        super().__init__(name)

    def info(self):
        print("Swimming")
        super().info()
        print("Size -", self.__size)




#zoo = Zoo("Animals")
#zoo.info()
f = Flying(name = "Birds", size = 3)
f.info()
s = Swimming(name = "Fish", size = 1)
s.info()
w = Walking(name = "Mammals", size = 8)
w.info()
