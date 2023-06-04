user_input = input("Введите число от 0 до 9: ")

user_input = int(user_input)
# try:
#     number = int(user_input)
# except ValueError:
#     message = 'Вы ввели неверные данные!'

# else:
# VN: в этой задаче можно вообще не преобразовывать в int, а проверять как текст: if user_input == "0" и тд.
if 0 == user_input:
    print(")")
elif 1== user_input:
    print("!")
elif 2== user_input:
    print("@")
elif 3== user_input:
    print('#')
elif 4 == user_input:
    print('$')
elif 5 == user_input:
    print("%")
elif 6 == user_input:
    print("^")
elif 7 == user_input:
    print("&")
elif 8 == user_input:
    print("*")
elif 9 == user_input:
    print("(")
else:
    print("Вы ввели значение не из диапазона")
