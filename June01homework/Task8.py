def format_time(s):
    h = s // 3600
    m = (s - h * 3600) // 60
    s = s - h * 3600 - m * 60
    time = f"Time: {h:02d}:{m:02d}:{s:02d}"
    return time

seconds = input("Введите количество секунд: ")
try:
    s= int(seconds)
# VN: Здесь исключение ValueError
except TypeError:
    print("Некорректные данные! Пожалуйста, введите целые числа для часов, минут и секунд.")
else:
    result = format_time(s)
    print(result)
