user_input1= input ( 'Введите число:')#ввод пользователя
user_input2= input ( 'Введите число:')#ввод пользователя
template = "Ваш результат %s среднего арифмитического числа"
try:
    user_input1 = int(user_input1)
    user_input2 = int(user_input2)
except ValueError:
    message = "Ошибка!Вы ввели неверное данные!"
else:
    aver=(user_input1+user_input2)/2 #вычисление среднего арифмитического числа
    message = template % aver
print(message)#выводит средное арифматическое число 