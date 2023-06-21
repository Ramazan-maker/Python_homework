class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_booked = False
    
    def get_room_number(self):
        return self.room_number
    
    def get_capacity(self):
        return self.capacity
    
    def get_price_per_night(self):
        return self.price_per_night
    
    def is_available(self):
        return not self.is_booked
    
    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        else:
            return False
    
    def cancel_booking(self):
        if self.is_booked:
            self.is_booked = False
            return True
        else:
            return False
room = Room("101", 2, 100)

print("Room number:", room.get_room_number())
print("Capacity:", room.get_capacity())
print("Price per night:", room.get_price_per_night())
print("Is available:", room.is_available())

booked = room.book_room()
print("Booking successful:", booked)
print("Is available:", room.is_available())

canceled = room.cancel_booking()
print("Cancellation successful:", canceled)
print("Is available:", room.is_available())
