import random

def random_number_generator(min_value, max_value):
    while True:
        yield random.randint(min_value, max_value)

# Пример использования:
min_value = 1
max_value = 100
random_gen = random_number_generator(min_value, max_value)

for _ in range(10):
    random_number = next(random_gen)
    print(random_number)
