"""
Написать функцию, которая вычисляет сумму целых чисел от 0 до переданного ей числа.
"""



def calculate_integer_sum(num):
    total_sum = 0
    for i in range(num + 1):
        total_sum += i
    return total_sum

num = input("Введите целое положительное число: ")
try:
    num = int(num)
    if num < 0:
        raise ValueError("Ошибка: Введите положительное число.")
except ValueError:
    print("Ошибка! Вы ввели некорректные данные!")
else:
    total_sum = calculate_integer_sum(num)
    print("Сумма чисел от 0 до", total_sum)


# VN: вы не передаёте ничего в функцию


