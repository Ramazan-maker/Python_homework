from random import randint

class Train:
    
    def __init__ (self, kassa, source, destination, datetime):
        self.source = source 
        self.destination = destination
        self.datetime = datetime
        self.number = randint(1, 100)
        self.kassa = kassa
        kassa.register_train(self)
    def go(self, passenger):
        ticket = self.kassa.get_ticket(passenger, self.number, self.datetime)
        if ticket:
            print(f'Вы поехали из {self.source} в {self.destination}\nПриехали')
            self.kassa.delete_ticket(ticket)
        else:
            print(f"У вас нет билета на поезд из {self.source} в {self.destination}")

    def __sub__(self, other):
        if isinstance(other, Train):
            return len(self.destination) - len(other.source)


            
if __name__ == "__main__":
    print("Train")