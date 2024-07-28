class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        """
        Craft two swords together to create a new sword.
        
        :param other: Another Sword instance to be combined with.
        :return: A new Sword instance of the resulting type after crafting.
        :raises Exception: If the swords cannot be crafted together.
        """
        if self.sword_type == 'bronze' and other.sword_type == 'bronze': 
            return Sword('iron')

        elif self.sword_type == 'iron' and other.sword_type == 'iron': 
            return Sword('steel')
        
        else:
            # Any other combination cannot be crafted
            raise Exception("can not craft")