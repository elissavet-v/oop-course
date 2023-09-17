class Point:

    """Created to uncover how the instantation process works in practice"""

    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")

        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialise the new instance of Point.")

        self.x = x

        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}), y={self.y} "


point = Point(21, 42)

""" Calling the Point class constructor creates,
initialises, and returns a new instance of the class.
This instance is then assigned to the variable point"""


Point(21, 42)
