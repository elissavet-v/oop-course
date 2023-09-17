class Enemy:
    def __init__(self, name, health, power_level):
        self.name = name
        self.health = health
        self.power_level = power_level

    def attack(self):
        print(f"The enemy {self.name} attacks!")

    def take_damage(self):
        self.health -= 10
        print(
            f"The enemy {self.name} took damage and their health is now at {self.health}"
        )

    def defeat(self):
        self.power_level -= 20
        print(
            f"The enemy {self.name} has reached power level {self.power_level} and are now defeated!"
        )


enemy_1 = Enemy("Hydra", 100, 10)  # instantiating the class
enemy_1.attack()
enemy_1.take_damage()
enemy_1.defeat()
