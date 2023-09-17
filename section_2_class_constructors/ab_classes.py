class A:
    def __init__(self, a_value):
        print("Initialise the new instance of A.")
        self.a_value = a_value


class B:
    def __new__(cls, *args, **kwargs):
        return A(42) 

    # the init code is never going to run
    def __init__(self, b_value):
        print("Initialise the new instance of B.")
        self.b_value = b_value

 

# best to run this in bpython in the same folder as this class.

a = A(7)
b = B(21)
print(b.a_value)

 