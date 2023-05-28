user_input_km = input ( 'Введите киллометр:')#запрос у пользователя км
try:
    user_input_km = int(user_input_km)
except ValueError:
    message = "Ошибка! Вы ввели неверные данные!"
else:
    km_to_mile = user_input_km/1.609#вычисление км в милли
    message  = "Ваше значение %s км,результат вычисление значение в миллах %s" % (user_input_km,km_to_mile)
print(message)#вывод вычисление км в милли