'''
this calss conects between Game and Gui.
'''
from .disc import Disc

class GameRunner:

    def __init__(self, game):

        self.__game = game

    def one_turn(self, col_selection, cur_player):
        '''
        Responsible for operating one turn in the game
        :param col_selection:
        :param cur_player:
        :return:
        '''
        cur_player = cur_player
        disc = Disc(cur_player, (0, 0))
        try:
            if self.__game.make_move(col_selection, disc):
                self.__game.change_player(cur_player)
                return disc
        except Exception as e:
            return False

    def check_if_win(self):
        winner =  self.__game.get_winner()
        if winner:
            return winner
        return False

    def is_board_full(self):
        board_ind = self.__game.get_board().board_is_full()
        if board_ind:
            return True
        return board_ind

    def get_cur_player(self):
        return self.__game.get_current_player()

    def change_player(self, cur_player):
        return self.__game.change_player(cur_player)











