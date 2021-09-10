class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        # self.attack(robot)
        print( " " +  self.name + " attacka " + robot.name + " for " + str(self.attack_power) + " damage")
        robot.health -= self.attack_power
        print("robot hp " + str(robot.health))



