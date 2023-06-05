def format_time():
    seconds = input("Введите количество секунд: ")
    try:
        s= int(seconds)
    except TypeError:
        print("Некорректные данные! Пожалуйста, введите целые числа для часов, минут и секунд.")
    else:
        h = s // 3600
        m = (s - h * 3600) // 60
        s = s - h * 3600 - m * 60
    time = f"Time: {h:02d}:{m:02d}:{s:02d}"
    return time

result = format_time()
print(result)
