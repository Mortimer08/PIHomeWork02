# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from decimal import Decimal 
number = Decimal(input('Введите вещественное число: '))
integerPart = int(number)
fractionalPart = number-integerPart

sum = 0
while integerPart!=0:
    sum += integerPart % 10
    integerPart //= 10
while fractionalPart!=0:
    fractionalPart *= 10
    sum += int(fractionalPart)
    fractionalPart -= int(fractionalPart)

print(f'В числе {number} сумма цифр равна {sum}')
