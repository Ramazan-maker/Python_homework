from order import Order
from datetime import datetime, timedelta

class Room:
    number = 0
    bedrooms = 0
    order: Order = None
    def __init__(self, number):
        self.number = number
        self.bedrooms = 2 if number % 2 == 0 else 1
        self.order = None

    def is_empty(self, date=None):
        if date is None:
            date = datetime.now().date()
        if self.order is None:
            return True
        return not (self.order.date_from <= date <= self.order.date_to)

    def show_info(self):
        info = f"""Комната: {self.number}
        Кровати: {self.bedrooms}
        Пусто: {self.is_empty()}"""
        print(info)







