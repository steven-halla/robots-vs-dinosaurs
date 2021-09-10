from fleet import Fleet
from herd import Herd

class BattleField:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def welcome_message(self):
        print("Hi welcome to the game")

    def battle(self):
        while len(self.fleet.robot_list) > 0 and len(self.herd.dinosaur_list) > 0:
            self.fleet.robot_list[0].attack(self.herd.dinosaur_list[0])
            print(self.fleet.robot_list[0].name + " robot attack over")
            self.herd.dinosaur_list[0].attack(self.fleet.robot_list[0])
            print(self.herd.dinosaur_list[0].name + " dinosaur attack over")
            if self.herd.dinosaur_list[0].health <= 0:
                print(self.fleet.robot_list[0].name + " robot wins the match")
                del self.herd.dinosaur_list[0]
            elif self.fleet.robot_list[0].health <= 0:
                print(self.herd.dinosaur_list[0].name + " dinosaur wins the match")
                del self.fleet.robot_list[0]
            else:
                print("battle on going")

    def battle_over(self):
        print("The battle is over")
        return





















# dinosaur1_is_alive = True
        # dinosaur2_is_alive = True
        # dinosaur3_is_alive = True
        # robot1_is_alive = True
        # robot2_is_alive = True
        # robot3_is_alive = True

        # if robot1.health <= 0:
        #     robot3_is_alive = False
        # if robot2.health <= 0:
        #     robot3_is_alive = False
        # if robot3.health <= 0:
        #     robot3_is_alive = False
        # if dinosaur1.health <= 0:
        #     robot3_is_alive = False
        # if dinosaur2.health <= 0:
        #     robot3_is_alive = False
        # if dinosaur3.health <= 0:
        #     robot3_is_alive = False















