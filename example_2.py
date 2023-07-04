a = int(input("Задайте минимум диапазона: "))
b = int(input("Задайте максимум диапазона: "))
s = []

from random import randint
list1 = [randint(-10, 10) for i in range(20)]
print(list1)

for i in range(len(list1)):
    if a <= list1[i] <= b:
        s.append(i)
print(*s)