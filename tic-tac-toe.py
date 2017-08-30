import sys
import random

class tic_tac_toe_board:
    def __init__(self):
        self.board_array = ['s','-','-','-','-','-','-','-','-','-']
    def print_board(self):
        for i in range(len(self.board_array)):
            if i ==0:
                continue
            sys.stdout.write(self.board_array[i])
            if i % 3 == 0:
                sys.stdout.write('\n')
                continue
            sys.stdout.write('|')
    def add_token(self,place,token):
        self.board_array[place] = token
    def check_full(self):
         self.count = 0;
         for i in range(len(self.board_array)):
            if self.board_array[i] != '-':
                self.count = self.count + 1;
            if self.count == 9:
                print "Board is Full"
                return
         print "Board is not Full"

    def move(self, place,token):
        self.board_array[place] = token

class tic_tac_toe_ai:
    def __init__(self):
        pass
    def make_move(self,board):
        self.count = 0
        for i in range(len(board.board_array)):
           if board.board_array[i] == '-':
               return i
               self.count = self.count + 1;
           if count == 9:
               print "Board is Full"


my_board = tic_tac_toe_board()
my_board.print_board()
my_board.add_token(1,'O')
my_board.print_board()
my_ai = tic_tac_toe_ai()
num =  my_ai.make_move(my_board)
my_board.move(num,'X')
print num
my_board.print_board()
my_board.check_full()
