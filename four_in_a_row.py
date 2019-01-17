'''
This is the main file that responsible for the operations
'''

import tkinter as tk
from ex12.game import Game
from ex12.game_runner import GameRunner
from ex12.gui import *
from ex12.ai import AI


def run_game():
    g = Game()
    gr = GameRunner(g)
    start_screen = StartWindow()
    player1 = start_screen.get_player1()
    player2 = start_screen.get_player2()
    ai1 = AI(g, player1)
    ai2 = AI(g, player2)
    main_gui = Gui(gr, player1, player2, ai1, ai2)


if __name__ == '__main__':
    run_game()
