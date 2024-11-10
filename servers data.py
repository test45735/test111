class Block():
    def __init__(self, name = "Server"):
        self.name = name
        self.giga = 1000
        self.data = 896
        self.age = 1
    def info(self):
        print("="*30)
        print(f"Name - {self.name}")
        print(f"Giga - {self.giga}")
        print(f"Data - {self.data}")
        print(f"Age  - {self.age}")
        print("=" * 30)

b = Block()
class Server1(Block):
    b.info()
class Server2(Block):
    b.info()
class Server3(Block):
    b.info()

s1 = Server1()
s2 = Server2()
s3 = Server3()