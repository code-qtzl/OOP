class Rectangle:
    def overlaps(self, rect):
        # return (self.get_left_x() <= rect.get_right_x() and
        #         self.get_right_x() >= rect.get_left_x() and
        #         self.get_bottom_y() <= rect.get_top_y() and
        #         self.get_top_y() >= rect.get_bottom_y())


        # Check if the left side of this rectangle is on or to the left of the right side of the other rectangle
        left_side_check = self.get_left_x() <= rect.get_right_x()

        # Check if the right side of this rectangle is on or to the right of the left side of the other rectangle
        right_side_check = self.get_right_x() >= rect.get_left_x()

        # Check if the bottom side of this rectangle is on or below the top side of the other rectangle
        bottom_side_check = self.get_bottom_y() <= rect.get_top_y()

        # Check if the top side of this rectangle is on or above the bottom side of the other rectangle
        top_side_check = self.get_top_y() >= rect.get_bottom_y()

        # Return True if all the above conditions are true, meaning the rectangles overlap or touch
        return left_side_check and right_side_check and bottom_side_check and top_side_check

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
