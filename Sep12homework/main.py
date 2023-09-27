import threading

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def calculate_average(sublist, result):
    avg = sum(sublist) / len(sublist)
    result.append(avg)

# Разбиваем список на подсписки
chunk_size = len(numbers) // 4  # Разбиваем на 4 подсписка
sublists = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

# Создаем список для хранения результатов
averages = []

# Создаем и запускаем потоки для вычисления средних значений
threads = []
for sublist in sublists:
    thread = threading.Thread(target=calculate_average, args=(sublist, averages))
    threads.append(thread)
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

# Вычисляем общее среднее значение
total_average = sum(averages) / len(averages)

print("Среднее значение:", total_average)

