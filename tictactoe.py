#!/usr/bin/env python
# encoding: utf-8
"""
tictactoe.py

This application will play tic-tac-toe and never lose.

Created by Matt Culbreth on 2010-10-18.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import random

game_pieces = ('X', 'O')
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

columns = {
    'A' : 0,
    'B' : 1,
    'C' : 2
}

def print_board():
    '''
    Print the board to the console
    '''
    print "    A | B | C"
    print "-" * 14
    for i in range(len(board)):
        s = "%d|  " % (i + 1)
        row = board[i]
        s += " | ".join([item or ' ' for item in row])
        print s
        
def calc_computer_move():
    '''
    This is a function to calculate the computer's move
    '''
    return 'A1'

def main():
    '''
    The main function with the main game loop
    '''
    print "***********************************************"
    print "Hello, this is Matt Culbreth's Tic-Tac-Toe game."
    print "Good luck! (You'll need it.)"
    print "***********************************************"
    
    # let's choose a piece at random
    user_piece = random.choice(game_pieces)
    print "You are playing %s\n" % user_piece
    
    # the main game loop.
    # algorithm:
    #   show the board
    #   let X go
    #   if winner, end
    #   show the board
    #   let O go
    #   if winner, end
    #   show the board
    next_move = user_piece if user_piece == 'X' else 'O'
    while True:
        print_board()
        
        # get the move from the active user (user or computer)
        if next_move == user_piece:
            move = raw_input("Please choose your move by typing coordinates (like A1 or B2):")
        else:
            move = calc_computer_move()
            
        # validate the move to be A1 through C3
            
        # update the game board
        column = columns[move[0]]
        row = int(move[1]) - 1
        board[row][column] = next_move
        
        next_move = 'X' if next_move == 'O' else 'O'    
        
        


if __name__ == '__main__':
	main()

