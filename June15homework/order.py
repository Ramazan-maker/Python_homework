from random import randint
from person import Person

class Order ():

    hotel_name = ""
    id = 0
    room = 0
    date_from = 0
    date_to = 0
    visitor_name = ""
    visitor_iin = 0

    def __init__(self, hotel_name, room, date_from, date_to, visitor_name, visitor_iin):
        self.hotel_name = hotel_name
        self.id = randint(100000, 999999)
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name
        self.visitor_iin = visitor_iin

    def show_info(self):
        info = f""" Бронь: {self.id}
        Отель: {self.hotel_name}
        Комната: {self.room.number}
        Дата заезда: {self.date_from}
        Дата выезда: {self.date_to}
        Посетитель: {self.visitor_name}
        ИИН: {self.visitor_iin}"""
        print(info)



