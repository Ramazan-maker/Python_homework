"""
Написать функцию, которая принимает длину и ширину прямоугольника и вычисляет его площадь. 
Если в функцию передали 1 параметр, то она вычисляет площадь квадрата.
"""

def calculate_area(length, width=None):
    if width is None:
        area = length ** 2
    else:
        area = length * width
    return area

length = input("Введите длину прямоугольника: ")
width = input("Введите ширину прямоугольника (если оставить пустым, будет вычислена площадь квадрата): ")

try:
    length = int(length)
    if width:
        width = int(width)
except ValueError:
    print("Ошибка! Вы ввели неверные данные!")
else:
    result = calculate_area(length, width)
    print(result)

#Виталий здраствуйте как здесь реализовать это задачу?