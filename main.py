import dinosaur
import robot
from dinosaur import Dinosaur
from robot import Robot
from battlefield import start_game

class game_start():
    def __init__(self):
        start_game()

game_start()
my_battle = start_game()

my_battle.welcome_message()
my_battle.battle()

# devastator = Robot("devastator")
# print(devastator.name)
# print(devastator.weapon.attack_power)
# print(devastator.weapon.name)
# print(devastator.health)
#
# raptor = Dinosaur("raptor", 10)
# print(raptor.name)
# print(raptor.attack_power)
# print(raptor.health)