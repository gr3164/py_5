# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

mylist = [random.randint(1, 10) for i in range(0, 7)]
print(f'{mylist} -> {str(list(filter(lambda x: x > 5 ,mylist))).strip("[]")}')


# mylist = [random.randint(1, 10) for i in range(0, 7)]
# compare = lambda x: x > 5
# result = list(filter(compare, mylist))
# print(f'{mylist} -> {str(result).strip("[]")}')