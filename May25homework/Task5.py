user_input_first_number = input ( 'Введите первое число:')#запрос у пользователя первого числа для вычисление 
user_input_second_number = input ( 'Введите второе число:')#запрос у пользователя второго числа для вычисление 
try:
    user_input_first_number = int(user_input_first_number)
    user_input_second_number = int(user_input_second_number)
except ValueError:
    message = "Ошибка!Вы ввели некорретные данные!"
else:
    plus = user_input_first_number + user_input_second_number#вычисление сложение первого и второго числа
    minus = user_input_first_number -user_input_second_number#вычисление вычитание первого и второго числа
    umnozh = user_input_first_number * user_input_second_number#вычисление умножение первого и второго числа 
    delenie = user_input_first_number / user_input_second_number#вычисление деление первого и второго числа
    message = """Результат выполнение сложение %s,
Результат выполнение вычитание %s,
Результат выполнение умножение %s , 
Результат выполнение деление %s.
    """ %(plus,minus,umnozh,delenie)

print(message)#вывод всех вычислений,пример задачи калькулятор