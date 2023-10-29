def iter_matrix(matrix):

    row = 0
    while row < len(matrix):
        column = 0
        while column < len(matrix[row]):
            yield matrix[row][column]
            column += 1
        row += 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for item in iter_matrix(matrix):
    print(item)