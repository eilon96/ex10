import numpy as np


class Torpedo:
    """"""

    def __init__(self, location_x, location_y, ship_speed_x, ship_speed_y, ship_direction):
        """"""
        self.__torpedo_location_x = location_x
        self.__torpedo_location_y = location_y
        self.__torpedo_speed_x = ship_speed_x+2*np.cos(ship_direction)
        self.__torpedo_speed_y = ship_speed_y+2*np.sin(ship_direction)
        self.__torpedo_direction = ship_direction
        self.__torpedo_life_time = 200
