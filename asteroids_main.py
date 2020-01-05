from screen import Screen
import sys
from numpy import *
import random
import ship
import asteroid
import torpedo


DEFAULT_ASTEROIDS_NUM = 5
ITEMS_TYPE = [ship, asteroid, torpedo]
SCREEN_MIN_X = Screen.SCREEN_MIN_X
SCREEN_MIN_Y = Screen.SCREEN_MIN_Y
SCREEN_MAX_X = Screen.SCREEN_MAX_X
SCREEN_MAX_Y = Screen.SCREEN_MAX_Y


class GameRunner:

    def __init__(self, asteroids_amount):

        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__items_on_screen = {}
        self.__ship = self.create_ship()

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        self.__screen.draw_ship(self.__ship.get_location_x(), self.__ship.get_location_y(),
                                self.__ship.get_direction())
        self.change_ship_direction()
        self.accelerate_ship()
        self.move_object(self.__ship)


    def add_item(self, item):
        """"""
        if type(item) == ship.Ship:
            self.__items_on_screen["ship"] = item


    def get_screen(self):
        return self.__screen


    def create_ship(self):

        x, y = self.get_location_on_screen()
        my_ship = ship.Ship(x, y)
        return my_ship

    def move_object(self,object):
        """

        :param object:
        :return: the new location of a given object according to the formula
        """

        min_x = self.__screen_min_x
        max_x = self.__screen_max_x
        min_y = self.__screen_min_y
        max_y = self.__screen_max_y

        location_x = object.get_location_x()
        location_y = object.get_location_y()
        speed_x = object.get_speed_x()
        speed_y = object.get_speed_y()

        new_spot_x = min_x + (location_x + speed_x - min_x) % (max_x - min_x)
        new_spot_y = min_y + (location_y + speed_y - min_y) % (max_y - min_y)

        object.set_location_x(new_spot_x)
        object.set_location_y(new_spot_y)

    def change_ship_direction(self):

        """

        :return: the function changes the direction of the ship
        """

        if self.get_screen().is_left_pressed():
            new_direction = self.__ship.get_direction()+7
            self.__ship.set_direction(new_direction)

        elif self.get_screen().is_right_pressed():
            new_direction = self.__ship.get_direction()-7
            self.__ship.set_direction(new_direction)


    def accelerate_ship(self):
        """

        :return: accelerate the ship acorrding to the formula if "up" was pressed by the user
        """

        heading = math.radians(self.__ship.get_direction())

        if self.get_screen().is_up_pressed():
            new_speed_x = self.__ship.get_speed_x() + cos(heading)
            new_speed_y = self.__ship.get_speed_y() + sin(heading)
            self.__ship.set_speed_x(new_speed_x)
            self.__ship.set_speed_y(new_speed_y)


    def get_location_on_screen(self):

        """"""
        item_location_x = random.randint(SCREEN_MIN_X, SCREEN_MAX_X)
        item_location_y = random.randint(SCREEN_MIN_Y, SCREEN_MAX_Y)
        return item_location_x, item_location_y


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)

