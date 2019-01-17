from .disc import Disc


class GameRunner:
    """
    this class responsible to connect between the game and the gui (the "controller" in the mvc)
    """
    def __init__(self, game):
        """
        the ctor of the class
        :param game: the game object
        """
        self.__game = game

    def one_turn(self, col_selection):
        """
        Responsible for operating one turn in the game
        :param col_selection: the selection of the player
        :param cur_player: the current player who is playing
        :return: False if there is an exception, the disc if the move worked, None otherwise
        """
        try:
            move_result = self.__game.make_move(col_selection)
            if move_result:
                self.__game.change_player()
                return move_result
        except Exception:
            return False

    def check_if_win(self):
        """
        checks if there is a winner
        :return: True if there is a winner, false otherwise
        """
        winner = self.__game.get_winner()
        if winner:
            return winner
        return False

    def is_board_full(self):
        """
        checks if the board is full
        :return: True if the board is full, false otherwise
        """
        board_ind = self.__game.get_board().board_is_full()
        if board_ind:
            return True
        return board_ind

    def get_cur_player(self):
        """
        getter for current player
        """
        return self.__game.get_current_player()

    def set_player(self, cur_player):
        """
        setter for current player
        :param cur_player: the new player
        """
        return self.__game.set_player(cur_player)
