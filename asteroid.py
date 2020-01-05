from game_objects import *

class Asteroid(GameObject):
    """"""

    def __init__(self, size, start_location_x, start_location_y):
        """"""
        self.__location_x = start_location_x
        self.__location_y = start_location_y
        self.__speed_x = 0
        self.__speed_y = 0
        if 1 <= size <= 3:
            self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
         self.__size = new_size


