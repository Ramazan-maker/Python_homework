hour = int ( input ( 'Введите час:'))#запрос у пользователя времени(часа)
minute =  int ( input ( 'Введите минуты:'))#запрос у пользователя времени (минуты)
next_hour =23- hour#вычисление сколько осталось  часа
next_minute= 59-minute#вычисление сколько осталось  минуты
print(next_hour,next_minute)#вывод значении