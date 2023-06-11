def get_total_seconds(hours, minutes, seconds):

   
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds
    
hours = input("Введите часы: ")
minutes = input("Введите минуты: ")
seconds = input("Введите секунды: ")
try:
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
# VN: Здесь исключение ValueError
except TypeError:
    print("Некорректные данные! Пожалуйста, введите целые числа для часов, минут и секунд.")
else:

    time_in_seconds = get_total_seconds(hours, minutes, seconds)

if time_in_seconds is not None:
    print("Общее время в секундах:", time_in_seconds)
