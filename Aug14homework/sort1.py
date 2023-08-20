# Сортировка "пузырьком"

user_in = input("Введите список цифр через запятую: ")
user_in = user_in.split(',')
the_list = list(map(lambda x: float(x), user_in))#преобразоваем в число и записываем в список

is_sorted = False #обозначаем не отсортированный список
while not is_sorted:#будет выполнятся пока список не отсотируется
    is_sorted = True
    for i in range(len(the_list) - 1):# все индексы элементов списка кроме последнего
        if the_list[i] > the_list[i+1]: #проверка если текущий элемент больше следующего то значение меня№тся местами
            the_list[i], the_list[i+1] = the_list[i+1], the_list[i] #меняем порядок и таким образом впслывает пузырок
            is_sorted = False
        # j = len(the_list) - i - 1
        # if the_list[j] > the_list[j-1]:
        #     the_list[j], the_list[j-1] = the_list[j-1], the_list[j]
        #     is_sorted = False

print(the_list)