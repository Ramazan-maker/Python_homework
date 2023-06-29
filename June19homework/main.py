from person import Person
from train import Train
from kassa import Kassa
from ticket import Ticket

if __name__ == "__main__":

    dude = Person("Ilon", "Kask", "1994-06-25")
    dude.earn(25000)
    dude.pay(3500)
    dude.show_info()
    #случай, где получается купить билет на подходящий поезд
    tmp_ticket = Ticket(23, "Алматы", "Ташкент", "2023-06-16 07:59", dude)
    tmp_ticket.show()
    kassa = Kassa()
    tmp_train = Train("Астана", "Шымкент", "2023-06-16 20:00",kassa)
    kassa.buy_ticket(dude, "Астана", "Шымкент", tmp_train)
    # VN:            надо убрать этот аргумент ^^^^^^^^^^
    tmp_train.go(dude)


    #* случай, где нет подходящего поезда и билет купить нельзя
    tmp_train1 = Train("Астана", "Шымкент", "2023-06-16 20:00",kassa)
    if not kassa.buy_ticket(dude, "Алматы", "Ташкент", tmp_train1):
        print("Билет недоступен")
    tmp_train1.go(dude)

    print("Ниже магический метод:")
    dude5 = Person("Jonh", "Doe", "1994-06-25")
    print(dude5)  # Вывод: Person: Jonh Doe

    tmp_ticket3 = Ticket(23, "Алматы", "Ташкент", "2023-06-16 07:59", dude5)
    print(repr(tmp_ticket3))  # Вывод: Ticket(train_id=23, source=Алматы, destination=Ташкент)

    tmp_train3 = Train("Алматы", "Шымкент", "2023-06-16 20:00",kassa)
    print(repr(tmp_train3))  # Вывод: Train(source=Алматы, destination=Шымкент, datetime=2023-06-16 20:00, number=<случайное число>)
else:
    print(__name__)