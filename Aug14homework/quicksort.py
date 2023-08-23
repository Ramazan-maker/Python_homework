def quick_sort(s,key=None):
    if len(s) <= 1:
        return s
    key_func = key if key else lambda x :x
    elem = s[0]
    left = list(filter(lambda x: key_func(x)< key_func(elem),s))
    center = [i for i in s if key_func(i) == key_func(elem)]
    right = list (filter(lambda x: key_func(x)> key_func(elem),s))
    return quick_sort(left,key) + center + quick_sort(right,key)


print('Without key: ',quick_sort([7,6,10,5,9,8,7,7,3,4]))

print("with key: ",quick_sort([7,6,10,5,9,8,7,7,3,4],key=lambda x:x%2))


