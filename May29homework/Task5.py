usd_amount = input('Введите количество USD: ')
currency = input("Введите валюту для конвертации (EUR,UAN,AZN):")

usd_amount = float(usd_amount)
if currency == 'EUR':
    converted_amount = usd_amount * 0.85
    print("Доллары ",usd_amount,"конверт в ",converted_amount,"EUR")
elif  currency == 'UAN':
    converted_amount = usd_amount * 27.3
    print("Доллары ",usd_amount,"конверт в ",converted_amount ,"UAN")
elif currency == 'AZN':
    converted_amount = usd_amount * 1.7
    print("Доллары ",usd_amount,"конверт в ",converted_amount, 'AZN')
else:
    print("Выбранная валюта недоступна  ")