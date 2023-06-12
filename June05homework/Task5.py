import random 

def get_random_int(min,max):
    number = random.random() * (max-min)
    number += min
    
    return int(number)


def game(my_random,bottom,top,attempts):
    if attempts == 0:
        print(f"Вы проиграли! А число было: {my_random}")
        return False
    user_number = input("Угадай число от %s до %s: "  %(bottom,top))
    try:
        user_number = int(user_number)
    except ValueError :
        print("Ошибка! Вы ввели не число! ")
        return game(my_random,bottom,top,attempts)
    else:

        if user_number > my_random:
            print("Вы ввели большое число,попробуйте ввести число меньше")
        elif user_number < my_random:
            print("Вы ввели число меньше чем задано,попробуйте ввести число больше")
        elif user_number == my_random:
            print(f"Правильно! Вы угадали за {8 - attempts} попыток.")
            return True
        return game(my_random,bottom,top,attempts-1)

bottom = -20
top= 20
play_again = True

while play_again:
    num = get_random_int(bottom,top)
    game(num,bottom,top,7)
    answer = input("Хотите ещё раз сыграть (да/нет)? ")
    if answer.lower() in ["да", "д", "yes"]:
        play_again = True
    else:
        play_again = False

print("Спасибо за игру!")