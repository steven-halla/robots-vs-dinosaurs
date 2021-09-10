class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def attack(self, dinosaur):
        print( " Robot Attacks " + dinosaur.name + " with " + self.name + " for " + str(self.attack_power) + " damage")
        dinosaur.health -= self.attack_power
        print("dinosaur hp " + str(dinosaur.health))

class AutoCannons(Weapon):
    def __init__(self):
        Weapon.__init__(self, "auto cannons", 10)

    def attack(self, enemy):
        # add some special auto cannons behavior.
        Weapon.attack(self, enemy)

