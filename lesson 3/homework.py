'''
# Task 1
num = int(input("Введите количество чисел: "))
arr = [1]
counter = 0
for i in range(num - 1):
    num = int(input(f"Введите {i + 2} число: "))
    arr.append(num)
find = int(input("Введите число которого хотите найти: "))
for i in arr:
    if find == i:
        counter += 1
print(counter)
'''

# Task 2
'''
num = int(input("Введите количество чисел: "))
arr = [1]
counter = arr[0]
res = arr[0]
for i in range(num - 1):
    num = int(input(f"Введите {i + 2} число: "))
    arr.append(num)
find = int(input("Введите число которого хотите найти: "))
if arr[0] > find:
    diff = arr[0]-find
else:
    diff = find - arr[0]
for i in range(len(arr)):
    if arr[i] > find:
        if (arr[i] - find) < diff:
            diff = arr[i] - find
            res = arr[i]
    elif arr[i] < find:
        if (find - arr[i]) < diff:
            diff = find - arr[i]
            res = arr[i]
    else:
        continue
print(res)
'''

