#import fileinput
file_path = open('./file.txt',encoding='utf-8')
text = file_path.read()
file_path.close()


user_input_source_word = input('Введите исходное слово: ')
user_input_word_replacement = input('Введите слово, на которое нужно заменить: ')
new_word = text

if user_input_source_word.lower() in text:
    new_word = text.replace(user_input_source_word.lower(), user_input_word_replacement.lower())

if user_input_source_word.upper() in new_word:
    new_word = new_word.replace(user_input_source_word.upper(), user_input_word_replacement.upper())

if user_input_source_word.title() in new_word:
    new_word = new_word.replace(user_input_source_word.title(), user_input_word_replacement.title())
    
print(new_word)


