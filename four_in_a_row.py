
'''
This is the main file that responsible for the operations
'''

import tkinter as tk
from ex12.game import Game
from ex12.game_runner import GameRunner
from ex12.gui import *
from ex12.ai import AI


if __name__ == '__main__':
    g = Game()
    gr = GameRunner(g)
    start_root = tk.Tk()
    start_screen = Start_window(start_root)
    player1 = start_screen.get_player1()
    player2 = start_screen.get_player2()
    board = g.get_board()
    ai1 = AI(g, player1)
    ai2 = AI(g, player2)
    main_root = tk.Tk()
    main_screen = Gui(main_root, gr, player1, player2, ai1, ai2)
    main_root.mainloop()

