from person import Person
from order import Order
from room import Room
from hotel import Hotel

person = Person("John", "Doe", "1990-01-01")
order = Order("Отель XYZ", "101", "2023-06-25", "2023-06-30")
order.get_visitor_full_name(person)  # Передаем объект person в качестве аргумента
order.show_info()




# Создание экземпляра класса Hotel
# VN: Здесь программа падает - не хватает ещё одного аргумента: capacity. См. конструктор класса Room
rooms = [
    Room(101, 2, order),  # Первая комната
    Room(102, 1, order),  # Вторая комната
    Room(103, 3, order),  # Третья комната
]
hotel = Hotel("Название гостиницы", 10000, rooms)

# Вызов метода get_price
room_number = 101
date_from = "2023-06-25"
date_to = "2023-06-30"
room_price = hotel.get_price(room_number, date_from, date_to)
print("Цена комнаты:", room_price)

# Вызов метода buy_order
visitor = person  # Предположим, что объект person представляет посетителя гостиницы
order_success = hotel.buy_order(date_from, date_to, visitor)
if order_success:
    print("Бронирование успешно")
else:
    print("Не удалось забронировать комнату")



# Вызов метода check_in
check_in_success = hotel.check_in(visitor, date)
# VN:               этой переменной нет:   ^^^^  , и программа здесь падает
if check_in_success:
    print("Заселение успешно")
else:
    print("Не удалось заселиться в отель")

# Вызов метода check_out
check_out_success = hotel.check_out(visitor,date)
if check_out_success:
    print("Выселение успешно")
else:
    print("Не удалось выселиться из отеля")

room = Room(101, 2, order)
is_empty = room.is_empty()  # Проверяем, свободна ли комната сегодня
print(is_empty)  # Выводим результат