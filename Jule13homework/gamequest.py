# #!/usr/bin/env python
# import time
# import readline


# with open('kolobok.json','r',encoding='utf-8') as fileName:
#     if not fileName:
#         print("Не указан файл игры.")
#         exit(1)


# game_end = 0
# currentScene = 'SCENE_0'
# pocketItems  = ()
# passedScenes = ()
# availActions = ()
# say = print
# say ("Добро пожаловать в игру $game{NAME}! ")
# say ("Автор игры: $game{AUTHOR} ")
# say ("Нажмите любую клавишу, чтобы начать. ")
# c = input()

# pause()
# show_scene()
# while not game_end:
#     GameAction()

# print("Конец.\n\n")


# def pause():
#     for _ in range(5):
#         time.sleep(0.1)
#         print(".", end="", flush=True)

# def show_scene():
#     Disappear()
#     ShowDescription()
#     print('\n')
#     ShowPocket()
#     print('\n')
#     ShowActions()

# def GameAction():
#     if not game[currentScene]["ACTIONS"]:
#         game_end = True
#         return
#     act = GetAction()
#     if act < 0:
#         return
#     effect = act["EFFECT"]
#     if effect["COLLECT"]:
#         pocketItems.append(effect["COLLECT"])
#     if effect["DISPOSE"]:
#         pocketItems = [item for item in pocketItems if item != effect["DISPOSE"]]
#     if effect["ALERT"]:
#         Disappear()
#         print(effect["ALERT"])
#         c = input()
#         ShowScene()
#     if effect["GO"]:
#         if currentScene != effect["GO"]:
#             passedScenes.append(currentScene)
#             currentScene = effect["GO"]
#             ShowScene()


# def GetAction():
#     autocomplist = []
#     for action in availActions:
#         autocomplist.append(action["NAME"])
#     c = input("> ")
#     while c not in autocomplist:
#         c = input("> ")
#     Pause()
#     print("> ")
#     for action in availActions:
#         if c == action["NAME"]:
#             return action
#     return -1

# def ShowDescription():
#     text = game[currentScene]["DESCRIPTION"]
#     text = text.replace("\n", "|")
#     text = " ".join(text.split())
#     text = text.replace("|", "\n ")
#     print(text)

# def ShowPocket():
#     if not game[currentScene]["ACTIONS"]:
#         return
#     text = "У тебя есть:  "
#     if len(pocketItems) < 0:
#         text += "ничего, "
#     else:
#         for i in pocketItems:
#             text += i + ", "
#     print(text[:-2])

# def ShowActions():
#     if not game[currentScene]["ACTIONS"]:
#         return
#     text = "Что будешь делать? ("
#     whenOk = True
#     act_array = game[currentScene]["ACTIONS"]
#     availActions = []
#     for action in act_array:
#         whenOk = True
#         if action["WHEN"]:
#             if action["WHEN"]["HAVE"]:
#                 whenOk &= action["WHEN"]["HAVE"] in pocketItems
#             if action["WHEN"]["LACK"]:
#                 whenOk &= action["WHEN"]["LACK"] not in pocketItems
#             if action["WHEN"]["PASSED"]:
#                 whenOk &= currentScene in passedScenes
#             if action["WHEN"]["MISSED"]:
#                 whenOk &= currentScene not in passedScenes
#         if whenOk:
#             text += action["NAME"] + ", "
#             availActions.append(action)
#     print(text[:-2] + ")\n")

# def Pause():
#     for i in range(6):
#         time.sleep(0.1)
#         print(".", end="")
#     print()

# def Disappear():
#     print("\033[2J")

import time
import json


game_end = 0
currentScene = "SCENE_0"
pocketItems = []
passedScenes = []
availActions = []
say = print


def pause():
    for _ in range(5):
        time.sleep(0.1)
        print(".", end="", flush=True)




def GameAction():
    global game_end, currentScene, pocketItems, passedScenes, availActions

    if not game[currentScene]["ACTIONS"]:
        game_end = True
        return

    act = GetAction()
    if act < 0:
        return
    effect = act["EFFECT"]
    if effect["COLLECT"]:
        pocketItems.append(effect["COLLECT"])
    if effect["DISPOSE"]:
        pocketItems = [item for item in pocketItems if item != effect["DISPOSE"]]
    if effect["ALERT"]:
        Disappear()
        print(effect["ALERT"])
        c = input()
        ShowScene()
    if effect["GO"]:
        if currentScene != effect["GO"]:
            passedScenes.append(currentScene)
            currentScene = effect["GO"]
            ShowScene()


def GetAction():
    global availActions

    autocomplist = [action["NAME"] for action in availActions]
    c = input("> ")
    while c not in autocomplist:
        c = input("> ")
    pause()
    print("> ")
    for action in availActions:
        if c == action["NAME"]:
            return action
    return -1


def ShowDescription():
    text = game[currentScene]["DESCRIPTION"]
    text = text.replace("\n", "|")
    text = " ".join(text.split())
    text = text.replace("|", "\n ")
    print(text)


def ShowPocket():
    if not game[currentScene]["ACTIONS"]:
        return
    text = "У тебя есть:  "
    if len(pocketItems) < 1:
        text += "ничего, "
    else:
        text += ", ".join(pocketItems) + ", "
    print(text[:-2])


def ShowActions():
    if not game[currentScene]["ACTIONS"]:
        return
    text = "Что будешь делать? ("
    whenOk = True
    act_array = game[currentScene]["ACTIONS"]
    availActions = []
    for action in act_array:
        whenOk = True
        if action["WHEN"]:
            if action["WHEN"]["HAVE"]:
                whenOk &= action["WHEN"]["HAVE"] in pocketItems
            if action["WHEN"]["LACK"]:
                whenOk &= action["WHEN"]["LACK"] not in pocketItems
            if action["WHEN"]["PASSED"]:
                whenOk &= currentScene in passedScenes
            if action["WHEN"]["MISSED"]:
                whenOk &= currentScene not in passedScenes
        if whenOk:
            text += action["NAME"] + ", "
            availActions.append(action)
    print(text[:-2] + ")\n")


def Disappear():
    print("\033[2J")

def show_scene():
    Disappear()
    ShowDescription()
    print('\n')
    ShowPocket()
    print('\n')
    ShowActions()

# Код игры

with open('kolobok.json', 'r', encoding='utf-8') as fileName:
    if not fileName:
        print("Не указан файл игры.")
        exit(1)

# Ваш код продолжается здесь

game = {}  # Добавьте инициализацию переменной game

say("Добро пожаловать в игру $game{NAME}!")
say("Автор игры: $game{AUTHOR}")
say("Нажмите любую клавишу, чтобы начать.")
c = input()

pause()
show_scene()
while not game_end:
    GameAction()

print("Конец.\n\n")
