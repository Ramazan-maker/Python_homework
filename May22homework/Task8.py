purchase_price = float(input("Введите стоимость покупки в $: "))
discount = float(input("Введите размер скидки в %: "))

# Расчет суммы к оплате
amount_due = purchase_price - (purchase_price * discount / 100)

# Форматирование вывода
output = "Сумма к оплате: $" + "%.2f" % amount_due

# Вывод информации
print(output)
