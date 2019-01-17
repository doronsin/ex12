import tkinter as tk
from tkinter import *
import time
import sys

SLEEP_BETWEEN_AIS_IN_SECONDS = 1

BOARD_ROW_NUMBER = 6

BOARD_COL_NUMBER = 7

HUMAN_INDICATOR = "Human"
COMPUTER_INDICATOR = "Computer"


class StartWindow:
    """
    responsible for the start window of the game
    """

    def __init__(self):
        """
        the ctor of the class
        :param root:
        """
        self.start_parent = tk.Tk()
        self.start_parent.title("Connect Four | Opening window")
        self.player1 = HUMAN_INDICATOR
        self.player2 = HUMAN_INDICATOR
        self.design_window(self.start_parent)

    def design_window(self, root):
        """
        designs the window
        :param root: the root
        """
        self.start_parent = root
        self.opening_text = tk.Label(self.start_parent, text="Please define the players", font=("Ariel", 12),
                                     justify=tk.CENTER, height=2)
        self.opening_text.pack()

        self.left_frame = tk.Frame(self.start_parent)
        self.left_frame.pack(side=tk.LEFT)
        self.right_frame = tk.Frame(self.start_parent)
        self.right_frame.pack(side=tk.RIGHT)

        self.disp_player1 = tk.Label(self.left_frame, text="Player 1", font=("Ariel", 10), width=8)
        self.disp_player1.pack(side=tk.TOP)
        self.listbox1 = Listbox(self.left_frame, exportselection=0, height=2, width=10, font=("Ariel", 10),
                                selectbackground="blue")
        self.listbox1.insert(1, HUMAN_INDICATOR)
        self.listbox1.insert(2, COMPUTER_INDICATOR)
        self.listbox1.pack()

        self.disp_player2 = tk.Label(self.right_frame, text="Player 2", font=("Ariel", 10), width=8)
        self.disp_player2.pack(side=tk.TOP)
        self.listbox2 = Listbox(self.right_frame, exportselection=0, height=2, width=10, font=("Ariel", 10),
                                selectbackground="red")
        self.listbox2.insert(1, HUMAN_INDICATOR)
        self.listbox2.insert(2, COMPUTER_INDICATOR)
        self.listbox2.pack()

        done_button = tk.Button(self.start_parent, text="DONE", padx=30, pady=6, command=self.done(), bg="red")
        done_button.pack(side=tk.BOTTOM)

        self.start_parent.mainloop()

    def done(self):
        """
        the function that happens when the done button is pressed
        :return: the function
        """

        def exit():
            x = None
            y = None
            selection1 = self.listbox1.curselection()
            selection2 = self.listbox2.curselection()
            for i in selection1:
                x = str(self.listbox1.get(i))
            for j in selection2:
                y = str(self.listbox2.get(j))
            if x: self.player1 = x
            if y: self.player2 = y
            self.start_parent.destroy()

        return exit

    def get_player1(self):
        """
        getter for player1
        :return: player1 type
        """
        return self.player1

    def get_player2(self):
        """
        getter for player2
        :return: player2 type
        """
        return self.player2


