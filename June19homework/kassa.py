from ticket import Ticket

class Kassa:
    balance = 0
    tickets = []
    trains = []

    def get_price(self, source, destination):
        price = (len(source) + len(destination))*1000
        return price

    def buy_ticket(self, passenger, source, destination):
        for train in self.trains:
            if train.source == source and train.destination == destination:
                money = passenger.pay(self.get_price(source, destination))
                if money > 0:
                    self.balance += money
                    ticket = Ticket(train.number, source, destination, train.datetime, passenger)
                    self.tickets.append(ticket)
                    return True
        return False

    def get_ticket(self, passenger, train_number, datetime):
        for x in self.tickets:
            if x.passenger.iin == passenger.iin and x.train_id == train_number and x.datetime == datetime:
                return x

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)

    def register_train(self, train):
        self.trains.append(train)


if __name__ == "__main__":
    print("Kassa")
