def get_number_combine():
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    num3 = input("Введите третье число: ")
    try:
        number1 = int(num1) 
        number2 = int(num2) 
        number3 = int(num3) 
    except ValueError:
        print("Ошибка! Вы ввели некорректные данные!")
    else:
        combined_number = int(str(number1) + str(number2) + str(number3))
    return combined_number

results = get_number_combine()
print(results)