p =  input ( 'Введите число:')
try:
    p = int(p)
except ValueError:
    message = "Ошибка! Введено некорректное значение"
else:
    b = p**2# идет вычисление,числа в квадрат
    template ="Результат %s квадрат числа"
    message = template % b
print(message)#вывод числа в квадрате