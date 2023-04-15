# Task 1
'''
num = int(input("Введите число: "))
flag = 0
while num>0:
    flag += num%10
    num //= 10
print(flag)
'''

# Task 2
'''
num = int(input("Введите общее количество журавликов: "))  
boys = num // 6
girl = boys*4
print(f"Петя сделал: {boys} журавликов, Катя сделала: {girl} журавликов, Сережа сделал: {boys} журавликов")
'''

# Task 3
'''
num = int(input("Введите 6 значный номер: "))
if num//100000 != 1:
    print("Введите 6 значное число")
else:
    half_1 = num%1000
    half_2 = num//1000
    flag_1 = 0
    flag_2 = 0
    while half_1>0:
        flag_1 += half_1%10
        half_1 //= 10
    while half_2>0:
        flag_2 += half_2%10
        half_2 //= 10
    if flag_1==flag_2:
        print("Yes")
    else:
        print("No")
'''

# Task 4
'''
n = int(input("Введите 1 число: "))
m = int(input("Введите 2 число: "))
k = int(input("Введите 3 число: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
'''
