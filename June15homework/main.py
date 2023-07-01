from person import Person
from order import Order
from room import Room
from hotel import Hotel
from datetime import datetime, timedelta

hotel = Hotel("Arcanus side resort", 100000, 10)

visitor1 = Person("Рамазан", "Сартаеы", "1991-11-11")
visitor1.earn(50000)

visitor2 = Person("Илон", "Маск", "198-06-14")
visitor2.earn(70000)

date_from = datetime.now().date()
date_to = date_from + timedelta(days=5)

order1 = hotel.buy_order(3, date_from, date_to, visitor1.first_name, visitor1.iin)
if order1:
    order1.show_info()
else:
    print("Не забронировна")

order2 = hotel.buy_order(8, date_from, date_to, visitor2.first_name, visitor2.iin)
if order2:
    order2.show_info()
else:
    print("Не забронировна")

room2 = hotel.rooms[1]
room2.show_info()

room8 = hotel.rooms[7]
room8.show_info()

date_check_in = date_from + timedelta(days=2)
date_check_out = date_to + timedelta(days=2)
hotel.check_in(visitor1, date_check_in)
hotel.check_out(visitor1, date_check_out)
hotel.check_out(visitor2, date_check_out)