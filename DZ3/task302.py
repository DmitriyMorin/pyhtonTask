# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input())
list = [int(input()) for i in range(n)]
x = int(input())
count = 0
for i in list:
    if i < x:
        count += 1
print(count)

n = int(input())

# list1 = list()
# for i in range(n):
# list1.append(int(input()))

# list1 = [int(input()) for i in range(n)]
# k= int(input())
# m = abs(k - list1[0]) - abs - модуль от числа
# number = list1[0]
# for i in range(1, len(list1)):
#     if m > abs(k - list1[i]): 
#         m = abs(k - list1[i])
#         number = list1[i]
# print(number)