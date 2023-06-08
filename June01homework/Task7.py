def get_total_seconds(hours, minutes, seconds):
    try:
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    except TypeError:
        # VN: функция, задача которой - вычисление, не должна заниматься вводом-выводом
        # лучше здесь написать return None. Тем более, что ниже в программе у вас есть проверка на это
        print("Некорректные данные! Пожалуйста, введите целые числа для часов, минут и секунд.")

hours = int(input("Введите часы: "))
minutes = int(input("Введите минуты: "))
seconds = int(input("Введите секунды: "))

time_in_seconds = get_total_seconds(hours, minutes, seconds)
if time_in_seconds is not None:
    print("Общее время в секундах:", time_in_seconds)
