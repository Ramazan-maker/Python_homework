from person import Person
from train import Train
from kassa import Kassa
from ticket import Ticket

if __name__ == "__main__":
    dude = Person("Ilon", "Kask", "1994-06-25")
    dude.earn(25000)
    dude.show_info()

    alex = Person("Alex", "Boldwin", "1954-06-25")
    alex.earn(95000)  # Маг метод
    alex.show_info()

    kassa = Kassa()
    train_to_chile = Train(kassa, 'Алматы', "Сантьяго", '2023-06-16 20:00')
    train_to_uruguay = Train(kassa, 'Алматы', "Монтевидео", '2023-06-26 09:00')

    kassa.buy_ticket(dude, 'Алматы', 'Сантьяго')
    kassa.buy_ticket(dude, 'Алматы', 'Монтевидео')

    kassa.buy_ticket(alex, 'Алматы', 'Сантьяго')
    kassa.buy_ticket(alex, 'Алматы', 'Норильск')

    print(kassa.tickets)
    train_to_chile.go(dude)
    print(kassa.tickets)
    kassa.buy_ticket(dude, 'Алматы', 'Нью-Йорк')

    train_diff = train_to_chile.__sub__(train_to_uruguay)  # маг метод
    print(f"Расстояние от Алматы до Сантяьго: {train_diff} км")
    train_diff = train_to_uruguay.__sub__(train_to_chile)
    print(f"Расстояние от Алматы до Монтевидео: {train_diff} км")

    ticket = Ticket(86, 'Алматы', 'Монтевидео', '2023-06-26 09:00', alex)
    result = ticket.__mul__(3)  # маг  метод
    print(f"Стоимость билета с учетом количества вагонов: {result} тг")
