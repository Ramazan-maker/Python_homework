def calculate_volume(diameter, height):
    # Вычисляем объём бака по формуле: V = π * r^2 * h
    # Для перевода метров в литры умножаем результат на 1000
    volume = (3.1415 * (diameter / 2) ** 2 * height) * 1000
    return volume


diameter = input("Введите диаметр бака (в метрах): ")
height = input("Введите высоту бака (в метрах): ")
try:
    diameter = float(diameter)
    height = float(height)
except ValueError:
    print("Ошибка! Вы ввели некорректные данные!")
else:
    result = calculate_volume(diameter, height)
    print(result)
