import datetime


def action_based_on_time():
    current_time = datetime.datetime.now()

    current_hour = current_time.hour

    if 6 <= current_hour < 12:
        return "Доброе утро! Время для завтрака."
    elif 12 <= current_hour < 18:
        return "Добрый день! Время для обеда."
    elif 18 <= current_hour < 22:
        return "Добрый вечер! Время для ужина."
    else:
        return "Доброй ночи! Время отдохнуть."


message = action_based_on_time()
print(message)
