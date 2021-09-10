class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        # self.attack(robot)
        print("attack " + robot.name + " with " + self.name + " for " + str(self.attack_power) + " damage")
        robot.health -= self.attack_power
        print("robot hp " + str(robot.health))


# class Velociraptor(Dinosaur):
#     def __init__(self):
#         Dinosaur.__init__(self, "Velociraptor", 10, 20)
#
#
# class TyrannosaurusRex(Dinosaur):
#     def __init__(self):
#         Dinosaur.__init__(self, "Tyrannosaurus Rex", 20, 40)
