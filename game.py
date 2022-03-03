import os
os.system("")
import data_menager

def print_red(skk): print("\033[91m{}\033[00m" .format(skk))

BOARD_PLR_ONE = data_menager.get_table_from_file('Battleship-Game/board_one.cvs') 
BOARD_PLR_TWO = data_menager.get_table_from_file('Battleship-Game/board_two.cvs')\

def print_board(board, player):
    print_red('\n ', player, '\n')
    for sublist in board:
        print(' '.join(sublist))

def print_two_boards(board_one, board_two):
    print_red('\n PLAYER ONE', end = '\t\t')
    print_red(' PLAYER TWO\n')
    for i in range(0,6):
        print(' '.join(board_one[i]), end = "\t\t")
        print(' '.join(board_two[i]))

def main():
    pass

if __name__ == '__main__':
    main()

