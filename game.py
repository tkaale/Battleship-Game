import data_menager
import ui
import time

FILE_BOARD_ONE = 'Battleship-Game/board_one.cvs'
FILE_BOARD_TWO = 'Battleship-Game/board_two.cvs'

COL = 1
ROW = 0

PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

board_ii = data_menager.get_table_from_file(FILE_BOARD_ONE)

def choose_board():
    while True:
        user_input = input('Do you wanna play big or small board? [B] BIG / [S] SMALL: ').upper()
        if user_input == 'B':
            board = ui.board_big()
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_one.cvs')
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_two.cvs')
            ui.print_green('\nYou choose BIG board.\n')
            board_size = 'big'
            return board_size
        if user_input == 'S':
            board = ui.board_small()
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_one.cvs')
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_two.cvs')
            ui.print_green('\nYou choose SMALL board.\n')
            board_size = 'small'
            return board_size
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
    return col_title

def row_title(board):
    row_title = []
    for sublist in board:
        row_title.append(sublist[0])
    return row_title

def user_coordinates(board, title):   
    while True:
        user_input = input(f'\n{title}').upper()
        if len(user_input) < 2 or not user_input[ROW].isalpha() or not user_input[COL].isnumeric():
            ui.print_red('\nWrong! You should write B4, A1, G7 etc etc.')
            continue
        else:
            if user_input[ROW] not in row_title(board) or user_input[COL] not in col_title(board):
                ui.print_red('\nWrong! Try again')
                continue
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

def available_ships(board_size, player):
    if board_size == 'big':
        ui.big_board_info(player)
    if board_size == 'small':
        ui.small_board_info(player)

def ask_for_orientation(blocks, user_coordinate):
    while True:
        user_input = input("Please enter H for HORIZONTAL (left to right) set or V for VERTICAL (up to bottom) set: ").upper()
        if user_input == 'H':
            ship_cells = set_horizontal(blocks, user_coordinate)
            return ship_cells
        if user_input == 'V':
            ship_cells = set_vertical(blocks, user_coordinate)
            return ship_cells
        else:
            ui.print_red("Wrong! You should write H or V!")
            continue

def set_horizontal(blocks, user_coordinate):
    ship_cells = []
    for i in range(0, blocks):
        ship_cells.append(user_coordinate)
        user_coordinate = [user_coordinate[ROW], user_coordinate[COL] + 1]
    return ship_cells

def set_vertical(blocks, user_coordinate):
    ship_cells = []
    for i in range(0, blocks):
        ship_cells.append(user_coordinate)
        user_coordinate = [user_coordinate[ROW] + 1, user_coordinate[COL]]
    return ship_cells


def set_ship_on_board(board, ship_cells):
    for element in ship_cells:
        coordinates_row = element[ROW]
        coordinates_col = element[COL]
        board[coordinates_row][coordinates_col] = 'X'
    return board


def setting_ship_big(board, player):
    ships_list_big = {'Carrier (5 blocks)': 5, 'Battleship (4 blocks)': 4, 'Cruiser (3 blocks)': 3, 'Submarine (3 blocks)': 3, 'Submarine (3 blocks)': 3, 'Destroyer (2 blocks)': 2, 'Destroyer (2 blocks)': 2, 'Destroyer (2 blocks)': 2}
    for boat in ships_list_big:
        print_board(board, player)
        title = (f"Enter starting coordinate (e.g. B4) for the {boat}: ")
        blocks = (ships_list_big[boat])
        user_coordinate = user_coordinates_convert(board, user_coordinates(board, title))
        ship_cells = ask_for_orientation(blocks, user_coordinate)
        board = set_ship_on_board(board, ship_cells)
        print_board(board, player)

setting_ship_big(board_ii, "player one") 


def setting_ship_small(board, player):
    ship_list_small = {'Submarine (3 blocks)': 3, 'Destroyer (2 blocks)': 2, 'Destroyer (2 blocks)': 2}




# def setting_ships_info(board, player, blocks):
#     print(f"\nIt's time for {player} to set ships.\nShips can be only 1-block long and 2-blocks long. You have {blocks} blocks to use.\nPress ENTER to continue")
#     input()
#     print_board(board, player)

# def set_ships(player, blocks, board):
#     setting_ships_info(board, player,blocks)
#     ships = []
#     while blocks > 0:
#         ui.print_green(f"\nAmount of blocks to use: {blocks}")
#         user_input = ui.choose_ship_option()
#         while True:
#             if user_input == '1':
#                 coordinates = user_coordinates_convert(board, user_coordinates(board, "Please provide coordinates: ")) 
#                 check_coordinates = check_if_place_available(board, coordinates)
#                 if check_coordinates == True:
#                     board = set_ship_on_board(board,coordinates)
#                     print_board(board, player)
#                     blocks -= 1
#                     ships.append([coordinates])
#                     break
#                 break
#             if user_input == '2':
#                 if blocks == 1:
#                     ui.print_red('\nYou can only set 1-block-long ship!')
#                     break
#                 else:
#                     coordinates_one = user_coordinates_convert(board, user_coordinates(board, "Please provide start coordinates: "))
#                     check_coordinates = check_if_place_available(board, coordinates_one)
#                     if check_coordinates == True:
#                         coordinates_two = user_coordinates_convert(board, user_coordinates  (board, "Please provide end coordinates: "))
#                         check_coordinates = check_if_place_available(board, coordinates_two)
#                         if check_coordinates == True:
#                             check_coordinates_places = ui.blocking_more_than_2_blocks   (coordinates_one)
#                             if coordinates_two in check_coordinates_places:
#                                 board = set_ship_on_board(board, coordinates_one)
#                                 board = set_ship_on_board(board, coordinates_two)
#                                 print_board(board, player)
#                                 blocks -= 2
#                                 ships.append([coordinates_one, coordinates_two])
#                                 break
#                             else:
#                                 ui.print_red("\nYou choose 2-block-long ship. \nYou have to set second block next to first block. Try again")
#                         break
#                     break
#             else:
#                 ui.print_red('\nThere is no such option.')
#                 break
#     return ships


# def set_ship_on_board(board,coordinates):
#     coordinates_row = coordinates[ROW]
#     coordinates_col = coordinates[COL]
#     board[coordinates_row][coordinates_col] = 'X'
#     return board
        
# def check_if_place_available(board, coordinates):
#     coordinates_row = coordinates[ROW]
#     coordinates_col = coordinates[COL]
#     if board[coordinates_row][coordinates_col] == 'X':
#         ui.print_red('\nYou already set here a ship. Try again')
#         return False
#     else:
#         return True







def confirm_ships():
    ui.print_green('\nPress ENTER to hide your ships')
    input()
    time.sleep(0)
    for i in range(0,50):
        print('')

# def main():
#     ui.start_title()
#     blocks = choose_board()
#     board_plr_one = data_menager.get_table_from_file('Battleship-Game/board_one.cvs')
#     board_plr_two = data_menager.get_table_from_file('Battleship-Game/board_two.cvs')
#     ships_player_one = set_ships(PLAYER_ONE, blocks, board_plr_one)
#     confirm_ships()
    
#     ships_player_two = set_ships(PLAYER_TWO, blocks, board_plr_two)
#     confirm_ships()
#     pass

# if __name__ == '__main__':
#     main()

