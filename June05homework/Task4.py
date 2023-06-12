import random 

def get_random_int(min,max):
    number = random.random() * (max-min)
    number += min
    
    return int(number)


# my_random = get_random_int(1, 100)

def game(my_random,bottom,top,attempts):
    if attempts == 0:
        print(f"Вы проиграли! А число было: {my_random}")
        return
    user_number = input("Угадай число от %s до %s: "  %(bottom,top))
    try:
        user_number = int(user_number)
    except ValueError :
        print("Ошибка! Вы ввели не число! ")
        game(my_random,bottom,top,attempts)
    else:

        if user_number > my_random:
            print("Вы ввели большое число,попробуйте ввести число меньше")
        elif user_number < my_random:
            print("Вы ввели число меньше чем задано,попробуйте ввести число больше")
        elif user_number == my_random:
            print(f"Правильно! Вы угадали за {8 - attempts} попыток.")
            return
        game(my_random,bottom,top,attempts-1)
# game(get_random_int(1,100))
bottom = -20
top= 20
num = get_random_int(bottom,top)
game(num,bottom,top,7)
