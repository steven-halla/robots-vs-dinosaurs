from robot import Robot


class Fleet:
    def __init__(self):
        self.robot_list = []
        self.build_robots()

    def build_robots(self):
        robot1 = Robot("devastator")
        robot2 = Robot("ripper")
        robot3 = Robot("incinerator")

        self.robot_list.append(robot1)
        self.robot_list.append(robot2)
        self.robot_list.append(robot3)



