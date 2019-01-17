import tkinter as tk
from tkinter import *

import sys

class Start_window:
    def __init__(self, root):

        self.start_parent = root
        self.start_parent.title("Connect Four | Opening window")
        self.player1 = "Human"
        self.player2 = "Human"
        self.start_parent.geometry("270x100")
        self.design_window(self.start_parent)

    def design_window(self, root):
        self.start_parent = root
        self.opening_text = tk.Label(self.start_parent, text="Please define the players", font=("Ariel", 12), justify = tk.CENTER, height = 2)
        self.opening_text.pack()

        self.left_frame = tk.Frame(self.start_parent)
        self.left_frame.pack(side = tk.LEFT)
        self.right_frame = tk.Frame(self.start_parent)
        self.right_frame.pack(side = tk.RIGHT)

        self.disp_player1 = tk.Label(self.left_frame, text="Player 1", font=("Ariel", 10), width = 8)
        self.disp_player1.pack(side=tk.TOP)
        self.listbox1 = Listbox(self.left_frame, exportselection=0, height=2, width = 10, font=("Ariel", 10), selectbackground = "blue" )
        self.listbox1.insert(1, "Human")
        self.listbox1.insert(2, "Computer")
        self.listbox1.pack()

        self.disp_player2 = tk.Label(self.right_frame, text="Player 2", font=("Ariel", 10), width = 8)
        self.disp_player2.pack(side=tk.TOP)
        self.listbox2 = Listbox(self.right_frame, exportselection=0, height=2, width = 10,font=("Ariel", 10),  selectbackground = "red")
        self.listbox2.insert(1, "Human")
        self.listbox2.insert(2, "Computer")
        self.listbox2.pack()

        done_button = tk.Button(self.start_parent, text="DONE", padx=30, pady=6, command=self.done(), bg = "red")
        done_button.pack(side = tk.BOTTOM)


        self.start_parent.mainloop()


    def done(self):
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
        return self.player1

    def get_player2(self):
        return self.player2

class Gui:
    def __init__(self, root, gr, player1, player2, ai1, ai2):

        self.gr = gr
        self.root = root
        self.root.title("Connect Four | Barak Pelman")
        self.root.geometry("728x700")
        self.end_game = False
        self.players_dict = {1:player1, 2:player2}
        self.ais_dict = {1:ai1, 2:ai2}

        self.labels = []
        self.empty_image = tk.PhotoImage(file="ex12/empty.gif")  # All slots begin with an "empty" image
        self.blue_image = tk.PhotoImage(file="ex12/blue.gif")  # Blue slots
        self.red_image = tk.PhotoImage(file="ex12/red.gif")  # Red slots

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(side=tk.TOP)
        self.create_board_list(self.main_frame)
        self.slots_in_grid()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(side = tk.TOP)
        self.create_buttons(self.buttons_frame)

        self.create_lower_bar()
        self.msg("Player1: Where do you put your disc?")
        self.act_if_player_ai()


    def create_lower_bar(self):
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT)
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT)

        self.disp_player1 = tk.Label(left_frame, text="Player 1: " + self.players_dict[1], font=("Ariel", 12), fg = "blue")
        self.disp_player1.pack(side=tk.TOP)
        listbox1 = Listbox(left_frame, selectmode=SINGLE)
        listbox1.yview_scroll(1, UNITS)

        self.disp_player2 = tk.Label(right_frame, text="Player 2: "+self.players_dict[2], font=("Ariel", 12), fg = "red")
        self.disp_player2.pack(side=tk.TOP)
        listbox2 = Listbox(right_frame, selectmode=SINGLE)
        listbox2.yview_scroll(1, UNITS)

        self._display_label = tk.Label(self.root, height = 3)
        self._display_label.pack(side=tk.TOP)

    def create_board_list(self, frame):
        for i in range(6):
            row = []
            for j in range(7):
                row.append(tk.Label(frame, image=self.empty_image))
            self.labels.append(row)

    def slots_in_grid(self):
        for row in range(6):
            for col in range(7):
                self.labels[row][col].grid(row=row,column=col,padx=0,pady=0)

    def create_buttons(self, frame):
        for i in range(7):
            button = tk.Button(frame, text = str(i+1), padx = 45, command = self.col_but_evet(i))
            button.grid(row=0, column = i)

    def act_if_player_ai(self):
        cur_player = self.gr.get_cur_player()
        if self.players_dict[cur_player] == "Computer":
            try:
                col_num = self.ais_dict[cur_player].find_legal_move()
                self.col_but_evet(col_num)()
            except Exception as e:
                self.msg(e)

    def col_but_evet(self, col_num):
        def update_cl_selection():
            if not self.end_game:
                cur_player = self.gr.get_cur_player()
                if cur_player == 1:
                    disc = self.gr.one_turn(col_num, cur_player)
                    if disc:
                        self.mang_disc(disc, cur_player)
                    else:
                        self.msg("There is no place here")
                else:
                    disc = self.gr.one_turn(col_num, cur_player)
                    if disc:
                        self.mang_disc(disc, cur_player)
                    else:
                        self.msg("There is no place here")
                self.act_if_player_ai()
        return update_cl_selection

    def mang_disc(self, disc, cur_player):
        self.register_disc(disc, cur_player)
        winner = self.gr.check_if_win()
        if winner:
            self.msg("Player " + str(winner) + " WON!!")
            self.end_game = True

        elif self.gr.is_board_full():
                self.msg("Board is full! No one Wins")
                self.end_game = True
        else:
            self.mang_turn_desply()


    def mang_turn_desply(self):
        cur_player = str(self.gr.get_cur_player())
        self.msg("Player" + cur_player + ": Where do you put your disc?")
        self.root.update()


    def msg(self, text):
        self._display_label.configure(text = text, font = ("Ariel", 16))
        self.root.update()

    def register_disc(self, disc, cur_player):
        parent = self.main_frame
        x,y = disc.get_coordination()
        if cur_player ==1:
            self.labels[x][y] = tk.Label(parent, image = self.blue_image )
        else:
            self.labels[x][y]= tk.Label(parent, image= self.red_image)
        self.slots_in_grid()

