class File1():
    def __init__(self, name = "file243", size = 4, data = "16.11.2024", type = ".txt", road = "C:/"):
        self.name = name
        self.size = size
        self.data = data
        self.type = type
        self.road = road
    def info(self):
        print("=" * 30)
        print(f"Name - ({self.name})")
        print(f"Size - {self.size} kb")
        print(f"Data - -{self.data}-")
        print(f"Type - {self.type}")
        print(f"Road - {self.road}")
        print("=" * 30)
class File2():
    def __init__(self, name = "file222", size = 99, data = "16.9.2024", type = ".docx", road = "C:/"):
        self.name = name
        self.size = size
        self.data = data
        self.type = type
        self.road = road
    def info(self):
        print("=" * 30)
        print(f"Name - ({self.name})")
        print(f"Size - {self.size} kb")
        print(f"Data - -{self.data}-")
        print(f"Type - {self.type}")
        print(f"Road - {self.road}")
        print("=" * 30)
class File3():
    def __init__(self, name = "txt222", size = 35, data = "19.10.2024", type = ".txt", road = "C:/System/"):
        self.name = name
        self.size = size
        self.data = data
        self.type = type
        self.road = road
    def info(self):
        print("="*30)
        print(f"Name - ({self.name})")
        print(f"Size - {self.size} kb")
        print(f"Data - -{self.data}-")
        print(f"Type - {self.type}")
        print(f"Road - {self.road}")
        print("=" * 30)

f1 = File1()
f2 = File2()
f3 = File3()

print("Enter number of file: file1, file2, file3")
try:
    p = int(input("number = "))
    if p == 1:
        f1.info()
    if p == 2:
        f2.info()
    if p == 3:
        f3.info()
except:
    print("Error")
finally:
    print("Information")
print("Program is stopped")