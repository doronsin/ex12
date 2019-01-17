import random

BOARD_COL_NUMBER = 7
BOARD_ROW_NUMBER = 6


class AI:
    def __init__(self, game, player):
        self.__game = game

    def find_legal_move(self):
        """
        returns a legal move of the game
        :return: the number of column in which to put disc at
        """
        if self.__game.get_winner() is not None:
            raise Exception("No possible AI moves.")
        legal_moves = []
        for row in range(BOARD_ROW_NUMBER):
            for col in range(BOARD_COL_NUMBER):
                if self.__game.get_player_at(row, col) is None:
                    legal_moves.append(col)
            if not legal_moves:
                raise Exception("No possible AI moves.")
            return random.choice(legal_moves)

    def get_last_found_move(self):
        pass
