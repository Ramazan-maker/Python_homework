get_user_year = input("Введите год: ")
year = int(get_user_year)
if year % 400 == 0 or(year % 4 == 0 and year % 100 !=0):
#Если год кратен 400 или 4 то он високосный,иначе если год кратен 100 то он невисокосный год
    print("Високосный год   ")
else:
    print("Не високосный год")