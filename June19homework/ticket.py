from random import randint
from person import Person
class Ticket:
    number = 0
    train_id = 0
    source = ""
    destination = ""
    seat = 0
    wagon = 0
    datetime = ""
    passenger: Person = False  # Initialize passenger attribute to None

    def __init__ (self, train_id, source, destination, datetime, person):
        self.train_id = train_id
        self.source = source
        self.destination = destination
        self.datetime = datetime
        self.passenger = person  # Assign the person object to passenger
        self.number = randint(100000, 999999)
        self.wagon = randint(1, 12)
        self.seat = randint(1, 32)

    def show(self):
        info = f"""Ticket number {self.number}:
        {self.source} - {self.destination},
        Departure: {self.datetime},
        Train ID: {self.train_id}, Wagon: {self.wagon}, Seat: {self.seat}
        Passenger: {self.passenger.first_name} {self.passenger.last_name},
        IIN: {self.passenger.iin}, Birth Date: {self.passenger.birth_date}"""
        print(info)
    #Magical metod
    def __repr__(self):
        return f"Ticket(train_id={self.train_id}, source={self.source}, destination={self.destination})"
    """
    В классе Ticket добавим метод __repr__, который будет возвращать официальное представление объекта Ticket при вызове функции repr().
    """
if __name__ == "__main__":
    print("Ticket")