from game_objects import *


class Torpedo(GameObject):
    """"""

    def __init__(self, location_x, location_y, speed_x=0, speed_y=0, direction=0):
        GameObject.__init__(self, location_x, location_y, speed_x, speed_y, direction)



