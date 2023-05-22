number = int ( input ( 'Введите пятизначное число:'))
a = number % 10
b = str(a)
sum = b + str(number)
print(int(sum))