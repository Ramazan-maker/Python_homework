number = input("Введите число: ")
shift = int(input("На сколько цифр сдвинуть число? "))

# Выполняем сдвиг цифр
shifted_number = number[shift:] + number[:shift]

print("Результат сдвига:", shifted_number)
