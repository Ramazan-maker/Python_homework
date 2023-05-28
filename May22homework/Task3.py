number = input("Введите шестизначное число: ")

# Разделяем число на две половины
half_length = len(number) // 2
first_half = number[:half_length]
second_half = number[half_length:]

# Суммируем числа
sum_of_halves = int(first_half) + int(second_half)

# Выводим результат
print("Сумма двух чисел:", sum_of_halves)