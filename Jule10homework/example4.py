orders = [{'product': 'apple','quantity': 500},
          {'product': 'banana','quantity': 300},
          {'product': 'apple','quantity': 200},
          {'product': 'orange','quantity': 400},
          {'product': 'banana','quantity': 1000}]
# Создание словаря для хранения суммарного количества продуктов
product_quantity = {}
#orders и подсчитывает общее количество каждого продукта, используя словарь product_quantity
for order in orders:
    product = order['product']#Проходя по каждому элементу order в списке orders, код извлекает значение ключей 'product' и 'quantity'. 
                                 # Переменная product содержит название продукта, а quantity содержит количество заказанного продукта.
    quantity = order['quantity']
    """
    Затем код проверяет, есть ли уже запись для данного продукта в словаре product_quantity 
    с помощью условного оператора if product in product_quantity:. Если запись уже существует, 
    то к существующему значению количества продукта прибавляется текущее значение quantity с помощью оператора +=. 
    Это позволяет увеличивать существующее количество продукта.
    """
    if product in product_quantity:
        product_quantity[product] += quantity
    else:
        product_quantity[product] = quantity
# Вывод результатов
for product, quantity in product_quantity.items():
    print(f'{product}: {quantity}')
#Этот код выполняет итерацию по элементам словаря product_quantity с помощью цикла for. 
# На каждой итерации цикла извлекаются ключ (product) и значение (quantity) пары ключ-значение из словаря.
#Таким образом, код печатает на экране каждый продукт из словаря product_quantity вместе с его соответствующим количеством. 
# Каждая строка вывода будет иметь формат "название продукта: количество".