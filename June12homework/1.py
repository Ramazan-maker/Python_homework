from random import randint
import math

class Car():

    Marka = ""
    Model = ""
    Color = ""
    Year = 0
    Speed = 0
    Mileage = 0
    Price = 0
    def __init__(self, Marka,Model,Color,Year):
        self.Marka = Marka
        self.Model = Model
        self.Color = Color 
        self.Year = Year
        self.Speed = randint(10,200)
        self.Mileage = randint(1000,300000)
        self.Price = randint(100000,999999)
    def show_info_car (self):
        info = f"""Марка:{self.Marka} и модель:{self.Model},
        Пробег:{self.Mileage},Год выпуска:{self.Year},
        Цена:{self.Price} тг
        """
        return info 
    #Виталий я взял этот кусок функции из интернета.Вычесление расстояние между городами
    def get_distance(self, lat1, lon1, lat2, lon2):
        # Преобразование координат в радианы
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Радиус Земли в километрах
        earth_radius = 6371

        # Разница между долготами и широтами
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad

        # Вычисление гаверсинуса половины разницы широт и долгот
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2

        # Вычисление расстояния
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = earth_radius * c

        return distance
    
    def drive(self,distance):
        self.Mileage += distance
        
    def get_speed(self):
        return self.Speed


    



my_car = Car('Toyota', 'Camry', 'Red', 2020)
distance = my_car.get_distance(43.238949, 76.889709, 51.1694, 71.4491)
speed = my_car.get_speed()
print(my_car.show_info_car())
print("Расстояние между городами:", distance, "км")
print("Скорость автомобиля:", speed, "км/час")
