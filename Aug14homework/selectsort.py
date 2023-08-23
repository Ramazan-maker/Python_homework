def selectionSort(array, key=None):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            compare_a = key(array[i]) if key else array[i]
            compare_b = key(array[min_idx]) if key else array[min_idx]

            if compare_a < compare_b:
                min_idx = i

        # Swap min element with the first element of the unsorted part
        array[step], array[min_idx] = array[min_idx], array[step]


data_with_key = [21, 45, 27, 11, 9]
selectionSort(data_with_key, key=lambda x: x % 3)
print('Sorted Array with Key in Ascending Order:')
print(data_with_key)

data_without_key = [-2, 45, 0, 11, -9]
selectionSort(data_without_key)
print('Sorted Array without Key in Ascending Order:')
print(data_without_key)
