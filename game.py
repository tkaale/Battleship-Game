import data_menager
import ui

BOARD_PLR_ONE = data_menager.get_table_from_file('Battleship-Game/board_one.cvs') 
BOARD_PLR_TWO = data_menager.get_table_from_file('Battleship-Game/board_two.cvs')

FILE_BOARD_ONE = 'Battleship-Game/board_one.cvs'
FILE_BOARD_TWO = 'Battleship-Game/board_two.cvs'
COL = 1
ROW = 0

def choose_board():
    while True:
        user_input = input('Do you wanna play big or small board? [B] BIG / [S] SMALL: ').upper()
        if user_input == 'B':
            board = ui.board_big()
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_one.cvs')
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_two.cvs')
            ui.print_green('\nYou choose BIG board.\n')
            break
        if user_input == 'S':
            board = ui.board_small()
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_one.cvs')
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_two.cvs')
            ui.print_green('\nYou choose SMALL board.\n')
            break
        else:
            ui.print_red('\nYou should choose [B] or [S]! Try again.\n')            
            continue  

def print_board(board, player):
    ui.print_red(f'\n {player}\n')
    for sublist in board:
        print(' '.join(sublist))

def print_two_boards(board_one, board_two):
    ui.print_red('\n PLAYER ONE', end = '\t\t')
    ui.print_red(' PLAYER TWO\n')
    for i in range(0,6):
        print(' '.join(board_one[i]), end = "\t\t")
        print(' '.join(board_two[i]))

def col_title(board):
    col_title = board[0]
    return col_title   #[' ', '1', '2', '3', '4', '5']

def row_title(board):
    row_title = []
    for sublist in board:
        row_title.append(sublist[0])
    return row_title  #[' ', 'A', 'B', 'C', 'D', 'E']

def user_coordinates(board, title):   
    while True:
        user_input = input(f'\n{title}').upper()
        if len(user_input) < 2 or not user_input[ROW].isalpha() or not user_input[COL].isnumeric():
            ui.print_red('\nWrong! You should write B4, A1, G7 etc etc.')
            continue
        else:
            if user_input[ROW] not in row_title(board) or user_input[COL] not in col_title(board):
                ui.print_red('Wrong! Try again')
                continue
            else:
                break
    return user_input

def user_coordinates_convert(board, user_input):
    user_input_convert = []
    for element in row_title(board):
        if element == user_input[ROW]:
            row_index = row_title(board).index(element)
            user_input_convert.append(int(row_index))
    for element in col_title(board):
        if element == user_input[COL]:
            col_index = col_title(board).index(element)
            user_input_convert.append(int(col_index))
    return user_input_convert

def set_ships(player, blocks, board):
    print(f"\nIt's time for {player} to set ships.\nShips can be only 1-block long and 2-blocks long. You have {blocks} blocks to use.\nPress ENTER to continue")
    input()
    ships = []
    print_board(board, player)
    while blocks > 0:
        ui.print_green(f"\nAmount of blocks to use: {blocks}")
        user_input = ui.choose_ship_option()
        while True:
            if user_input == '1':
                coordinates = user_coordinates_convert(board, user_coordinates(board, "Please provide coordinates: ")) 
                board = set_ship_on_board(board,coordinates)
                print_board(board, player)
                blocks -= 1
                ships.append([coordinates])
                break
            if user_input == '2':
                if blocks == 1:
                    ui.print_red('\nYou can only set 1-block-long ship!')
                    break
                else:
                    coordinates_one = user_coordinates_convert(board, user_coordinates(board, "Please provide start coordinates: "))
                    coordinates_two = user_coordinates_convert(board, user_coordinates(board, "Please provide end coordinates: "))
                    check_coordinates = ui.blocking_more_than_2_blocks(coordinates_one)
                    if coordinates_two in check_coordinates:
                        board = set_ship_on_board(board, coordinates_one)
                        board = set_ship_on_board(board, coordinates_two)
                        print_board(board, player)
                        blocks -= 2
                        ships.append([coordinates_one, coordinates_two])
                        break
                    else:
                        ui.print_red("\nYou choose 2-block-long ship. \nYou have to set your ship next to first block. Try again")
            else:
                ui.print_red('\nThere is no such option.')
                break
    return ships

def set_ship_on_board(board,coordinates):
    coordinates_row = coordinates[ROW]
    coordinates_col = coordinates[COL]
    if board[coordinates_row][coordinates_col] == 'X':
        print('You already set here a ship')
    else:
        board[coordinates_row][coordinates_col] = 'X'
    return board

#print(set_1_long_ship(BOARD_PLR_ONE, [1,1]))
        

 


    

set_ships('PLAYER ONE', 6, BOARD_PLR_ONE)

def main():
    # ui.start_title()
    # choose_board()
    pass

if __name__ == '__main__':
    main()

