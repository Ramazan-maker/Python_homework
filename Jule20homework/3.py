import random

# задаем размеры матрицы
N = 3
M = 4

# создаем матрицу со случайными числами от -10 до 10
matrix = [[random.randint(-10, 10) for j in range(M)] for i in range(N)]

# выводим матрицу в консоль
for row in matrix:
    print(row)

# находим и выводим максимальные и минимальные элементы в каждой строке
for i in range(N):
    row_max = max(matrix[i])
    row_min = min(matrix[i])
    print(f"Максимальный элемент в {i+1}-й строке: {row_max}")
    print(f"Минимальный элемент в {i+1}-й строке: {row_min}")

# находим и выводим максимальные и минимальные элементы в каждом столбце
for j in range(M):
    col_max = max(matrix[i][j] for i in range(N))
    col_min = min(matrix[i][j] for i in range(N))
    print(f"Максимальный элемент в {j+1}-м столбце: {col_max}")
    print(f"Минимальный элемент в {j+1}-м столбце: {col_min}")
