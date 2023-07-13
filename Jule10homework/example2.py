fruits = ['apple','banana','cherry','apple','orange','banana']
passed = {} # Словарь для уже просмотренных элементов
duplicates = [] # Список для найденных дубликатов
for item in fruits:#мы тут перебераем список в методе fruits
    if item in passed: # провераем если в item мы пробежались по методу fruits и все элементы кладем в passed
        duplicates.append(item)#если найдем дубликаты то их кладем в отдельный метод duplicates 
    else:#иначе не найдено дубликатов то выводим Тrue и сохранаем значение
        passed[item] = True
print(f'Найденные дубликаты: {duplicates}')
