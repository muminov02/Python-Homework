# Task 1

'''
import random

arr_1 = [int(random.random() * 20) for i in range(int(input("Введите количество чисел 1 набора: ")))]
arr_2 = [int(random.random() * 20) for i in range(int(input("Введите количество чисел 2 набора: ")))]
print("1 набор: ", arr_1)
print("2 набор: ", arr_2)
set_1 = set(arr_1)
set_2 = set(arr_2)
res = list()
for i in set_1:
    if i in set_2:
        res.append(i)
for i in set_2:
    if i in set_1:
        res.append(i)
res_set = set(res)
res_set = list(res_set)
for i in range(len(res_set)):
    if res_set[i] != res_set[len(res_set)-1]:
        if res_set[i]>res_set[i+1]:
            res_set[i], res_set[i+1] = res_set[i], res_set[i+1]
print(res_set)
'''

# Task 2

'''
n = int(input()) 
arr = list() 
for i in range(n): 
    x = int(input()) 
    arr.append(x) 
arr_count = list() 
for i in range(len(arr) - 1): 
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1]) 
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count)) 
'''
