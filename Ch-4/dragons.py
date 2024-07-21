
class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        """
        Check if the unit is within the specified rectangular area.

        Parameters:
        x_1, y_1: Coordinates of the bottom-left corner of the area.
        x_2, y_2: Coordinates of the top-right corner of the area.

        Returns:
        bool: True if the unit is within the area, False otherwise.
        """
        if (x_1 <= self.pos_x <= x_2) and (y_1 <= self.pos_y <= y_2):
            return True
        return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        """
        Simulate the dragon breathing fire at a specific point.

        Parameters:
        x, y: Coordinates of the target point where the dragon breathes fire.
        units: List of units to check if they are within the blast zone.

        Returns:
        list: List of units that are within the blast zone of the dragon's fire.
        """
        blast_zone = []

        # Calculate the rectangular area affected by the dragon's fire
        x_1 = x - self.__fire_range
        x_2 = x + self.__fire_range
        y_1 = y - self.__fire_range
        y_2 = y + self.__fire_range

        # Check each unit to see if it is within the blast zone
        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                blast_zone.append(unit)
        return blast_zone