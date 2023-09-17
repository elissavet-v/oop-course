import math


class Circle:
    def __init__(self, _radius):
        self.radius = _radius

    def _calculate_area(self):
        return round(math.pi * self.radius**2, 2)


circle_1 = Circle(2)
circle_2 = Circle(7)
circle_2.radius = 100  # assignment statement
print(circle_1.radius)
print(circle_2.radius)
print(circle_1._calculate_area())
print(circle_2._calculate_area())
