user_input_kub_dlina = input ( 'Введите длину квадрата:')#запрос у пользователя длины квадрата
user_input_kub_dlina **=2 #Вычисление квадрата площади
template = "Результат вычисления квадрата площади %s"
try:
    user_input_kub_dlina = int(user_input_kub_dlina)
except ValueError:
    message = "Ошибка!Вы ввели неверные данные"
else:
    user_input_kub_dlina **=2 #Вычисление квадрата площади
    message = template % user_input_kub_dlina

print(message)#вывод квадрата площади