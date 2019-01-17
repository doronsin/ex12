PLAYER_2_COLOR = 'Red'
PLAYER_1_COLOR = 'Blue'


class Disc:
    """
    this class represents one disc in the game
    """

    def __init__(self, player, coordination):
        """
        ctor for the class
        :param player: the number of the player that owns the disc
        :param coordination: the place of the disc on the board
        """
        self.__player = player
        self.__coordination = coordination
        if player == 1:
            self.__color = PLAYER_1_COLOR
        else:
            self.__color = PLAYER_2_COLOR

    def set_player(self, player):
        """
        setter for player
        :param player: the new player number
        """
        self.__player = player

    def set_coordination(self, coordination):
        """
        setter for the place of the disc
        :param coordination: the new place
        """
        self.__coordination = coordination

    def get_coordination(self):
        """
        getter for the place
        :return: the place of the sice
        """
        return self.__coordination
    
    def get_player(self):
        """
        getter for the player number
        :return: the player number
        """
        return self.__player
    
    def get_color(self):
        """
        getter for the disc color
        :return: the disc color
        """
        return self.__color

    def __eq__(self, other):
        """
        function to compare between two discs
        :param other: the other disc to compare to
        :return: return True if the discs belongs to the same player, false otherwise
        """
        if other is None:
            return False
        return self.get_player()==other.get_player()

