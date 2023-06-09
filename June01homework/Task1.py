"""
Написать функцию, которая принимает 2 числа и возвращает -1,
 если первое меньше, чем второе; 1 – если первое больше, чем второе; и 0 – если числа равны.
"""



# VN: "функция, которая принимает 2 числа". В вашей функции 0 аргументов
def get_numbers():
    # по заданию, функция не должна ничего спрашивать у пользователя
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Ошибка! Вы ввели некорректные данные!")
    else:
        if num1<num2:
            return -1
        elif num1 >num2:
            return 1
        elif num1 == num2:
            return 0
        else:
            print("Вы ввели неверные данные")

    
# results = get_numbers()
# print(results)


def compare_numbers(num1, num2):
    if num1 < num2:
        return -1
    elif num1 > num2:
        return 1
    else:
        return 0


number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

result = compare_numbers(number1, number2)

print("Результат сравнения:", result)
