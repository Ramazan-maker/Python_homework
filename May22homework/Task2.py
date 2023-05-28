word = input('Введите слово: ')# запрос у пользователя какого либо слово
half_length = len(word) // 2
first_half = word[:half_length]
second_half = word[half_length:]

print("Первая половина:", first_half)
print("Вторая половина:", second_half)