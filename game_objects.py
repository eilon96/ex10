class GameObject:

    def __init__(self, start_location_x, start_location_y,
                 speed_x=0, speed_y=0, direction=0):
        """"""
        self.__location_x = start_location_x
        self.__location_y = start_location_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__direction = direction

    def get_location_x(self):
        return self.__location_x

    def get_location_y(self):
        return self.__location_y

    def get_speed_x(self):
        return self.__speed_x

    def get_speed_y(self):
        return self.__speed_y

    def get_direction(self):
        return self.__direction

    def set_direction(self, new_direction):
        self.__direction = new_direction

    def set_speed_x(self, new_speed):
        self.__speed_x = new_speed

    def set_speed_y(self, new_speed):
        self.__speed_y = new_speed

    def set_location_x(self,new_location):
        self.__location_x = new_location

    def set_location_y(self,new_location):
        self.__location_y = new_location
