
from ticket import Ticket


class Kassa:
    kassa_balance = 0
    trains = []
    
    def get_price(self, source, destination):
        price = (len(source) + len(destination)) * 1000
        return price
    
    def buy_ticket(self, passenger, source, destination, train):
        # VN:        из метода надо убрать этот аргумент ^^^^^
        # И тогда в первую очередь нужно перебрать все self.trains, и продавать билет
        # только если подходящий поезд из source в destination нашёлся в списке 
        money = passenger.pay(self.get_price(source, destination))
        if money > 0:
            self.kassa_balance += money
            ticket = Ticket(train.number, source, destination, train.datatime, passenger)
            passenger.ticket = ticket
            return True
        else:
            return False
    def register_train(self, train):
        self.trains.append(train)
if __name__ == "__main__":
    print("Kassa")