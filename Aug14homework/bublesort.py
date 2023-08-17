def bubble_sort(n,mas):
    count = 0
    for run in range(n-1):
        for i in range(n-1-run):
            if mas[i]>mas[i+1]:
                count+=1
                mas[i],mas[i+1] = mas[i+1],mas[i]
    return mas,count

template,count= bubble_sort(6,[5,7,4,3,5,6])
print("Sorted array:",template)
print("Замены:",count)