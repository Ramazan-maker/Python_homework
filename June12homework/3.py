class Weather:
    today = ""

    def __init__(self, temperature, humidity, wind_speed, precipitation_type, cloudiness):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.precipitation_type = precipitation_type
        self.cloudiness = cloudiness

    def get_current_weather(self):
        print("Текущая погода:")
        print(f"Температура: {self.temperature}°C")
        print(f"Влажность: {self.humidity}%")
        print(f"Скорость ветра: {self.wind_speed} м/с")
        print(f"Тип осадков: {self.precipitation_type}")
        print(f"Облачность: {self.cloudiness}%")

    def get_forecast(self, days):
        print(f"Прогноз погоды на следующие {days} дней:")
        #  код для получения прогноза на несколько дней
        forecast = []
        

        #Если сегодня погода была дождливой ,завтра она будет облачной а след. два дня будут солнечными 
        #и наоборот Если солнечно то облачно и два дня дождливо 
        #проверка текущей погоды и генерация прогноза на основе условий
        if self.precipitation_type == "Дождь":
            forecast = ["Облачно"] + ["Солнечно"] * (days - 1)
        elif self.precipitation_type == "Солнечно":
            forecast = ["Облачно"] + ["Дождь"] * (days - 1)
        elif self.cloudiness == "Облачно":
            forecast = ["Дождь"] + ["Солнечно"] * (days - 1)
        for i in range(days):
            print(f"День {i + 1}: {forecast[i]}")

        return forecast
    def check_danger_level(self):
        #  код для проверки степени опасности погоды
        if self.precipitation_type == "Дождь" and self.wind_speed > 20:
            return "Опасно! Намечается торнадо или ветер, который сдувает все."
        elif self.precipitation_type == "Солнечно" and self.temperature > 50:
            return "Опасно! Не выходите из дома, на улице сильно жарко, возможна засуха."
        else:
            return "Опасности нет, все хорошо."  
weather= Weather(25, 80, 5,"Дождь",50 )
danger_level = weather.check_danger_level()

# Вызов методов класса "Погода"
weather.get_current_weather()
weather.get_forecast(3)
weather.check_danger_level()
print(danger_level)