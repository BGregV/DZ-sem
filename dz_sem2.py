# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# РЕШЕНИЕ: 
# a = input('Введите число ')
# def summa(a):                            
#     if float(a) < 0:                            
#         a = float(a) * (-1)
#     number = 0

#     for i in str(a):
#         if i != '.':
#             number += int(i)
#     return number
# print(f'Сумма чисел равна {summa(a)}')


# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# РЕШЕНИЕ: 

# n = int(input('Введите число: ')) 

# def get_squerence(n):
#     return [round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

# nums = get_squerence(n)
# print(nums)
# print(round(sum(nums), 2))

# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int

# РЕШЕНИЕ: 
# import random

# l = [1, 4, 5, 6, 3, 9, 45]
# # l = list(input('Введите числа для рандома: ')) 
# # print(l)
# print ('Исходный список: ' + str(l))
# for i in range(len(l)-1, 0, -1):      
#     j = random.randint(0, i + 1)     
#     l[i], l[j] = l[j], l[i]       
# print ('Перемешанный список: ' +  str(l))
