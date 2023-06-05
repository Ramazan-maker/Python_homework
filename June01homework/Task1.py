"""
Написать функцию, которая принимает 2 числа и возвращает -1,
 если первое меньше, чем второе; 1 – если первое больше, чем второе; и 0 – если числа равны.
"""

def get_numbers():
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
    
results = get_numbers()
print(results)