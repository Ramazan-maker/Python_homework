sales =  input ( 'Введите сумму продаж за месяц :')#запрос у пользователя значение 
try:
    sales = int(sales)
except ValueError:
    message = "Ошибка! Вы ввели неверные данные"
else:    
    PercentageOfSales = (sales*10)/100
    salary = 250+PercentageOfSales# вычисление зарплаты 
    message = ''' Ваше продажа за месяц %s
    10 процентов от продаж %s
    Итого ваша заработная плата %s
    ''' % (sales,PercentageOfSales,salary)
print(message)#вывод значение зарплаты

'''
VN:
Введите сумму продаж за месяц :1000
102.5

Должно быть 350.  (10% от продаж + 250)
'''

