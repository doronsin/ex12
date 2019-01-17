class Disc:

    def __init__(self, player, coordination):
        '''

        :param name:
        :param player:
        :param coordination: tuple(x,y)
        '''

        self.__player = player
        self.__coordination = coordination
        if player == 1:
            self.__color = 'Blue'
        else:
            self.__color = 'Red'

    def player(self, player):
        self.__player = player

    def set_coordination(self, coordination):
        self.__coordination = coordination

    def get_coordination(self):
        return self.__coordination
    
    def get_player(self):
        return self.__player
    
    def get_color(self):
        return self.__color

    def __eq__(self, other):
        if other is None:
            return False
        return self.get_player()==other.get_player()

