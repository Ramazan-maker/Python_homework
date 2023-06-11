positive_count = 0
negative_count = 0
zero_count = 0
even_count = 0
odd_count = 0

for _ in range(10):
    user_input = int(input("Введите число: "))
    
    if user_input > 0:
        positive_count += 1
    elif user_input < 0:
        negative_count += 1
    else:
        zero_count += 1
    
    if user_input % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Статистика:")
print("Положительные числа:", positive_count)
print("Отрицательные числа:", negative_count)
print("Нули:", zero_count)
print("Четные числа:", even_count)
print("Нечетные числа:", odd_count)
