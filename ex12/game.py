
from .import board

class Game:

    BOARD_COL_NO = 7
    BOARD_ROW_NO = 6

    def __init__(self):

        self.__board = board.Board(Game.BOARD_ROW_NO, Game.BOARD_COL_NO)
        self.__cur_player = 1


    def get_board(self):
        return self.__board

    def make_move(self, column, disc):
        coordination = self.__board.get_empty_cell(column)
        if coordination:
            disc.set_coordination(coordination)
            self.__board.insert_disc(disc)
            return True
        else:
            raise Exception("Illegal move.")


    def change_player(self, cur_player):
        if cur_player == 1:
            self.__cur_player = 2
        else:
            self.__cur_player = 1


    def get_winner(self):
        for row in range(self.BOARD_ROW_NO):
            for col in range (self.BOARD_COL_NO):
                horizontal_check = self.__board.is_hor_sec(row, col, 4)
                vertical_check = self.__board.is_ver_seq(row, col, 4)
                diagonal_check = self.__board.is_seq_diag(row, col, 4)
                if horizontal_check or vertical_check or diagonal_check:
                    return self.get_player_at(row,col)

        if self.__board.board_is_full():
            return 0


    def get_player_at(self, row, col):
        if row in range(0, self.BOARD_ROW_NO) and col in range(0, self.BOARD_COL_NO):
            board_list = self.__board.get_board_list()
            disc_at_location = board_list[row][col]
            if disc_at_location:
                return disc_at_location.get_player()
            else:
                return None
        else:
            raise Exception('Illegal Location.')


    def get_current_player(self):
        return self.__cur_player

