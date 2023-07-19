class Animal:

    def __init__(self,name,weight,size):
        self.name = name
        self.weight = weight
        self.size = size

    def talk(self):
        print("Mmmmm......")

    def eat(self,meal):
        increase = len(meal)
        if increase == 0:
            print("Я голоден!")
        else:
            self.size += increase
            self.weight += increase
            print(f"Мой размер теперь - {self.size},а вес - {self.weight}")

class Herbivore(Animal):
    def __init__(self,name,weight,size):
        super().__init__(name,weight,size)
        self.ratio = ["мох", "ветки", "ягоды", "трава", "грибы"]
    
    def eat(self,meal):
        if meal in self.ratio:
            super().eat(meal)
        else:
            print('Это еда не мой рацион!')
class Predator(Animal):
    def __init__(self,name,weight,size):
        super().__init__(name,weight,size)
    
   

    def eat(self,meal):
        if meal.weight < self.weight and meal.size < self.size:
            increase = (meal.weight + meal.size )*0.20
            self.weight += increase
            self.size += increase
            print(f"Мой размер теперь - {self.size},а вес - {self.weight}")
        else:
            print("Я не могу его съесть")


class Goose(Herbivore):
    def __init__(self,name,weight,size):
        super().__init__(name,weight,size)

    def talk(self):
        print("Го-го-го")

    def kill(self, weight_limit):
        if self.weight > weight_limit:
            print("Гуся пустили на шашлык")
        else:
            print("Гусь жив здоров")
class Wolf(Predator):
    def __init__(self,name,weight,size,speed, victim):
        super().__init__(name,weight,size)
        self.speed = speed
        self.victim = victim
    def talk(self):
        print("Aууууууу-аууууууу")

    def set_speed(self,speed):
        if self.victim: 
            self.speed = speed + 0.25
        else:
            speed = 0 

herbivore = Goose('Goose',10,10)
predator = Wolf('Grey Wolf', 10, 10, 10, True)
herbivore.talk()
herbivore.eat('мох')
herbivore.kill(11)
predator.talk()
predator.eat(herbivore)
predator.set_speed(10)