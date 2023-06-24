from order import Order
import datetime

class Room():

    def __init__(self,number,bedrooms,order,capacity):
        self.number = order.room
        self.bedrooms = 2 if number % 2 == 0 else 1
        self.order = order
        self.capacity = capacity
    def is_empty(self):
        date_from = self.order.date_from
        date_to = self.order.date_to
        if date_from > self.order.date_to or date_to < self.order.date_from:
            return True
        return False






