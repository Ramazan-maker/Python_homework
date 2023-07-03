# Задача: Подсчет количества слов в предложении

# Напишите программу, которая принимает на вход предложение и выводит количество слов в этом предложении.

# Правила:

# Слово - это последовательность символов, разделенных пробелами.
# Знаки препинания считаются частью слова. Например, "hello," и "hello" считаются двумя разными словами.


def count_words(sentence):
    # Разделяем предложение на слова с помощью метода split()
    words = sentence.split()

    # Возвращаем количество слов в предложении
    return len(words)

if __name__ == "__main__":
    input_sentence = "Hello, how are you today?"
    word_count = count_words(input_sentence)
    print(f"The number of words in the sentence is: {word_count}")
