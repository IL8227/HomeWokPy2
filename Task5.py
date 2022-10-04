# Задание 5 Реализуйте алгоритм перемешивания списка.


import random


def mix_lst(lst_original):
    
    
    lst = lst_original[:]
    lst_length = len(lst)
    for i in range(lst_length):
        # Получение случайного индекса
        index = random.randint(0, lst_length - 1)
        # Замена
        temp = lst[i]
        lst[i] = lst[index]
        lst[index] = temp
    # Возвращаем список
    return lst
lst = [1, 2, 3, 4, 5, 6, 7]
mixed_lst = mix_lst(lst)
print(lst)
print(mixed_lst)


