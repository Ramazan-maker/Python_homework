import json
import time

with open("quest.json", encoding="utf-8") as myfile:
    quest = json.load(myfile)

greeting = f"""
Добро пожаловать в игру '{quest["info"]["name"]}'!
Авторы игры: {quest["info"]["author"]},
Версия: {quest["info"]["version"]}
"""
print(greeting)
current_scene = "start"

def show_description(scene):
    description = quest["game"][scene]["description"]
    print(description)

def is_game_end(scene):
    return "ending" in quest["game"][scene]

def show_actions(scene):
    print("Что будете делать?")
    for action in quest["game"][scene]["actions"]:
        print(" -> ", action["name"])
    print()

def get_user_action():
    while True:
        user_in = input()
        if user_in:
            return user_in

def check_action(scene, action_name):
    for allowed_action in quest["game"][scene]["actions"]:
        if action_name == allowed_action["name"]:
            return allowed_action["effect"]

def perform_action(effect):
    global current_scene
    if "go" in effect:
        current_scene = effect["go"]
    elif "have" in effect:
        print(f"Вы получили: {effect['have']}")

while True:
    time.sleep(3)
    line = '-' * 50
    print(f"\n {line} \n")
    show_description(current_scene)
    if is_game_end(current_scene):
        print("Игра завершена.")
        break
    show_actions(current_scene)
    action = get_user_action()
    effect = check_action(current_scene, action)
    if effect:
        perform_action(effect)
    else:
        print("Такого действия нет. Выберите другое")
