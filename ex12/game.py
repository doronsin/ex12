from . import board
from .disc import Disc

BOARD_FULL_INDICATOR = 0


class Game:
    """
    this class responsible to the game logic
    """
    BOARD_COL_NO = 7
    BOARD_ROW_NO = 6

    def __init__(self):
        """
        the ctor of the class
        """
        self.__board = board.Board(Game.BOARD_ROW_NO, Game.BOARD_COL_NO)
        self.__cur_player = 1

    def get_board(self):
        """
        getter for the board
        :return: the board
        """
        return self.__board

    def make_move(self, column):
        """
        makes move in the game
        :param column: the colum in which to insert the disc
        :return: True if the disc inserted, false otherwise
        """
        if self.get_winner() is not None:
            raise Exception("Illegal move.")
        disc = Disc(self.__cur_player, (0, 0))
        coordination = self.__board.get_empty_cell(column)
        if coordination:
            disc.set_coordination(coordination)
            self.__board.insert_disc(disc)
            self.__change_player()
            return disc
        else:
            raise Exception("Illegal move.")

    def __change_player(self):
        """
        switches to the other player
        """
        if self.__cur_player == 1:
            self.__cur_player = 2
        else:
            self.__cur_player = 1

    def get_winner(self):
        """
        returns the number of the winning player, or 0 if the board is full
        :return: 1 if player1 is winner, 2 if player 2 is winner, 0 if the board is full, none otherwise
        """
        for row in range(self.BOARD_ROW_NO):
            for col in range(self.BOARD_COL_NO):
                horizontal_check = self.__board.is_seq_hor(row, col, 4)
                vertical_check = self.__board.is_ver_seq(row, col, 4)
                diagonal_check = self.__board.is_seq_diag(row, col, 4)
                if horizontal_check or vertical_check or diagonal_check:
                    return self.get_player_at(row, col)

        if self.__board.board_is_full():
            return BOARD_FULL_INDICATOR

    def get_player_at(self, row, col):
        """
        returns the player located in row,col
        :param row: the row
        :param col: the col
        :return:
        """
        disc_at_location = self.__board.get_disc_at(row, col)
        if disc_at_location:
            return disc_at_location.get_player()

    def get_current_player(self):
        """
        getter for the current player
        :return: the current player number
        """
        return self.__cur_player
