hour = int ( input ( 'Введите час:'))#запрос у пользователя времени(часа)
minute =  int ( input ( 'Введите минуты:'))#запрос у пользователя времени (минуты)
try:
    hour = int(hour)
    minute = int(minute)
except ValueError:
    message = 'Ошибка! Вы ввели неверные данные!'
else:
    next_hour =23- hour#вычисление сколько осталось  часа
    next_minute= 60-minute#вычисление сколько осталось  минуты
    message = "Вам осталось до конца дня %s часов, %s минут" % (next_hour,next_minute)
print(message)#вывод значении