
import numpy as np

####print board
def print_board(r1):
     for x in r1:
            print "|".join(str(y) for y in x)
####print winner
def print_winner(r):
    print "Winner is : ",r

####sweep the board horizontally for the winner
def horizontal_check(row):
    a = np.array(row)
    if a[0,0] == a[0,1] == a[0,2] and a[0,0] != '-':
        print_winner(a[0,0])
        quit()
    elif a[1,0] == a[1,1] == a[1,2] and a[1,0] != '-':
        print_winner(a[1,0])
        quit()
    elif a[2,0] == a[2,1] == a[2,2] and a[2,0] != '-':
        print_winner(a[2,0])
        quit()     
####sweep the board veritcally for the winner
def vertical_check(row):
    a = np.array(row)
    if a[0,0] == a[1,0] == a[2,0] and a[0,0] != '-':
        print_winner(a[1,1])
        quit()
    elif a[0,1] == a[1,1] == a[2,1] and a[0,1] != '-':
        print_winner(a[0,1])
        quit()
    elif a[0,2] == a[1,2] == a[2,2] and a[0,2] != '-':
        print_winner(a[0,2])
        quit()
####sweep the board diagnally for the winner
def diagonal_check(row):
    a = np.array(row)
    if a[0,0] == a[1,1] == a[2,2] and a[0,0] != '-':
        print_winner(a[0,0])
        quit()
    elif a[0,2] == a[1,1] == a[2,0] and a[0,2] != '-':
        print_winner(a[0,1])
        quit()

####function to annotate based of user input
def annotate_board(ro,co,value,row):
    if ro <= 3 and co <= 3:
            if row[ro-1][co-1] == '-':
                row[ro-1][co-1] = value
    else:
        print "Invalid Entry"
   

####user input from keyboard
def tic_tac_toe():
    '''
    Players should be playing on the same machine
    Inputs : row, colum  where you want to add your (x/o) signatures
             x/o are the signatures
    '''
    ####initialize row & cells
    row = [['-','-','-'],['-','-','-'],['-','-','-']]
    n = 0

    ####Start taking inputs from user
    while n < 9 :
        ro = int(raw_input("Enter the row number: "))
        co = int(raw_input("Enter the col number: "))
        value = raw_input("Enter your value: ")
        if value == 'x' or value == 'o':

            ##ANNOTATE board
            annotate_board(ro,co,value,row)
            print_board(row)
            ##Logic for win
            horizontal_check(row)
            vertical_check(row)
            diagonal_check(row)
            n += 1
        else: 
            print "Wrong Marker, should be either - x - or  - o - "
            break

tic_tac_toe()
