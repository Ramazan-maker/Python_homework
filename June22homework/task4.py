import random
list1 = [random.randint(1,20) for _ in range(10)]
list2 =  [random.randint(1,20) for _ in range(10)]
print("Изначальный списки:")
print("Первый список: ",list1)
print('Второй список: ',list2)
for item in list2:
    if item in list1:
        list1.remove(item)
list1 = list(set(list1))
print("Список после удаление элементов: ",list1)