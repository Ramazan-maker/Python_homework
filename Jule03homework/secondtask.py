def split_into_syllables(word):
    vowels = 'аеёиоуыэюя'  # Список гласных букв для русского языка
    syllables = []
    syllable = ''

    for letter in word:
        syllable += letter
        if letter in vowels:
            syllables.append(syllable)
            syllable = ''

    return '-'.join(syllables)


# Запрос слова у пользователя
word = input("Введите слово: ")

# Разделение слова на слоги
syllables = split_into_syllables(word)

# Вывод результата
print(syllables)
