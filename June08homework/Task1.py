start_user_range = input("Введите начальное число диапазона: ")
end_user_range = input("Введите конечное число диапазона: ")
sum=0
try:
    start_num = int(start_user_range)
    end_num = int(end_user_range)
except ValueError:
    print("Ошибка ! Вы ввели не число ")
else:
    for i in range(start_num,end_num + 1):
        sum+=i

print("Сумма чисел в заданном диапазоне: " ,sum)
