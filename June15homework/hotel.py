from order import Order
from room import Room

class Hotel:
    name = ""
    balance = 0
    
    def __init__(self, name, balance, num_rooms):
        self.name = name
        self.balance = balance
        self.rooms = [Room(i) for i in range(1, num_rooms + 1)]

    def get_price(self, room_number, date_from, date_to):
        room = self.rooms[room_number - 1]
        return room.bedrooms * (date_to - date_from).days * 1000

    def buy_order(self, room_number, date_from, date_to, visitor_name, visitor_iin):
        room = self.rooms[room_number - 1]
        price = self.get_price(room_number, date_from, date_to)
        if self.balance >= price and room.is_empty(date_from):
            self.balance -= price
            order = Order(self.name, room, date_from, date_to, visitor_name, visitor_iin)
            room.order = order
            return order
        return None

    def check_in(self, visitor, date):
        if visitor.order is not None and visitor.order.date_from <= date <= visitor.order.date_to:
            print(f"{visitor.first_name} {visitor.last_name} заселился.")
        else:
            print(f"{visitor.first_name} {visitor.last_name} у него нет бронирования на эту дату.")

    def check_out(self, visitor, date):
        if visitor.order is None or visitor.order.date_to < date:
            print(f"{visitor.first_name} {visitor.last_name} нет активного бронирования")
            return

        extra_days = (date - visitor.order.date_to).days
        if extra_days > 0:
            price_per_day = visitor.order.room.bedrooms * 1000
            additional_price = extra_days * price_per_day
            self.balance += additional_price
            print(f"{visitor.first_name} {visitor.last_name}  выслился. Дополнительная оплата: {additional_price}.")
        else:
            print(f"{visitor.first_name} {visitor.last_name}  выселился.")
