class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday


class Employee(Person):
    def __init__(self, name, birthday, position):
        super().__init__(name, birthday)
        self.position = position


j = Employee("Eli", "March 22nd 1988", "swe")
print(j.name)
