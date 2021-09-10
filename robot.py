from weapon import AutoCannons


class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = AutoCannons()
        self.health = 100

    def attack(self, dinosaur):
        self.weapon.attack(dinosaur)
