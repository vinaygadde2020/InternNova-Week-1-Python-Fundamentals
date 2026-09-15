def square(num):
    return num * num


def average(a, b, c):
    return (a + b + c) / 3


num = float(input("Enter a number to find square: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("Square:", square(num))
print("Average:", average(a, b, c))