from random import randint

class Person:
    balance = 0
    iin = 0
    birth_date = ""
    first_name = ""
    last_name = ""
    # ticket = False

    def __init__(self, name, last_name, birth_date):
        self.first_name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.iin = randint(100000000000, 999999999999)

    def show_info(self):
        info = f"""Person: {self.first_name} {self.last_name},
        Date of Birth: {self.birth_date},
        IIN: {self.iin}, Balance: {self.balance}"""
        print(info)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        return 0

    #Magical metod
  
    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}"
    """
    __str__, который будет возвращать строковое представление объекта Person при вызове функции str() или при преобразовании объекта в строку.
    """
if __name__ == "__main__":
    print("Person")
# else :
#     print(__name__)