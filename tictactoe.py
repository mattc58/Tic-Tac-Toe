#!/usr/bin/env python
# encoding: utf-8
"""
tictactoe.py

This application will play tic-tac-toe and never lose.

Usage:
    Either run from the command line with "python tictactoe.py", or 
    from the REPL by doing import tictactoe as t; t.main()

Created by Matt Culbreth on 2010-10-18.
Please see LICENSE file.
"""

import sys
import os
import random
import copy

columns = {
    'A' : 0,
    'B' : 1,
    'C' : 2
}
valid_moves = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')

class GamePlayException(RuntimeError):
    '''
    A typed exception we'll use for game rule violations
    '''
    pass

class TicTacToe(object):
    '''
    The class for the game
    '''
    def __init__(self):
        '''
        Init the game board
        '''
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def move(self, piece, cell):
        '''
        Update the board using the piece and cell
        '''
        # validate the move to be A1 through C3
        if cell not in valid_moves:
            print "Please enter a move from %s" % str(valid_moves)
            raise GamePlayException()
        
        # determine the column and row
        column = columns[cell[0]]
        row = int(cell[1]) - 1
    
        # make sure there's not an existing piece there
        if self.board[row][column]:
            print "Please choose an empty cell."
            raise GamePlayException()
        
        self.board[row][column] = piece
        
    def print_board(self):
        '''
        Print the self.board to the console
        '''
        print "    A | B | C"
        print "-" * 14
        for i in range(len(self.board)):
            s = "%d   " % (i + 1)
            row = self.board[i]
            s += " | ".join([item or ' ' for item in row])
            print s
        print "-" * 14
    
    def is_board_full(self):
        '''
        Return True if the self.board is full
        '''
        empty = [None in row for row in self.board]
        return empty == [False, False, False]

    def _check_cells(self, cells):
        '''
        Check a passed in set of cells for a winning solution
        '''    
        return (None not in cells) and (cells[0] == cells[1] == cells[2])
    
    def is_winner(self, test_board=None):
        '''
        Return True if we have a winner
        '''
        if not test_board:
            test_board = self.board
            
        # check for a row of all the same
        cells = []
    
        for row in test_board:
            cells = [row[0], row[1], row[2]]
            if self._check_cells(cells):
                return cells[0]
    
        # for a column of all the same
        for column in range(3):
            cells = [test_board[0][column], test_board[1][column], test_board[2][column]]
            if self._check_cells(cells):
                return cells[0]
    
        # check the two diagonals
        diag1 = [test_board[0][0], test_board[1][1], test_board[2][2]]
        diag2 = [test_board[0][2], test_board[1][1], test_board[2][0]]
        if self._check_cells(diag1):
            return diag1[0]
        if self._check_cells(diag2):
            return diag2[0]
        
        # if we come down here, no winner
        return None
        
    def calc_computer_move(self, computer_piece, user_piece):
        '''
        This is a function to calculate the computer's move
        '''
        # make a local copy
        test_board = copy.deepcopy(self.board)
    
        # The plan: look for a winning solution, and take it. If not, block the user's if they have one.
        # Then look for good moves.
        for i in range(len(test_board)):
            row = test_board[i]
            for j in range(len(row)):
                cell = row[j]
                if not cell:
                    # empty square, so try it
                    test_board[i][j] = computer_piece
                    if self.is_winner(test_board):
                        column = 'A' if j == 0 else 'B' if j == 1 else 'C'
                        return '%s%d' % (column, i + 1)
                    else:
                        # reset the board
                        test_board[i][j] = None
                    
        # now block the user's game winning moves if necessary
        for i in range(len(test_board)):
            row = test_board[i]
            for j in range(len(row)):
                cell = row[j]
                if not cell:
                    # empty square, so try it
                    test_board[i][j] = user_piece
                    if self.is_winner(test_board):
                        column = 'A' if j == 0 else 'B' if j == 1 else 'C'
                        return '%s%d' % (column, i + 1)
                    else:
                        # reset self.board
                        test_board = copy.deepcopy(self.board)

        # stop cornering
        if self.board[0][1] == user_piece and self.board[1][0] == user_piece and not self.board[0][0]:
            return 'A1'
        if self.board[0][1] == user_piece and self.board[1][2] == user_piece and not self.board[0][2]:
            return 'C1'
        if self.board[1][2] == user_piece and self.board[2][1] == user_piece and not self.board[2][2]:
            return 'C3'
        if self.board[1][0] == user_piece and self.board[2][1] == user_piece and not self.board[2][0]:
            return 'A3'
        
        # triangles (B1, C2, B3, A2)
        if self.board[1][1] == user_piece:
            if not self.board[0][1] and (self.board[0][0] == user_piece or self.board[0][2] == user_piece):
                return 'B1'
            if not self.board[1][2] and (self.board[0][2] == user_piece or self.board[2][2] == user_piece):
                return 'C2'
            if not self.board[2][1] and (self.board[2][0] == user_piece or self.board[2][2] == user_piece):
                return 'B3'
            if not self.board[1][0] and (self.board[0][1] == user_piece or self.board[0][0] == user_piece):
                return 'A2'
    
        # no winning or game saving moves, so pick a cell out of a list of possibles, ordered by goodness
        good_cells = ('B2', 'A1', 'C1', 'A3', 'C3', 'B1', 'A2', 'B3', 'C2')
        for cell in good_cells:
            column = columns[cell[0]]
            row = int(cell[1]) - 1
            if not self.board[row][column]:
                return cell
    

def main():
    '''
    The main function with the main game loop
    '''
    print "***********************************************"
    print "Hello, this is Matt Culbreth's Tic-Tac-Toe game."
    print "Good luck! (You'll need it.)"
    print "***********************************************"
    
    # go in an infinite loop. kill the program to end the game.
    while True:
        # setup the board and the initial pieces
        game = TicTacToe()
        
        user_piece = random.choice(('X', 'O'))
        computer_piece = 'X' if user_piece == 'O' else 'O'
        print "You are playing %s\n" % user_piece
    
        if user_piece == 'X':
            game.print_board()
    
        # the main game loop. Keep going until we have a winner or a full board.
        current_move = 'X'
        while not game.is_winner() and not game.is_board_full():
            is_user_move = user_piece == current_move
        
            # get the move from the active user (user or computer)
            if is_user_move:
                move = raw_input("Please choose your move by typing coordinates (like A1 or B2):")
                move = move.upper()
            else:
                move = game.calc_computer_move(computer_piece, user_piece)
            
            # update the board
            try:
                game.move(current_move, move)
            except GamePlayException:
                continue
        
            # print the board if it's the computer's turn
            if current_move != user_piece:
                game.print_board()
            
            # change pieces
            current_move = 'X' if current_move == 'O' else 'O'    
    
        # print the final board
        game.print_board()
    
        winner = game.is_winner()  
        if winner:
            if winner == user_piece:
                print "You won! NOOOOOOOOOOOOOOOOO!"
            else:
                print "HAH! Beat you."
        elif game.is_board_full():
            print "DRAW"
        else:
            print "Something I didn't consider possible"
            
        print "\nNEW GAME\n"
        
        
if __name__ == '__main__':
	main()

