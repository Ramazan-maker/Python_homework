user_input = input("Введите до 10 чисел, разделенных запятой: ")
input_list = user_input.split(',')[:10]

if len(input_list) < 10:
    print("Вы ввели меньше 10 чисел. Введите данные снова.")

even_numbers = []
for item in input_list:
    if int(item) % 2 == 0:
        even_numbers.append(item)

print("Исходный список:", input_list)
print("Список четных чисел:", even_numbers)
