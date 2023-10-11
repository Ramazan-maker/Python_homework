# def get_day_name(day):
#     match day:
#         case 1: print('Monday')
#         case 2: return 'Tuesday'
#         case 3: return 'Wednesday'
#         case 4: return 'Thursday'
#         case 5: return 'Friday'
#         case 6: return 'Saturday'
#         case 7: return 'Sunday'
#         case _: return 'Error'
#
#
# result = get_day_name(1)
#
# print(result)


# data = [1,2,3]
# match data:
#     case [x, y] : print(f"Список из {x} и {y}")
#     case (x, y, z): print(f"Кортеж из {x}, {y} и {z}")
#     case _: print("Неизвестная последовательность")
#
# point = [1,2]

# match point:
#     case (x, y) if x > 0 and y > 0:
#         print(f"Точка в первом квадранте: x={x}, y={y}")
#     case (x, y) if x < 0 and y > 0:
#         print(f"Точка во втором квадранте: x={x}, y={y}")
#     case _:
#         print("Точка не в первом и не втором квадранте")

# data = {"name": "Ramazan", "age": 19}
#
# match data:
#     case {"name": str, "age": int}:
#         print("Словарь с ключами 'name' и 'age'")
#     case _: print("Неизвестный словарь")
# value = 2
#
# match value:
#     case 0 | 1: print("Ноль или один")
#     case 2 | 3 | 4: print("Два, три или четыре")
#     case _: print("Другое число")
# value = 1
#
# match value:
#     case 0: "zero"
#     case x if x > 0: "positive"
#     case x if x < 0: "negative"
#     case _: "other"
#не работает
