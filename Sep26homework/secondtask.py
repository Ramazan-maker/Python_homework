import datetime


# now = datetime.datetime.now()
# print(now)
#
# print(now.year, now.month, now.day)

# # Создание объекта date
# d = datetime.date(2023, 9, 1)
# print(d)
# # Извлечение частей даты
# print(d.year, d.month, d.day)

# t = datetime.time(12, 0, 0)
# print(t)
# # Извлечение частей времени
# print(t.hour, t.minute, t.second)

# dt = datetime.datetime(2023, 9, 1, 12, 0, 0)
# print(dt)
# # Извлечение частей даты и времени
# print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)


# delta = datetime.timedelta(days=7, hours=3)
# print(delta)
# # Вычисление новой даты
# new_date = datetime.datetime.now() + delta
# print(new_date)

# now = datetime.datetime.now()
# formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted)

# date_str ="2023-09-01 12:00:00"
# parsed = datetime.datetime.strptime(date_str,
# "%Y-%m-%d %H:%M:%S")
# print(parsed)

# birthday = datetime.date(1990, 5, 15)
# today = datetime.date.today()
# age = today.year - birthday.year - \
#         ((today.month, today.day) < (birthday.month, birthday.day))
# print("Возраст:", age)