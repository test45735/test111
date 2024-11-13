# raise TypeError
# print("process")
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     c = a / b
#     print(c)
# except:
#     print("Error")
# finally:
#     print("Work")
# print("Stop")

def check(var):
    if type(var) != str:
        raise TypeError(f"var {type(var)}is not string")
    return var

try:
    a = "10"
    print(check(a))
except(TypeError) as ex:
    print(ex)