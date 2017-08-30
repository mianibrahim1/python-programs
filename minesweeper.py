import sys
import random
class cell:
    adjacent_mines = 0
    touched = False
    is_mine = False
    def __init__(self, input_is_mine):
        self.is_mine = input_is_mine
class board:
    rows = 0;
    columns = 0;
    mines = 0;
    def __init__(self, input_rows, input_columns):
        self.rows = input_rows
        self.columns = input_columns
        self.board = [([None] * self.columns) for x in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                random_number = random.randrange(0,10)
                if (random_number == 1):
                    self.board[i][j] = cell(True)
                    self.mines = self.mines + 1
                else :
                    self.board[i][j] = cell(False)

    def print_board_lost(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.board[i][j].is_mine == True):
                    sys.stdout.write('*')
                elif (self.board[i][j].touched == True):
                    sys.stdout.write(str(self.board[i][j].adjacent_mines))
                else:
                    sys.stdout.write('-')
            sys.stdout.write('\n')

    def print_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.board[i][j].touched == True):
                    sys.stdout.write(str(self.board[i][j].adjacent_mines))
                else:
                    sys.stdout.write('-')
            sys.stdout.write('\n')
class game:
    def __init__(self,rows,columns):
        print "Minesweeper"
        self.new_board = board(rows, columns)
        self.new_board.print_board()
        self.count = 0
        self.tries = 0
        self.win = False
    def play_game(self):
        print "playing game"
        while ~self.win:
            row_input = int(raw_input("Spcify row to touch:"))
            column_input = int(raw_input("Spcify column to touch:"))
            if row_input >= self.new_board.rows or column_input >= self.new_board.columns or row_input < 0 or column_input < 0:
                print "Invalid: input out of bounds"
                continue
            self.new_board.board[row_input][column_input].touched = True
            if (self.new_board.board[row_input][column_input].is_mine == True):
                self.new_board.print_board_lost()
                print "You lost the game!!!"
                break
            else:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i == 0 and j == 0:
                            continue
                        self.r = row_input + i
                        self.c = column_input + j
                        if self.r >= self.new_board.rows or self.c >= self.new_board.columns or self.r < 0 or self.c < 0:
                            continue
                        if (self.new_board.board[self.r][self.c].is_mine == True):
                            self.count = self.count + 1
                self.new_board.board[row_input][column_input].adjacent_mines = self.count
                self.count = 0
                self.new_board.print_board()

newgame = game(5,6)
newgame.play_game()
