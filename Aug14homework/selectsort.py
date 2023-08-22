
def selectionSort(array, size,key=None):
    #VN: то же самое    ^^^^^^ размер списка функция в состоянии узнать сама: size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


#VN: здесь аргумент key никак не используется, задача не решена

data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)