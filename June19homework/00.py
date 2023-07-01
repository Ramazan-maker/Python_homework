from random import randint

class Person:
    balance = 0
    iin = 0
    birth_date = ""
    first_name = ""
    last_name = ""
    ticket = False

    def __init__(self, name, last_name, birth_date):
        self.first_name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.iin = randint(100000000000, 999999999999)

    def show_info(self):
        info = f"""Person: {self.first_name} {self.last_name},
        Date of Birth: {self.birth_date},
        IIN: {self.iin}, Balance: {self.balance}"""
        print(info)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        return 0
    
class Ticket:
    number = 0
    train_id = 0
    source = ""
    destination = ""
    seat = 0
    wagon = 0
    datetime = ""
    passenger = None  # Initialize passenger attribute to None

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

class Kassa:
    kassa_balance = 0
    trains = []
    
    def get_price(self, source, destination):
        price = (len(source) + len(destination)) * 1000
        return price
    
    def buy_ticket(self, passenger, source, destination, train):
        money = passenger.pay(self.get_price(source, destination))
        if money > 0:
            self.kassa_balance += money
            ticket = Ticket(train.number, source, destination, train.datatime, passenger)
            passenger.ticket = ticket
            return True
        else:
            return False
    
class Train:
    source = None 
    destination = None 
    datatime = None
    number = None 

    def __init__ (self, source, destination, datatime):
        self.source = source 
        self.destination = destination
        self.datatime = datatime
        self.number = randint(1, 100)
        
    def go(self, passenger):
        if passenger.ticket.datetime == self.datatime and passenger.ticket.destination == self.destination:
            print(f"Вы поехали из {self.source} в {self.destination}")
            passenger.ticket = False
        else:
            print("У вас нет билета на этот поезд!")

dude = Person("Ilon", "Kask", "1994-06-25")
dude.earn(25000)
dude.pay(3500)
dude.show_info()

tmp_ticket = Ticket(23, "Алматы", "Ташкент", "2023-06-16 07:59", dude)
tmp_ticket.show()

kassa = Kassa()

tmp_train = Train("Алматы", "Шымкент", "2023-06-16 20:00")
kassa.buy_ticket(dude, "Алматы", "Шымкент", tmp_train)
tmp_train.go(dude)

