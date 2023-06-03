question_square = input("Самый большой город Казахстана по площади? 1 -Шымкент 2-Алматы 3-Астана Ваш ответ: ")
question_flower= input("Какой нациолнальный цветок Японии? 1-Роза 2-Сакура 3-Тульпан Ваш ответ: ")
question_about_earth = input("Сколько дней нужно, чтобы Земля совершила оборот вокруг Солнца? 1-364 2-366 3-365 Ваш ответ: ")
score = 0 
if question_square == '1':
    score +=2
if question_flower == '2':
    score +=2
if question_about_earth == '3':
    score +=2
print ("Вы набрали",score,"очков!")  