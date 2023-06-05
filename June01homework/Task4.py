"""
Написать функцию, которая принимает длину и ширину прямоугольника и вычисляет его площадь. 
Если в функцию передали 1 параметр, то она вычисляет площадь квадрата.
"""



def calculate_area():
    length = input("Введите длину прямоугольника: ")
    width = input("Введите ширину прямоугольника: ")
    area = 0  # Инициализируем переменную area

    try:
        length = int(length)
        width = int(width)
    except ValueError:
        print("Ошибка! Вы ввели неверные данные!")
    else:
        if width is None:
            area = length ** 2
        else:
            area = length * width
    return area

result = calculate_area()
# if result is not None:
#     print("Площадь прямоугольника:", result)
print(result)
#Виталий здраствуйте как здесь реализовать это задачу?