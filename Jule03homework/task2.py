
file_path = open('file.txt',encoding='utf-8')
text = file_path.read()

max_line_lenght = input("Введите максимальную длину строк: ")

try:
    max_line_lenght = int(max_line_lenght)
except ValueError:
    print('Ошибка!Вы ввели неккоре')

#это функция разбивает строки длина которых не превышает указанный размер на более короткие строки не разрывая слово
def spl(text, maxlen):
    text1 = ''  # записываем сюда новую строку
    c = 0  # счётчик символов с строке
    for i in text.split():  # проходим по каждому слову
        c += len(i)  # прибавляем длину слова
        if c >= maxlen:  # если символов больше максимума
            text1 += '\n'  # перенос строки
            c = len(i)  # счётчик равен первому слову в строке
        elif text1 != '':  # условие, чтобы не ставить пробел перед 1-м словом
            text1 += ' '  # ставим пробел после непоследнего слова в строке
            c += 1  # учитываем его в счётчике
        text1 += i  # прибавляем слово
    return text1  # возвращаем новый текст
#Исправить регистр символов - предложения должны начинаться с большой буквы.

def fix_case(text):
    return '.'.join(map(str.capitalize, text.split('. ')))
#﻿﻿﻿﻿Удалить лишние пробелы между словами и в конце строк.

def delete_space(text):
    words = text.split()
    words = list(filter(None,words))
    new_text = " " .join(words)
    return new_text
# Выделить начало абзаца - четырьмя пробелами.

def capitalize_sentences_4spaces(text):
    lines = text.split("\n")
    new_text = ""
    for line in lines:
        new_text += "    " + line + "\n"
    print(new_text)
#Выровнять текст по ширине, чтобы каждая строка содержала
#одинаковое количество символов (при необходимости добавлять пробелы между словами), если только это не последняя строка.
def align_text(text, max_line_length):
    lines = text.splitlines()
    aligned_lines = []

    for line in lines:
        # Разбиваем строку на слова
        words = line.split()

        # Если это не последняя строка, выравниваем текст по ширине
        if len(line) < max_line_length:
            spaces_to_add = max_line_length - len(line)  # Вычисляем количество пробелов, которое нужно добавить
            num_gaps = len(words) - 1  # Количество интервалов между словами
            if num_gaps > 0:
                spaces_per_gap = spaces_to_add // num_gaps  # Равномерно распределяем пробелы между интервалами
                extra_spaces = spaces_to_add % num_gaps  # Оставшиеся пробелы добавляем по одному к интервалам
                new_line = words[0]
                for word in words[1:]:
                    spaces = spaces_per_gap + 1 if extra_spaces > 0 else spaces_per_gap
                    new_line += " " * spaces + word
                    extra_spaces -= 1
            else:
                new_line = line
        else:
            new_line = line

        aligned_lines.append(new_line)

    # Объединяем отформатированные строки обратно в текст
    new_text = "\n".join(aligned_lines)
    return new_text
#Удаление пустых строк
def strip_empty_lines(text):
    lines = text.splitlines()
    stripped_lines = [line for line in lines if line.strip()]
    new_text = "\n".join(stripped_lines)
    return new_text

template = spl(text,max_line_lenght)
template2 = delete_space(text)
template3 = fix_case(text)
template4 = capitalize_sentences_4spaces(text)
template5 = align_text(text,max_line_lenght)
template6 = strip_empty_lines(text)
print("Result: ",template)
print("Result: ",template2)
print("Result: ",template3)
print("Result: ",template4)
print("Result: ",template5)
print("Result: ",template6)