class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.__pos_x += self.__speed * 2
        self.__use_sprint_stamina()

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__pos_x -= self.__speed * 2
        self.__use_sprint_stamina()

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__pos_y += self.__speed * 2
        self.__use_sprint_stamina()

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__pos_y -= self.__speed * 2
        self.__use_sprint_stamina()

    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception('not enough stamina to sprint')

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina
