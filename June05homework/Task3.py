def print_multiplication_table(n, m=1):
    if n > 9:  # базовый случай: если n превышает 9, завершаем выполнение функции
        return

    if m > 10:  # базовый случай: если m превышает 10, переходим к следующему числу n
        print()  # переходим на новую строку
        print_multiplication_table(n + 1)  # рекурсивный вызов функции с увеличенным значением n
    else:
        result = n * m
        print(f"{n} x {m} = {result}")  # выводим результат умножения
        print_multiplication_table(n, m + 1)  # рекурсивный вызов функции с увеличенным значением m

# Пример использования функции:
print_multiplication_table(2)


