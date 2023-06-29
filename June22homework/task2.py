from random import randint

N = 10
a = []

for i in range(N):
    a.append(randint(1, 100))
    print(a[i], end=' ')
print()

print('Элементы больше предыдущего:')
for i in range(1, N):
    if a[i] > a[i-1]:
        print(a[i], end=' ')
print()
