from random import randint
from person import Person

class Order ():

    def __init__(self, hotel_name, room, date_from, date_to):
        self.hotel_name = hotel_name
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.id = randint(100000, 999999)
        self.visitor_name = ""
        self.visitor_iin = ""


    def get_visitor_full_name(self,person):
        self.visitor_name = f"{person.first_name} {person.last_name}"
        self.visitor_iin = person.iin
    def show_info(self):
        info = f"""
        Имя посетителя: {self.visitor_name},
        ИИН постетителя: {self.visitor_iin},
        Айди: {self.id},
        Комната: {self.room},
        Дата въезда: {self.date_from},
        Дата выезда: {self.date_to},
        Имя отела: {self.hotel_name}
        """
        print(info)



