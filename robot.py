from weapon import Weapon, Auto_Cannons

class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = Auto_Cannons()
        self.health = 100

    def attack(self, dinosaur):
        self.weapon.attack(dinosaur)







