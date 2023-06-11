user_input_number1 = input("Введите первое число: ")
user_input_number2 = input("Введите второе число: ")
try:
    number1 = abs(int(user_input_number1))
    number2 = abs(int(user_input_number2))
except ValueError:
    print("Ошибка! Вы ввели некорректные данные")
else:
    while number1!=number2:
        if number1>number2:
            number1=number1-number2
        else:
            number2= number2-number1
gcd = number1
print(gcd)
