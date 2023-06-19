class Film:
    def __init__(self, title, director, genre, duration, year):
        self.title = title
        self.director = director
        self.genre = genre
        self.duration = duration
        self.year = year
        self.playing = False

    def play(self):
        self.playing = True
        print(f"Фильм '{self.title}' начал проигрываться.")

    def pause(self):
        self.playing = False
        print(f"Фильм '{self.title}' приостановлен.")

    def rewind(self, minutes):
        print(f"Перемотка фильма '{self.title}' на {minutes} минут.")

    def display_info(self):
        print(f"Информация о фильме:")
        print(f"Название: {self.title}")
        print(f"Режиссер: {self.director}")
        print(f"Жанр: {self.genre}")
        print(f"Продолжительность: {self.duration} минут")
        print(f"Год выпуска: {self.year}")

film = Film("Oppenheimer", "Кристофер Нолан", "Документальный", 220, 2023)

# Вызов методов класса "Фильм"
film.play()
film.pause()
film.rewind(10)
film.display_info()