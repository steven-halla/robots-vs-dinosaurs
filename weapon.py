class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def attack(self, dinosaur):
        print("attack " + dinosaur.name + " with " + self.name + " for " + str(self.attack_power) + " damage")
        dinosaur.health -= self.attack_power
        print("enemy hp " + str(dinosaur.health))


class Auto_Cannons(Weapon):
    def __init__(self):
        Weapon.__init__(self, "auto cannons", 10)

    def attack(self, enemy):
        print("robot looks at you and shoots his weapon")
        # add some special auto cannons behavior.
        Weapon.attack(self, enemy)


# class Flame_thrower(Weapon):
#     def __init__(self):
#         Weapon.__init__(self, "flame thrower", 10)
#
#     def attack(self, enemy):
#         print("robot shoots his flames")
#
#         Weapon.attack(self, enemy)
