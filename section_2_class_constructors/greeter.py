class Greeter:
    """To showcase default arguments"""

    def __init__(self, name, formal=False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Good morning, {self.name}!")
        else:
            print(f"Hello, {self.name}")


informal_greeter = Greeter("Eli")
informal_greeter.greet()
formal_greet = Greeter("Elissavet")
formal_greet = Greeter("Elissavet", formal=True)
formal_greet.greet()
