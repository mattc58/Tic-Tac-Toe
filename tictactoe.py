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
valid_moves = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')


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
    return (None not in cells) and (cells[0] == cells[1] == cells[2])
    
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
        
def calc_computer_move(computer_piece, user_piece):
    '''
    This is a function to calculate the computer's move
    '''
    # the plan: look for a winning solution, and take it. If not, block his.
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            cell = row[j]
            if not cell:
                # empty square, so try it
                board[i][j] = computer_piece
                if is_winner():
                    column = 'A' if j == 0 else 'B' if j == 1 else 'C'
                    return '%s%d' % (column, i + 1)
                else:
                    # reset the board
                    board[i][j] = None
                    
    # now block the user's game winning moves if necessary
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            cell = row[j]
            if not cell:
                # empty square, so try it
                board[i][j] = user_piece
                if is_winner():
                    column = 'A' if j == 0 else 'B' if j == 1 else 'C'
                    return '%s%d' % (column, i + 1)
                else:
                    # reset the board
                    board[i][j] = None
    
    
    # no winning or game saving moves, so just pick the first empty cell
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            cell = row[j]
            if not cell:
                column = 'A' if j == 0 else 'B' if j == 1 else 'C'
                return '%s%d' % (column, i + 1)
    

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
    computer_piece = 'X' if user_piece == 'O' else 'O'
    print "You are playing %s\n" % user_piece
    
    if user_piece == 'X':
        print_board()
    
    # the main game loop.
    current_move = 'X'
    while not is_winner() and not is_board_full():
        is_user_move = user_piece == current_move
        
        # get the move from the active user (user or computer)
        if is_user_move:
            move = raw_input("Please choose your move by typing coordinates (like A1 or B2):")
        else:
            move = calc_computer_move(computer_piece, user_piece)
            
        # validate the move to be A1 through C3
        if is_user_move and move not in valid_moves:
            print "Please enter a move from %s" % str(valid_moves)
            continue
            
        # determine the column and row
        column = columns[move[0]]
        row = int(move[1]) - 1
        
        # make sure there's not an existing piece there
        if is_user_move and board[row][column]:
            print "Please choose an empty cell."
            continue
            
        # update the board
        board[row][column] = current_move
        
        # print the board
        if current_move != user_piece:
            print_board()
        
        current_move = 'X' if current_move == 'O' else 'O'    
    
    # print the final board
    if current_move == user_piece:    
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

