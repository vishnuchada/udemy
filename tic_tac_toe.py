#!/usr/bin/python

import numpy as np

####print board
def print_board(r1):
     for x in r1:
            print "|".join(str(y) for y in x)
####print winner
def print_winner(r):
    print "Winner is : ",r
    quit()

####sweep the board horizontally for the winner
def horizontal_check(board):
    a = np.array(board)
    if a[0,0] == a[0,1] == a[0,2] and a[0,0] != '-':
        print_winner(a[0,0])
    elif a[1,0] == a[1,1] == a[1,2] and a[1,0] != '-':
        print_winner(a[1,0])
    elif a[2,0] == a[2,1] == a[2,2] and a[2,0] != '-':
        print_winner(a[2,0])
####sweep the board veritcally for the winner
def vertical_check(board):
    a = np.array(board)
    if a[0,0] == a[1,0] == a[2,0] and a[0,0] != '-':
        print_winner(a[1,1])
    elif a[0,1] == a[1,1] == a[2,1] and a[0,1] != '-':
        print_winner(a[0,1])
    elif a[0,2] == a[1,2] == a[2,2] and a[0,2] != '-':
        print_winner(a[0,2])
####sweep the board diagnally for the winner
def diagonal_check(board):
    a = np.array(board)
    if a[0,0] == a[1,1] == a[2,2] and a[0,0] != '-':
        print_winner(a[0,0])
    elif a[0,2] == a[1,1] == a[2,0] and a[0,2] != '-':
        print_winner(a[0,1])

####function to annotate based of user input
def annotate_board(ro,co,value,board):
    if ro <= 3 and co <= 3:
            if board[ro-1][co-1] == '-':
                board[ro-1][co-1] = value
    else:
        print "Invalid Entry"

def toggle_player(player):
    if player == 'x':
        player = 'o'
    else:
        player = 'x' 

####user input from keyboard
def tic_tac_toe():
    '''
    Players should be playing on the same machine
    Inputs : row, colum  where you want to add your (x/o) signatures
             x/o are the signatures
    '''
    ####initialize row & cells
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    n = 0


    player = raw_input("Who's starting x/o? [x]: ")
    # Makes 'x' the default
    if player != 'o':
        player = 'x'

    ####Start taking inputs from user
    while n < 9 :
        ro = int(raw_input("Enter the row number: "))
        co = int(raw_input("Enter the col number: "))

        ##ANNOTATE board
        annotate_board(ro, co, player, board)
        print_board(board)
        ##Logic for win
        horizontal_check(board)
        vertical_check(board)
        diagonal_check(board)
        toggle_player(player)
        n += 1

tic_tac_toe()
