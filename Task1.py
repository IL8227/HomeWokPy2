# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
a = input('Введите число ')
s = 0
for i in str(a):
   # if str(a) < 0:
   #     s += float(i)
  #  else:
    s += int(i)
print(s)



      
        