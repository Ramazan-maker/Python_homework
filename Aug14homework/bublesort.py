def bubble_sort(n,mas,key=None):
    #VN:        ^ размер списка здесь лишний, т.к. функция сама в состоянии его вычислить: n = len(mas)
    count = 0
    for run in range(n-1):
        for i in range(n-1-run):
            #if mas[i]>mas[i+1]:
            element_i = key(mas[i]) if key else mas[i]
            element_i_plus_1 = key(mas[i + 1]) if key else mas[i + 1]
            #VN: очень неплохо - присваивание  ^^^^^^^^^^^ с условием.

            if element_i > element_i_plus_1:
                count+=1
                mas[i],mas[i+1] = mas[i+1],mas[i]
    return mas,count

template,count= bubble_sort(6,[5,7,4,3,5,6])
print("Sorted array:",template)
print("Замены:",count)

template, count = bubble_sort(6, [5, 7, 4, 3, 5, 6], key=lambda x: x % 2)
print("\nBubble Sort (с key):")
print("Sorted array:", template)
print("Замены:", count)