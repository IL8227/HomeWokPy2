# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.


n = int(input('Введите число: '))
a = int(input('Введите число: '))
b = int(input('Введите число: '))
lst = list(range(-n,n))
composition = lst[a] * lst[b]
print(lst)
print(composition)