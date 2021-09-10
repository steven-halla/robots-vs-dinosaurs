from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaur_list = []
        self.train_dinosaurs()

    def train_dinosaurs(self):
        dinosaur1 = Dinosaur("trex", 30)
        dinosaur2 = Dinosaur("raptor", 10)
        dinosaur3 = Dinosaur("triceratops", 20)

        self.dinosaur_list.append(dinosaur1)
        self.dinosaur_list.append(dinosaur2)
        self.dinosaur_list.append(dinosaur3)