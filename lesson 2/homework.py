import random
import math
# Task 1
'''
a = 0
b = 0
num = int(input("Введите количество монеток: "))
for i in range(num):
    tmp = int(input(f"{i+1} - монетка: "))
    if tmp != 0 and tmp != 1:
        print("У монетки может быть только 0 или 1 состояния.")
        break
    if tmp == 0:
        a+=1
    else:
        b+=1
if a>b:
    print(f"Минимальное количество переворотов у состояния 1. Она ровна {b}.")
elif a<b:
    print(f"Минимальное количество переворотов у состояния 0. Она ровна {a}.")
else:
    print(f"Минимальное количество переворотов у обоих состояний ровна - {a}.")
'''

'''
# Task 2
num_x = random.randint(0, 1000)
num_y = random.randint(0, 1000)
S = num_x + num_y
P = num_x * num_y
a = 1
b = -S
c = P
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
if (x1 == num_x or x1 == num_y) and (x2 == num_x or x2 == num_y):
    print("The two numbers are", x1, "and", S - x1)
    print("The two numbers are", x2, "and", S - x2)
'''


'''
# Task 3
num = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
'''
