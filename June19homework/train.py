from random import randint
from ticket import Ticket
from kassa import Kassa

class Train:
    
 
    def __init__(self, source, destination, datatime, kassa):
        self.source = source
        self.destination = destination
        self.datatime = datatime
        self.number = randint(1, 100)
        self.kassa = kassa  # Сохранение экземпляра kassa как атрибута класса
        self.kassa.register_train(self)  # Использование атрибута kassa для вызова метода register_train()

    def go(self, passenger):
        if passenger.ticket:
            if passenger.ticket.datetime == self.datatime and \
                passenger.ticket.train_id == self.number:
                print(f"Вы поехали из {self.source} в {self.destination}")
                print("Вы приехали")
                passenger.ticket = False
            else:
                print("У вас нет билета на этот поезд!")
        else:
            print("У вас нет билета")

    #Magical metod
    def __repr__(self):
        return f"Train(source={self.source}, destination={self.destination}, datetime={self.datatime}, number={self.number})"

if __name__ == "__main__":
    print("Train")