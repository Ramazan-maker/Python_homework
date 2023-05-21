# Task 1
p = int ( input ( 'Введите число:'))
b = p**2
print('Результат:',b)
# Task 2
user_input1= int ( input ( 'Введите число:'))
user_input2= int ( input ( 'Введите число:'))

aver=(user_input1+user_input2)/2
print(aver)
# Task 3
user_input_kub_dlina = int ( input ( 'Введите длину квадрата:'))
user_input_kub_dlina **=2
print(user_input_kub_dlina)
# Task 4
user_input_km = int ( input ( 'Введите киллометр:'))
km_to_mile = user_input_km/1.609
print(km_to_mile)
# Task 5
user_input_first_number = int ( input ( 'Введите первое число:'))
user_input_second_number = int ( input ( 'Введите второе число:'))
plus = user_input_first_number + user_input_second_number
minus = user_input_first_number -user_input_second_number
umnozh = user_input_first_number * user_input_second_number
delenie = user_input_second_number / user_input_second_number
print('Вывод сложение ',plus,'Вывод минусование ', minus,'Вывод умножение  ' , umnozh,'Вывод деление ' ,delenie)
# Task 6
a= int ( input ( 'Введите первое число:'))
b=  int ( input ( 'Введите второе число:'))
x= -b/a
print(x)
# Task 7
hour = int ( input ( 'Введите час:'))
minute =  int ( input ( 'Введите минуты:'))
next_hour =24- hour
next_minute= 60-minute
print(next_hour,next_minute)
# Task 8
number = int ( input ( 'Введите трехзначное число:'))
second_number= number % 100
sum = second_number % 10
# print(second_number)
print(sum)
# Task 9
number = int ( input ( 'Введите пятизначное число:'))
a = number % 10
b = str(a)
sum = b + str(number)
print(int(sum))

# Task 10 
sales = int ( input ( 'Введите сумму продаж за месяц :'))
salary = (250+(sales*10))/100
print(salary)



