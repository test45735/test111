print("------------------")
print("Enter value")
print("------------------")
int1 = int(input())
int2 = int(input())

print("------------------")
print("Enter which process: plus, minus, multi, division")
print("------------------")

pr = input()
if pr == "plus":
    print(int1 + int2)
if pr == "minus":
    print(int1 - int2)
if pr == "multi":
    print(int1 * int2)
if pr == "division":
    print(int1 / int2)

print("------------------")