# n1 = int(input("Ученики класса 1: "))
# n2 = int(input("Ученики класса 2: "))
# n3 = int(input("Ученики класса 3: "))

# sum =  (-n1//2) + (-n2//2) + (-n3//2)
# print(sum)

n1 = int(input("Введите год: "))

if(n1%4==0)and(n1%100!=0)or(n1%400==0):
    print("Yes")
else:
    print("No")