from random import randint
class Order:
    id=0
    def __init__(self,hotel_name,room,date_from,date_to,visitor_name,visitor_iin):
        self.hotel_name = hotel_name
        self.id = randint(100000,999999)
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name
        self.visitor_iin = visitor_iin
        self.is_canceled = False
        self.is_checked_in = False
        self.is_checked_out = False
    
    def show_info(self):
        info = f"""
        Name:{self.visitor_name}
        IIN:{self.visitor_iin}
        Hotel name:{self.hotel_name},
        Room:{self.room}
        Date from:{self.date_from}
        Date To:{self.date_to}
        """
        return info

    def update_dates(self, new_date_from, new_date_to):
        self.date_from = new_date_from
        self.date_to = new_date_to

    def change_room(self, new_room):
        self.room = new_room
    def check_in(self):
        self.is_checked_in = True

    def check_out(self):
        self.is_checked_out = True
    
order = Order("Отель XYZ", "101", "2023-06-25", "2023-06-30", "Иван Иванов", "123456789012")
print(order.show_info())
order.update_dates("2023-07-01", "2023-07-05")
print("Новые даты заезда и выезда:", order.date_from, order.date_to)

# Изменение номера комнаты
order.change_room("202")
print("Новый номер комнаты:", order.room)

# Заселение
order.check_in()
print("Статус заселения:", order.is_checked_in)

# Выселение
order.check_out()
print("Статус выселения:", order.is_checked_out)