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

def print_board():
    '''
    Print the board to the console
    '''
    for row in board:
        print " | ".join([item or ' ' for item in row])

def main():
    print "***********************************************"
    print "Hello, this is Matt Culbreth's Tic-Tac-Toe game."
    print "Good luck! (You'll need it.)"
    print "***********************************************"
    
    user_piece = random.choice(game_pieces)
    print "You are playing %s\n" % user_piece


if __name__ == '__main__':
	main()

