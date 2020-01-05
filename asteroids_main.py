from screen import *
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

        import screen
        self.__screen = screen.Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__items_on_screen = {}

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
        # TODO: Your code goes here
        pass

    def add_item(self, item):
        """"""
        if type(item) == ship:
            self.__items_on_screen[ship] = item

    def get_screen(self):
        return self.__screen


def get_location_on_screen():

    """"""
    item_location_x = random.randint(SCREEN_MIN_X, SCREEN_MAX_X)
    item_location_y = random.randint(SCREEN_MIN_Y, SCREEN_MAX_Y)
    return item_location_x, item_location_y


def main(amount):
    runner = GameRunner(amount)
    x, y = get_location_on_screen()
    my_ship = ship.Ship(x, y)
    runner.get_screen().draw_ship(x,y,0)
    runner.add_item(my_ship)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM
    
