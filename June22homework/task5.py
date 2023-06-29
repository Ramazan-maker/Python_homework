import random
numbers = [random.randint(1,100) for _ in range(20)]

min_num = min(numbers)
max_num = max(numbers)

min_index = numbers.index(min_num)
max_index = numbers.index(max_num)

distance = abs(max_index - min_index)

print("Расстояние между минимальным и максимальным числами:", distance)