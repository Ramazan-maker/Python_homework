from order import Order
from room import Room

class Hotel:
    def __init__(self, name, balance, rooms):
        self.name = name
        self.balance = balance
        self.rooms = rooms

    def get_price(self, room_number, date_from, date_to):
        for room in self.rooms:
            if room.number == room_number:
                return room.price * (date_to - date_from).days
        return None

    def buy_order(self, date_from, date_to, visitor):
        for room in self.rooms:
            if not any(
                    [
                        date_from < order.date_from < date_to or date_from < order.date_to < date_to
                        for order in room.orders
                    ]
            ):
                room.orders.append(Order(self.name, room.number, date_from, date_to))
                return True
        return False

    def check_in(self, visitor, date):
        for room in self.rooms:
            for order in room.orders:
                if order[0] == visitor and order[1] <= date <= order[2]:
                    room.orders.remove(order)
                    return True
        return False

    def check_out(self, visitor, date):
        for room in self.rooms:
            for order in room.orders:
                if order[0] == visitor and order[2] < date:
                    days_stayed = (date - order[2]).days
                    cost = days_stayed * room.price
                    if cost > 0 and cost <= visitor.balance:
                        visitor.balance -= cost
                        self.balance += cost
                        return True
        return False
