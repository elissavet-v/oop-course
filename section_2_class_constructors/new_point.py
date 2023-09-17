"""Code to show how the instantiation process works internally.
Not something you would do in real code!"""


class Point:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    """
    return creates new Point instance by calling the Parent class'
    .__new__() method with cls as an argument.
    Object is the parent class Point
    The call to super gives you access to it.
    Then the instance is returned and will be the self argument to .__init__()
    """

    def __init__(self, x, y):
        """
        self holds reference to the current instance we just returned
        from __new__()
        """

        print("2. Initialise the new instance of Point. ")
        self.x = x
        self.y = y
        """These lines print a message when __init__() runs the 
        object initialization step and then initialize the .x and .y 
        attributes
        How do they do this? They use the provided input args x and y"""

    def __repr__(self):
        """Provides a proper string representation for the Point class"""
        return f"{type(self).__name__}(x={self.x}, y={self.y})"


# p1 = Point(3, 2)
# print(p1)
# print(type(p1))
# print(p1.__repr__())
"""Pass the class itself as the first argument to the method __new__()"""
p2 = Point.__new__(Point)
"""If we call that, we run only the first step of the instatiation,
creating a new and empty object"""
p2
"""We can then initialize the class object by calling __init__ with
the right args"""
p2.__init__(2, 3)
p2
p2.y
print(p2)
