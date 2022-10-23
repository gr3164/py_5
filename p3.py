# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

from collections import Counter

mylist = [1, 4, 2, 3, 4, 6, 1, 7]

def Count_duplicate(x):
    coll = Counter(x)
    count = 0
    for i in coll:
        if coll[i] > 1:
            count += coll[i]
    return count

def Disordered_set(x):
    newlist = []
    for el in x:
        if el not in newlist:
            newlist.append(el)   
    return newlist

print(f'{mylist} -> {Count_duplicate(mylist)}\n{Disordered_set(mylist)}')

