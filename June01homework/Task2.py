"""
Написать функцию, которая вычисляет сумму целых чисел от 0 до переданного ей числа.
"""

# def get_int_sum():
#     num = input("Введите какое нибудь число: ")
#     try:
#         num = int(num)
#         # if num <= 100:
#         #     return num
#         # else:
#         #     print("Ошибка: Введите число, не превышающее 100.")
#     except ValueError:
#         print("Ошибка! Вы ввели некорректные данные!")
#     else:
#         calculate_get_int_sum = (num * (num + 1)) // 2
#     return calculate_get_int_sum
# total_sum = get_int_sum()

# print("Сумма чисел от 0 до",total_sum)
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


