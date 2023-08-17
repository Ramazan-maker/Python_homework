def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x< elem,s))
    center = [i for i in s if i == elem]
    right = list (filter(lambda x: x> elem,s))
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([7,6,10,5,9,8,7,7,3,4]))