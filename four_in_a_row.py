"""
This is the main file that responsible for the operations
"""
from ex12.game import Game
from ex12.game_runner import GameRunner
from ex12.gui import *
from ex12.ai import AI


def run_game():
    """
    runs the game
    :return: true if the player wants another game, false otherwise
    """
    g = Game()
    gr = GameRunner(g)
    start_screen = StartWindow()
    player1 = start_screen.get_player1()
    player2 = start_screen.get_player2()
    ai1 = AI(g, player1)
    ai2 = AI(g, player2)
    main_gui = Gui(gr, player1, player2, ai1, ai2)
    main_gui.run()
    return main_gui.get_another_game()


if __name__ == '__main__':
    another_game = run_game()
    if another_game:
        another_game = run_game()
