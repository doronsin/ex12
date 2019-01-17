
class Board:

    def __init__(self, row_no, col_no):

        self.__board_list = [] # making the board as a two dimensional list

        for i in range(row_no):
            row = []
            for j in range(col_no):
                row.append(None)
            self.__board_list.append(row)

    def get_board_list(self):
        return self.__board_list

    def is_hor_sec(self, row, col, k):
        if col < len(self.__board_list[0])-(k-1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1,k):
                if ref != self.__board_list[row][col+i]:
                    return False
            return True
        return False


    def is_ver_seq(self, row, col, k):
        if row < len(self.__board_list)-(k-1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1,k):
                if ref != self.__board_list[row+i][col]:
                    return False
            return True
        return False

    def is_seq_diag(self, row, col, k):
        if row < len(self.__board_list) - (k-1) and col < len(self.__board_list[0]) - (k-1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1,k):
                if ref != self.__board_list[row+i][col+i]:
                    return False
            return True


        if row < len(self.__board_list) and row >= (k-1) and col < len(self.__board_list[0]) - (k-1):
            ref = self.__board_list[row][col]
            if ref is None:
                return False
            for i in range(1,k):
                if ref != self.__board_list[row-i][col+i]:
                    return False
            return True
        return False


    def board_is_full(self):
        for row in range (len(self.__board_list)):
            for col in range (len(self.__board_list[0])):
                if not self.__board_list[row][col]:
                    return False
        return True

    def get_empty_cell(self, column):
        '''
        This function
        :param column: column number
        :return: empty cell coordination (tuple) or False if the column is full
        '''
        x = len(self.__board_list)-1
        for i in range(x+1):
            if not self.__board_list[x-i][column]:
                return x-i, column
        return False

    def insert_disc(self, disc):
        x,y = disc.get_coordination()
        self.__board_list[x][y] = disc


