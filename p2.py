# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random

mylist = [1, 5, 2, 3, 4, 6, 1, 7]
rand_number = random.randint(0, len(mylist)-1)
print(f'{mylist} -> {list(set(filter(lambda x: mylist[rand_number] <= x ,mylist[rand_number:])))}')


# mylist = [1, 5, 2, 3, 4, 6, 1, 7]
# mylist2 = []
# rand_number = random.randint(0, len(mylist)-1)

# for i in mylist[rand_number:]:
#     if mylist[rand_number] <= i:
#         mylist2.append(i)

# print(f'{mylist} -> {list(set(mylist2))}')
