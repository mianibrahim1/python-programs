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
         for i in range(len(self.board_array) - 1) :
            if self.board_array[i + 1] != '-':
                self.count = self.count + 1;
            if self.count == 9:
                print "Board is Full"
                return True
         print "Board is not Full"
         return False

    def move(self, place,token):
        self.board_array[place] = token

    def does_win(self):
        if self.board_array[1] == self.board_array[2] and self.board_array[2] == self.board_array[3]:
            return self.board_array[1]
        elif self.board_array[4] == self.board_array[5] and self.board_array[5] == self.board_array[6]:
            return self.board_array[4]
        elif self.board_array[7] == self.board_array[8] and self.board_array[8] == self.board_array[9]:
            return self.board_array[7]
        elif self.board_array[3] == self.board_array[4] and self.board_array[4] == self.board_array[7]:
            return self.board_array[3]
        elif self.board_array[2] == self.board_array[5] and self.board_array[5] == self.board_array[8]:
            return self.board_array[2]
        elif self.board_array[3] == self.board_array[6] and self.board_array[6] == self.board_array[9]:
            return self.board_array[3]
        elif self.board_array[1] == self.board_array[5] and self.board_array[5] == self.board_array[9]:
            return self.board_array[1]
        elif self.board_array[3] == self.board_array[5] and self.board_array[5] == self.board_array[7]:
            return self.board_array[1]
        return '-'
class tic_tac_toe_ai:
    def __init__(self):
        pass
    def make_move(self,board):
        self.count = 0
        for i in range(len(board.board_array)):
           if board.board_array[i] == '-':
               return i
               self.count = self.count + 1;
           if self.count == 9:
               print "Board is Full"

class game:
    def __init__(self):
        self.my_board = tic_tac_toe_board()
        self.my_board.print_board()
        self.win_state = False
    def play(self):
        while not self.win_state:
            self.player_move = int(raw_input("Input number between 1 and 9 for valid move:"))
            if self.player_move < 1 or self.player_move > 9:
                continue
            self.my_board.add_token(self.player_move,'O')
            self.my_board.print_board()
            if self.my_board.does_win() == 'O':
                print 'O Wins'
                break
            elif self.my_board.does_win() == 'X':
                print 'X Wins'
                break
            if self.my_board.check_full():
                break
            self.my_ai = tic_tac_toe_ai()
            self.ai_move = self.my_ai.make_move(self.my_board)
            self.my_board.move(self.ai_move,'X')
            self.my_board.print_board()
            if self.my_board.does_win() == 'O':
                print 'O Wins'
                break
            elif self.my_board.does_win() == 'X':
                print 'X Wins'
                break
            if self.my_board.check_full():
                break
new_game = game()
new_game.play()
