import json
import time

def load_quest(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def play_quest(quest):
    game_info = quest['game_info']
    game_scenes = quest['game']

    print(f'Название игры: {game_info["NAME"]}')
    print(f'Версия: {game_info["VERSION"]}')
    print(f'Автор: {game_info["AUTHOR"]}')

    current_scene = 'SCENE_0'
    visited_scenes = []

    while True:
        scene = game_scenes[current_scene]
        print('\n' + scene['DESCRIPTION'])
        actions = scene.get('ACTIONS')

        if actions is None:
            print('\nИгра окончена.')
            break

        print('\nЧто будете делать?')
        valid_actions = []
        for index, action in enumerate(actions, start=1):
            conditions = action.get('WHEN', {})
            if validate_conditions(conditions, visited_scenes):
                valid_actions.append(action)
                action_name = action['NAME']
                print(f'{index}. {action_name}')

        if not valid_actions:
            print('\nУ вас нет доступных действий. Попробуйте что-то другое.')
            continue

        choice = input('\nВыберите номер действия: ')

        if choice.isdigit() and 1 <= int(choice) <= len(valid_actions):
            action = valid_actions[int(choice) - 1]
            execute_action(action, game_scenes)
            current_scene = action['EFFECT'].get('GO', current_scene)
            visited_scenes.append(current_scene)
        else:
            print('\nВы ввели некорректный номер действия. Попробуйте снова.')

        time.sleep(2)

def validate_conditions(conditions, visited_scenes):
    if 'HAVE' in conditions:
        item = conditions['HAVE']
        if item not in inventory:
            return False

    if 'LACK' in conditions:
        item = conditions['LACK']
        if item in inventory:
            return False

    if 'MISSED' in conditions:
        scene = conditions['MISSED']
        if scene in visited_scenes:
            return False

    if 'PASSED' in conditions:
        scene = conditions['PASSED']
        if scene not in visited_scenes:
            return False

    return True

def execute_action(action, game_scenes):
    effect = action['EFFECT']

    if 'ALERT' in effect:
        print('\n' + effect['ALERT'])

    if 'COLLECT' in effect:
        item = effect['COLLECT']
        inventory.append(item)
        print(f'\nВы взяли {item}.')

    if 'DISPOSE' in effect:
        item = effect['DISPOSE']
        inventory.remove(item)
        print(f'\nВы избавились от {item}.')

def main():
    quest_file = 'kolobok.json'
    quest = load_quest(quest_file)
    play_quest(quest)

if __name__ == '__main__':
    inventory = []
    main()