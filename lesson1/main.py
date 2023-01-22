# # task 1
# n = 20
# m = 21
# t = 22
# a = n + (m + 1) + t
# print(a // 2)

# 5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан
# его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет
# это делать или сообщать, что без дополнительной информации это сделать невозможно.

# i = int(input('i = '))
# j = int(input('j = '))
# if i == j:
#     print('Мало данных')
# else:
#     print(i + j - 1)

# task 7
# n = 2016
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('yes')
# else:
#     print('no')

# По данному целому неотрицательному n вычислите значение 
# n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int(input())
# i = 1
# res = 1
# while i <= n:
#     res *= i
#     i += 1 # i = i + 1
# print(res)

#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1
# 0 1 1 2 3 5 8 13 21
# 0 1 1 2 3 5 8 13 21

# n = int(input())
# n0 = 0
# n1 = 0 # 1 член последовательности
# n2 = 1 # 2 член последовательности
# i = 2

# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
# if n0 > n:
#     i = -1

# print(i)


# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те,
# в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько
# дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная
# температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам 
# в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих
# строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий
# день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# 20 30 -40 50 10 -10

# n = int(input())
# k = 0
# max = 0
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         k += 1
#     else:
#         max = k
#         k = 0
#     if max < k:
#         max = k
# print(max)

#Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 3000
# 5 -> 5 1 6 5 9
# n = int(input()) # количество арбузов
# max = -1
# min = 3001
# for i in range(n):
#     x = int(input())
#     if x > max:
#         max = x
#     if x < min:
#         min = x
# print('max=',max)
# print('min=',min)


# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list1)))

# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть
# всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# list1 = [1, 2, 3, 4, 5]
# list2 = []
# k = 2

# for i in range(k):
#     list2.append(list1[len(list1) - i - 1])
#     list2 = list2[::-1]

# for i in range(len(list1) - k):
#     list2.append(list1[i])

# print(list2)

# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# result_set = set()
# for i in list1:
#     for k, v in i.items():
#         result_set.add(v)
# print(result_set)

# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая
# подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# count = 0
# list1= [0, -1, 5, 2, 3]
# for i in range(len(list1)-1):
#     if list1[i]<list1[i+1]:
#         count = count+1
# print(count)