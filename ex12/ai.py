import random

class AI:

    def __init__(self, game, player):

        self.__game = game

    def find_legal_move(self, timeout=None):
        # vertical_move = self.vertical_move()
        # if vertical_move:
        #     return vertical_move
        legal_moves = []
        for row in range(6):
            for col in range (7):
                if self.__game.get_player_at(row, col) == None:
                    legal_moves.append(col)
            if legal_moves == []:
                raise Exception("No possible AI moves")
            return random.choice(legal_moves)



        # for i in range (self.__game.BOARD_COL_NO):
        #     if self.__game.get_board().get_empty_cell(i):
        #         legal_moves.append(i)
        # if legal_moves == []:
        #     raise Exception("No possible AI moves")
        # return random.choice(legal_moves)


    def vertical_move(self):
        for row in range(self.__game.BOARD_ROW_NO):
            for col in range (self.__game.BOARD_COL_NO):
                vertical_check = self.__game.get_board().is_ver_seq(row, col, 3)
                if vertical_check:
                    empty_cell = self.__game.get_board().get_empty_cell(col)
                    if empty_cell and empty_cell[0]==row-1:
                        return col


    def get_last_found_move(self):
        pass