class Gui:
    """
    the GUI of the game
    """

    def __init__(self, gr, player1, player2, ai1, ai2):
        """
        the ctor of the class
        :param root: the root of the gui
        :param gr: the gameRunner object
        :param player1: player1 type
        :param player2: player2 type
        :param ai1: ai for the first player object
        :param ai2: ai for the secont player object
        """
        self.gr = gr
        self.root = tk.Tk()
        self.root.title("Connect Four | Barak Pelman")
        self.end_game = False
        self.players_type_dict = {1: player1, 2: player2}
        self.ais_dict = {1: ai1, 2: ai2}

        self.labels = []
        self.empty_image = tk.PhotoImage(file="ex12/empty.gif")  # All slots begin with an "empty" image
        self.blue_image = tk.PhotoImage(file="ex12/blue.gif")  # Blue slots
        self.red_image = tk.PhotoImage(file="ex12/red.gif")  # Red slots

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(side=tk.TOP)
        self.create_board_list(self.main_frame)
        self.slots_in_grid()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(side=tk.TOP)
        buttons = self.create_buttons(self.buttons_frame)

        self.create_lower_bar()
        self.msg("Player1: Where do you put your disc?")

        if player1 == COMPUTER_INDICATOR and player2 == COMPUTER_INDICATOR:
            self.sleep_between_turns = SLEEP_BETWEEN_AIS_IN_SECONDS
            for button in buttons:
                button.config(state='disabled')
        else:
            self.sleep_between_turns = 0
        self.act_if_player_ai()
        self.root.mainloop()

    def create_lower_bar(self):
        """
        responsible to create the lower bar in the screen
        """
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT)
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT)

        self.disp_player1 = tk.Label(left_frame, text="Player 1: " + self.players_type_dict[1], font=("Ariel", 12),
                                     fg="blue")
        self.disp_player1.pack(side=tk.TOP)
        listbox1 = Listbox(left_frame, selectmode=SINGLE)
        listbox1.yview_scroll(1, UNITS)

        self.disp_player2 = tk.Label(right_frame, text="Player 2: " + self.players_type_dict[2], font=("Ariel", 12),
                                     fg="red")
        self.disp_player2.pack(side=tk.TOP)
        listbox2 = Listbox(right_frame, selectmode=SINGLE)
        listbox2.yview_scroll(1, UNITS)

        self._display_label = tk.Label(self.root, height=3)
        self._display_label.pack(side=tk.TOP)

    def create_board_list(self, frame):
        """
        creates the board
        :param frame: where to create the board
        """
        for i in range(BOARD_ROW_NUMBER):
            row = []
            for j in range(BOARD_COL_NUMBER):
                row.append(tk.Label(frame, image=self.empty_image))
            self.labels.append(row)

    def slots_in_grid(self):
        """
        creates the slots in the grid
        """
        for row in range(BOARD_ROW_NUMBER):
            for col in range(BOARD_COL_NUMBER):
                self.labels[row][col].grid(row=row, column=col, padx=0, pady=0)

    def create_buttons(self, frame):
        """
        creates the buttons
        :param frame: where to create the buttons
        :returns the buttons constructed
        """
        buttons = []
        for i in range(7):
            button = tk.Button(frame, text=str(i + 1), padx=45, command=self.col_change_event(i))
            button.grid(row=0, column=i)
            buttons.append(button)
        return buttons

    def act_if_player_ai(self):
        """
        this function checks if the current player is an AI player, and if so - makes an ai move
        """
        cur_player = self.gr.get_cur_player()
        if self.players_type_dict[cur_player] == COMPUTER_INDICATOR:
            try:
                col_num = self.ais_dict[cur_player].find_legal_move()
                self.col_change_event(col_num)()
            except Exception as e:
                self.msg(e)

    def col_change_event(self, col_num):
        """
        returns a function that needs to be invoked in order to change the correct cell in the board
        :param col_num: the col_number to add a disc
        :return: the function that needs to be invoked (or by press of a button, or by the AI)
        """

        def update_cl_selection():
            if not self.end_game:
                disc = self.gr.one_turn(col_num)
                if disc:
                    self.register_disc(disc)
                    self.deal_with_winner()
                else:
                    self.msg("There is no place here")
                time.sleep(self.sleep_between_turns)
                if not self.end_game:
                    self.act_if_player_ai()

        return update_cl_selection

    def deal_with_winner(self):
        """
        checks if there is a winner, and deals with it
        """
        winner = self.gr.check_if_win()
        if winner:
            self.msg("Player " + str(winner) + " WON!!")
            self.end_game = True
        elif self.gr.is_board_full():
            self.msg("Board is full! No one Wins")
            self.end_game = True

        else:
            self.manage_turn_display()

    def manage_turn_display(self):
        """
        manages the display of the current turn
        :return:
        """
        cur_player = str(self.gr.get_cur_player())
        self.msg("Player" + cur_player + ": Where do you put your disc?")
        self.root.update()

    def msg(self, text):
        """
        send a message to the user throw the window
        :param text: the message to show
        """
        self._display_label.configure(text=text, font=("Ariel", 16))
        self.root.update()

    def register_disc(self, disc):
        """
        add disc to the board of the GUI
        :param disc: the disc to add
        """
        parent = self.main_frame
        x, y = disc.get_coordination()
        if self.gr.get_cur_player() == 1:
            self.labels[x][y] = tk.Label(parent, image=self.red_image)
        else:
            self.labels[x][y] = tk.Label(parent, image=self.blue_image)
        self.slots_in_grid()

