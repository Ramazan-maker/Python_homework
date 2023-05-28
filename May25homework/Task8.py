number = input ( 'Введите трехзначное число:')#запрос у пользователя трехзначного числа
try:
    number = int(number)
except:
    message = "Ошибка! Вы ввели неверные данные"
else:
    second_number= number % 100#деление на остаток
    sum = second_number // 10#деление на остаток \
    message = "Ваше трехзначное число %s и результат вывода второго числа %s" %(number,sum)

print(message)#вывод второго числа