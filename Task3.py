# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# Пример:

# Для n = 6 -> 14.072

n = int(input('Введите число: '))
lst = [] 
s = 0
for i in range(1,n + 1):
    lst += [(1 + 1/i)**i]
print(lst)    
for a in list(lst):
        s += a          
print(round(s,3))    
        
              

# print(sum(sequence(n)))
# n = int(input('Введите число: '))
# lst = []