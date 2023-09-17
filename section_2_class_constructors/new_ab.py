"""Code to show that .__new__() can return an
instance of a class different to the class that 
implements the method itself, without initializing it.
When that happens, Python doesn't call __init__ on the 
current class"""

"""The __new__ method of class B returns an instance of class A"""


class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A")
        self.a_value = a_value


class B:
    def __new__(cls, *args, **kwargs):
        print("Create and return new instance of B")
        return A(3)

    def __init__(self, b_value):
        print("Initialize the new instance of B class")
        self.b_value = b_value
        """B.__init__() never runs because you told it in __new__
        to return a new instance of A - so it goes back to A and runs
        that __init__ instead"""


b = B(1)
# b.b_value
b.a_value
print(isinstance(b, B))  # False
print(isinstance(b, A))  # True
