"""
Написать функцию, которая принимает время (часы, минуты, секунды) и возвращает его в виде строки в формате «чч:мм:сс». 
Если при вызове функции минуты и/или секунды не были переданы, то выводить их как 00.
"""

def format_time():
    hours = input("Введите часы: ")
    minutes = input("Введите минуты: ")
    seconds = input("Введите секунды: ")
    try:
        hours = int(hours)
        minutes = int(minutes) if minutes != "" else 0
        seconds = int(seconds) if seconds != "" else 0
    except ValueError:
        print("Некорректные данные! Пожалуйста, введите целые числа для часов, минут и секунд.")
    else:
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return time_string

result = format_time()
if result is not None:
    print(result)


