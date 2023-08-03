import random

# задаем размеры матрицы
N = 3
M = 4

# создаем матрицу со случайными числами от -10 до 10
matrix = [[random.randint(-10, 10) for j in range(M)] for i in range(N)]

# выводим матрицу в консоль
for row in matrix:
    print(row)

# подсчитываем и выводим суммы нечетных элементов в каждой строке
for i in range(N):
    row_sum = sum(x for x in matrix[i] if x % 2 != 0)
    print(f"Сумма нечетных элементов в {i+1}-й строке: {row_sum}")

# подсчитываем и выводим суммы нечетных элементов в каждом столбце
for j in range(M):
    col_sum = sum(matrix[i][j] for i in range(N) if matrix[i][j] % 2 != 0)
    print(f"Сумма нечетных элементов в {j+1}-м столбце: {col_sum}")
