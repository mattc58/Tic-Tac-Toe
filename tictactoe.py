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
    print "-" * 14
    
def is_board_full():
    '''
    Return True if the board is full
    '''
    empty = [None in row for row in board]
    return empty == [False, False, False]

def check_cells(cells):
    '''
    Check a passed in set of cells for a winning solution
    '''    
    return (None not in cells) and (cells[0] == cells[1] and cells[2])
    
def is_winner():
    '''
    Return True if we have a winner
    '''
    # check for a row of all the same
    cells = []
    
    for row in board:
        cells = [row[0], row[1], row[2]]
        if check_cells(cells):
            return cells[0]
    
    # for a column of all the same
    for column in range(3):
        cells = [board[0][column], board[1][column], board[2][column]]
        if check_cells(cells):
            return cells[0]
    
    # check the two diagonals
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    if check_cells(diag1):
        return diag1[0]
    if check_cells(diag2):
        return diag2[0]
        
    # if we come down here, no winner
    return None
        
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
    print_board()
    print "You are playing %s\n" % user_piece
    
    # the main game loop.
    current_move = 'X'
    while not is_winner() and not is_board_full():
        # get the move from the active user (user or computer)
        if current_move == user_piece:
            move = raw_input("Please choose your move by typing coordinates (like A1 or B2):")
        else:
            move = calc_computer_move()
            
        # validate the move to be A1 through C3
            
        # update the game board
        column = columns[move[0]]
        row = int(move[1]) - 1
        board[row][column] = current_move
        
        # print the board
        if current_move != user_piece:
            print_board()
        
        current_move = 'X' if current_move == 'O' else 'O'    
        
    print_board()
    
    winner = is_winner()  
    if winner:
        if winner == user_piece:
            print "You won! NOOOOOOOOOOOOOOOOO!"
        else:
            print "HAH! Beat you."
    elif is_board_full():
        print "DRAW"
    else:
        print "Something I didn't consider possible"
        
        
if __name__ == '__main__':
	main()

