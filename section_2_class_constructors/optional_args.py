class Greeter:
    def __init__(self, name, formal=False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Greetings, {self.name}")
        else:
            print(f"hey {self.name}!")


g = Greeter("Eli", True)
g1 = Greeter("Eli", False)
print(g)
g.greet()
g1.greet()
