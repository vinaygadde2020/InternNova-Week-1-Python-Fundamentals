# 1. Print numbers from 1 to 20
for i in range(1, 21):
    print(i)


# 2. Multiplication table
num = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 3. Print even numbers from 1 to 50
i = 2

while i <= 50:
    print(i)
    i += 2