import datetime


def log_with_timestamp(func):
    def wrapper(*args, **kwargs):
        # Получить текущее время
        current_time = datetime.datetime.now()

        # Преобразовать время в строку в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС"
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Вызвать функцию и записать результат
        result = func(*args, **kwargs)

        # Вывести лог с временной меткой
        print(
            f"{timestamp} - Вызвана функция {func.__name__} с аргументами {args} и ключевыми аргументами {kwargs}. Результат: {result}")

        return result

    return wrapper


# Пример использования декоратора
@log_with_timestamp
def add(x, y):
    return x + y


@log_with_timestamp
def subtract(x, y):
    return x - y


result1 = add(5, 3)
result2 = subtract(10, 4)


#https://ru.hexlet.io/courses/python-functions/lessons/decorators/theory_unit