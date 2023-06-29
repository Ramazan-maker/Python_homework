from functools import reduce 
# Используя функцию map() печатайте квадрат, каждого числа округленный до 3х знаков

square_areas = [4.5343,54.543,34.435,1.453,9.665]
result = list(map(round,square_areas,range(1,3)))

print("Result map(): ",result)
# Используя функцию filter() печатайте только те имена, у которых меньше 7 букв

name_list = ["Ramazan",'Ali','Baron','Josephina','Yari','Oleg']
filtered_name = list(filter(lambda x: len(x)<7,name_list))
for name in filtered_name:
    print("Result filter: ",name) 
# используя функцию reduce() напечатайте произведение этих чисел
my_numbers = [1,4,6,54,34,31]
result_reduce = reduce(lambda num1,num2: num1*num2,my_numbers)
print("Результат reduce: ",result_reduce)