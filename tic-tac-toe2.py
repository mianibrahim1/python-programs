import sys
import os

class board:
    def __init__(self):
        self.board_structure = ['s','*','*','*','*','*','*','*','*','*']
        self.count = 0
    def print_board(self):
        print "Displaying Board"
        for i in range(len(self.board_structure) - 1):
            sys.stdout.write(self.board_structure[i+1])
            if ( i + 1 ) % 3 == 0:
                sys.stdout.write('\n')
                if i + 1 != 9:
                    print '- - -'
            else:
                sys.stdout.write('|')

    def board_full(self):
        for i in range(len(self.board_structure) - 1):
            if self.board_structure[i+1] != '*':
                self.count += 1
        if self.count == 9:
            print True
        else :
            print False
    def move_token(self,move,token):
        self.board_structure[move] = token

    def ai_make_move(self):
        for i in range(len(self.board_structure) - 1):
            if self.board_structure[i+1] == '*':
                self.move_token(i + 1, 'X' )
                return True
        return False

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
     return '*'


class game:
    def __init__(self):
        self.new_board = board()
        self.win_state = False
    def play_game(self):
        while not self.win_state:
            self.player_move = int(raw_input("Enter a value between 1 and 9 for a valid move:"))
            # Check bounds here
            self.new_board.move_token(self.player_move, 'O')
            self.new_board.ai_make_move()
            self.new_board.print_board()
            print self.new_board.does_win()
new_game = game()
new_game.play_game()
