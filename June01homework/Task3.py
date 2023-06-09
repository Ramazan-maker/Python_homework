def get_number_combine(number1, number2, number3):
    combined_number = int(str(number1) + str(number2) + str(number3))
    return combined_number

number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")
number3 = input("Введите третье число: ")

try:
    number1 = int(number1)
    number2 = int(number2)
    number3 = int(number3)
except ValueError:
    print("Ошибка! Вы ввели некорректные данные!")
else:
    results = get_number_combine(number1, number2, number3)
    print(results)
