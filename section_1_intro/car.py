class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


car_1 = Car("blue", 20000)
car_2 = Car("red", 30000)
print(car_1.__str__())
print(car_2.__str__())
