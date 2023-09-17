class Dog:
    treat = "dog biscuits!"
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        print(f"{self.name} barks: {sound}")

    def __str__(self):
        print(f"{self.name} is {self.age} years old")


class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


miles = JackRusselTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
print(jim.speak("hello"))

print(miles.speak())
print(miles.speak("grrrrr!!!"))
# print(miles.species)
# print(buddy.name)
# print(jack)
# print(jim.speak("Woof"))
# print(type(miles))
# print(isinstance(miles, Dog))

# dog1 = Dog("Mikey", 4)
# dog1.introduce_yourself()
# dog1.play("ball")
# dog1.age = 7  # I can change the object's attributes like this!
# dog1.treat = "PB!"
# dog1.introduce_yourself()
# print(dog1.treat)
# dog1.birthday()
# dog1.introduce_yourself()
# dog1.__str__()
