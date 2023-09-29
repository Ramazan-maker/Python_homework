import threading
import time

def average_mean(numbers, result_list):
    total = sum(numbers)
    mean = total / len(numbers)
    result_list.append(mean)  # Добавляем среднее значение в список

def parallel_compute_mean(numbers, n_threads):
    threads = []
    results = []

    for i in range(n_threads):
        start = i * len(numbers) // n_threads
        end = (i + 1) * len(numbers) // n_threads
        numbers_chunk = numbers[start:end]
        thread = threading.Thread(target=average_mean, args=(numbers_chunk, results))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results) / len(results)

numbers = [12, 45, 54, 65, 57, 43, 100000, 435, 4646, 4443546]
start = time.time()
mean = parallel_compute_mean(numbers, 4)
end = time.time()

print("Mean:", mean)
print("Time:", end - start)
