# Сортировка выборкой

user_in = input("Введите список цифр через запятую: ")
user_in = user_in.split(',')
the_list = list(map(lambda x: int(x), user_in))

n = len(the_list)

for i in range(n):
    min_item = min(the_list[i:n])# получаем мин элемент в подсписке начиная с позиции i и до конца списка
    min_index = the_list[i:n].index(min_item)+i # находит минимальный индекс в подсписке
    the_list[i],the_list[min_index] = the_list[min_index],the_list[i]#меняем местами

print(the_list)