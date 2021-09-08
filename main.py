from dinosaur import Dinosaur
from robot import Robot

devastator = Robot("devastator")
print(devastator.name)
print(devastator.weapon.attack_power)
print(devastator.weapon.name)
print(devastator.health)

raptor = Dinosaur("raptor", 10)
print(raptor.name)
print(raptor.attack_power)
print(raptor.health)