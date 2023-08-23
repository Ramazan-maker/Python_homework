def bubble_sort(mas,key=None):
    n = len(mas) #Рассчитываем длину списка здесь
    count = 0
    for run in range(n-1):
        for i in range(n-1-run):
            #if mas[i]>mas[i+1]:
            element_i = key(mas[i]) if key else mas[i]
            element_i_plus_1 = key(mas[i + 1]) if key else mas[i + 1]

            if element_i > element_i_plus_1:
                count+=1
                mas[i],mas[i+1] = mas[i+1],mas[i]
    return mas,count

template,count= bubble_sort([5,7,4,3,5,6])
print("Sorted array:",template)
print("Замены:",count)

template, count = bubble_sort([5, 7, 4, 3, 5, 6], key=lambda x: x )
print("\nBubble Sort (с key):")
print("Sorted array:", template)
print("Замены:", count)