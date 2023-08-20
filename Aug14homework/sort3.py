# Быстрая сортировка

user_in = input("Введите список цифр через запятую: ")
user_in = user_in.split(',')
the_list = list(map(lambda x: int(x), user_in))

def quicksort(array, key=None):
    if len(array) <= 1:#проверка списка на пустоту
        return array

    pivot = array[0]#начальный или базовый случай в качестве опорного элемента
    less = [x for x in array if x < pivot]#пробегаемся по элементам списка и проверяем если есть ли значение меньше опорного элемента
    #если есть то перемещаем их вниз
    equal = [x for x in array if x == pivot]#если равен то оставляем
    more = [x for x in array if x > pivot]#если больше опорного элемента то перемезаем в вверх

    return quicksort(less) + equal + quicksort(more) #[меньше опорного элемента,равен опорному элементу,больше опорного элемента]

print(quicksort(the_list))

