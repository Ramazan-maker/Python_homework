film_name = input("Введите название фильма: ")
cinema_name = input("Введите название кинотеатра: ")
time = input("Введите время: ")

ticket_message = "Билет на %s в %s на %s забронирован." % (film_name, cinema_name, time)
print(ticket_message)