from random import randint
from person import Person

class Ticket:
    number = 0
    train_id = 0
    source = ""
    destination = ""
    wagon = 0
    seat = 0
    datetime = ""
    passenger: Person = False


    def __init__(self, train_id, source, destination, datetime, person):
        self.train_id = train_id
        self.source = source
        self.destination = destination
        self.datetime = datetime
        self.passenger = person
        self.number = randint(100000, 999999)
        self.wagon = randint(1, 12)
        self.seat = randint(1, 32)


    def __repr__(self):
        info = f"""Билет {self.number}:{self.source}-{self.destination}, № {self.train_id} в {self.datetime}"""
        return info

    def get_pricee(self):
        # Implement the method to calculate the price of the ticket based on source and destination
        price = (len(self.source) + len(self.destination)) * 1000
        return price



    def __mul__(self, other):
        if isinstance(other, int):
            # Вычисляем и возвращаем общую стоимость билетов с учетом количества вагонов
            return self.get_pricee() * self.wagon * other

if __name__ == "__main__":
    print("Ticket")
