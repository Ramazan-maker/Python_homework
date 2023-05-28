word = input("Введите слово: ")
# Получаем первые две буквы
first_two_letters = word[:2]

# Получаем последние две буквы
last_two_letters = word[-2:]

# Формируем сокращение
abbreviation = first_two_letters + "-" + last_two_letters

# Выводим сокращение
print("Сокращение:", abbreviation)