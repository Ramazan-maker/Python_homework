purchase_amount = input("Введите сумму покупки: ")

sale = int(purchase_amount)

if sale>=200 and sale <300 :
    discount =sale *0.03

elif sale>=300 and sale <500:
    discount =sale *0.05
elif sale >500:
    discount =sale *0.07
else:
    discount = 0

total_amount = sale - discount

print(total_amount)