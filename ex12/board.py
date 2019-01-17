class Board:
    """
    this class represents the board
    """

    def __init__(self, row_no, col_no):
        """
        the ctor of the class
        :param row_no: number of rows in the board
        :param col_no: number of cols in the board
        """
        self.__board_list = []  # making the board as a two dimensional list

        for i in range(row_no):
            row = []
            for j in range(col_no):
                row.append(None)
            self.__board_list.append(row)

    def get_board_list(self):
        """
        getter for the board list
        :return:
        """
        return self.__board_list

    def is_seq_hor(self, row, col, k):
        """
        checks if there a horizontal sequence of k discs from the cell in row,col
        :param row: the row of the cell that starts the sequence
        :param col: the col of the cell that starts the sequence
        :param k: the number of disks in the sequence
        :return: true if there a horizontal sequence of k discs from the starting cell, false otherwise
        """
        if col < len(self.__board_list[0]) - (k - 1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1, k):
                if ref != self.__board_list[row][col + i]:
                    return False
            return True
        return False

    def is_ver_seq(self, row, col, k):
        """
        checks if there a vertical sequence of k discs from the cell in row,col
        :param row: the row of the cell that starts the sequence
        :param col: the col of the cell that starts the sequence
        :param k: the number of disks in the sequence
        :return: true if there a vertical sequence of k discs from the starting cell, false otherwise
        """
        if row < len(self.__board_list) - (k - 1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1, k):
                if ref != self.__board_list[row + i][col]:
                    return False
            return True
        return False

    def is_seq_diag(self, row, col, k):
        """
        checks if there a diagonal sequence of k discs from the cell in row,col
        :param row: the row of the cell that starts the sequence
        :param col: the col of the cell that starts the sequence
        :param k: the number of disks in the sequence
        :return: true if there a diagonal sequence of k discs from the starting cell, false otherwise
        """
        if row < len(self.__board_list) - (k - 1) and col < len(self.__board_list[0]) - (k - 1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1, k):
                if ref != self.__board_list[row + i][col + i]:
                    return False
            return True

        if len(self.__board_list) > row >= (k - 1) and col < len(self.__board_list[0]) - (k - 1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1, k):
                if ref != self.__board_list[row - i][col + i]:
                    return False
            return True
        return False

    def board_is_full(self):
        """
        checks if the board is full
        :return: true if the board is full, false otherwise
        """
        for row in range(len(self.__board_list)):
            for col in range(len(self.__board_list[0])):
                if not self.__board_list[row][col]:
                    return False
        return True

    def get_empty_cell(self, column):
        """
        returns the most top empty cell in a given column, returns False if there is no empty cell in the column
        :param column: the column to check
        :return: the coordinates of the free cell if there is one, and false otherwise
        """
        x = len(self.__board_list) - 1
        for i in range(x + 1):
            if not self.__board_list[x - i][column]:
                return x - i, column
        return False

    def insert_disc(self, disc):
        """
        add a given disc to the board
        :param disc: the disc to add
        """
        x, y = disc.get_coordination()
        self.__board_list[x][y] = disc
