from types import new_class
import data_menager
import ui
import time

FILE_BOARD_ONE = 'Battleship-Game/board_one.cvs'
FILE_BOARD_TWO = 'Battleship-Game/board_two.cvs'

SMALL_BOARD_CODED_ONE = ui.board_small()
SMALL_BOARD_CODED_TWO = ui.board_small()
BIG_BOARD_CODED_ONE = ui.board_big()
BIG_BOARD_CODED_TWO = ui.board_big()

COL = 1
ROW = 0

PLAYER_ONE = 'PLAYER ONE'
PLAYER_TWO = 'PLAYER TWO'

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
    print('\n PLAYER ONE', end = '\t\t')
    print(' PLAYER TWO\n')
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

def ask_for_orientation():
    while True:
        user_input = input("\nPlease enter H for HORIZONTAL (left to right) or V for VERTICAL (up to bottom): ").upper()
        if user_input == 'H':
            return user_input
        if user_input == 'V':
            return user_input
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

def set_ship_on_board(board, ship_cells, file_name):
    for element in ship_cells:
        coordinates_row = element[ROW]
        coordinates_col = element[COL]
        board[coordinates_row][coordinates_col] = 'X'
    data_menager.overwrite_table_to_file(board, file_name)
    return board

def blocking_places_near_ship_horizontal(ship_cells, board_size):
    blocked_cells = []
    for element in ship_cells:
        blocked_cells.append([element[ROW] - 1, element[COL]])
        blocked_cells.append([element[ROW] + 1, element[COL]])
    first = [ship_cells[0]]
    last = [ship_cells[-1]]
    for element in first:
        blocked_cells.append([element[ROW], element[COL] - 1])
    for element in last:
        blocked_cells.append([element[ROW], element[COL] + 1])
    for element in blocked_cells:
        for i in element:
            if board_size == 'big':
                if i > 9:
                    blocked_cells.remove(element)
            if board_size == 'small':
                if i > 5:
                    blocked_cells.remove(element)
    return blocked_cells

def blocking_places_near_ship_vertical(ship_cells, board_size):
    blocked_cells = []
    for element in ship_cells:
        blocked_cells.append([element[ROW], element[COL] + 1])
        blocked_cells.append([element[ROW], element[COL] - 1])
    first = [ship_cells[0]]
    last = [ship_cells[-1]]
    for element in first:
        blocked_cells.append([element[ROW] - 1, element[COL]])
    for element in last:
        blocked_cells.append([element[ROW] + 1, element[COL]])
    for element in blocked_cells:
        for i in element:
            if board_size == 'big':
                if i > 9:
                    blocked_cells.remove(element)
            if board_size == 'small':
                if i > 5:
                    blocked_cells.remove(element)
    return blocked_cells

def set_blocked_place(board, blocked_cells, file_name):
    for element in blocked_cells:
        coordinates_row = element[ROW]
        coordinates_col = element[COL]
        if board[coordinates_row][coordinates_col] in col_title(board) or board[coordinates_row][coordinates_col] in row_title(board) or board[coordinates_row][coordinates_col] in row_title(board) == 'X':
            blocked_cells.remove(element)
    for element in blocked_cells:
        coordinates_row = element[ROW]
        coordinates_col = element[COL]
        board[coordinates_row][coordinates_col] = '-'
    data_menager.overwrite_table_to_file(board, file_name)
    return board

def checking_coordinates(ship_cells, board_size):
    for element in ship_cells:
        for i in element:
            if board_size == 'big':
                if i > 9:
                    return False
            if board_size == 'small':
                if i > 5:
                    return False
    else:
        return True

def check_available_place(board, coordinates):
    coordinates_row = coordinates[ROW]
    coordinates_col = coordinates[COL]
    if board[coordinates_row][coordinates_col] == 'X' or board[coordinates_row][coordinates_col] == '-':
        return False
    else:
        return True

def setting_ship(board, player, board_size, ships_list, file_name):
    print_board(board, player)
    ship_list_coordinates = []
    for boat in ships_list:
        title = (f"Enter starting coordinate (e.g. B4) for the {boat}: ")
        blocks = (ships_list[boat])
        while True:
            user_coordinate = user_coordinates_convert(board, user_coordinates(board, title))
            if check_available_place(board, user_coordinate) == False:
                ui.print_red("\nYou can't put here your ship. Try again")
                continue
            else:
                orientation = ask_for_orientation()
                if orientation == 'H':
                    ship_cells = set_horizontal(blocks, user_coordinate)
                    if checking_coordinates(ship_cells, board_size) == False:
                        ui.print_red('\nThere is no space for this ship. Try again!')
                        continue
                    else:
                        ship_list_coordinates.append(ship_cells)
                        board = set_ship_on_board(board, ship_cells, file_name)
                        blocked_cells = blocking_places_near_ship_horizontal(ship_cells, board_size)
                        board = set_blocked_place(board, blocked_cells, file_name)
                        print_board(board, player)
                        break
                if orientation == 'V':
                    ship_cells = set_vertical(blocks, user_coordinate)
                    if checking_coordinates(ship_cells, board_size) == False:
                        ui.print_red('\nThere is no space for this ship. Try again!')
                        continue
                    else:
                        ship_list_coordinates.append(ship_cells)
                        board = set_ship_on_board(board, ship_cells, file_name)
                        blocked_cells = blocking_places_near_ship_vertical(ship_cells, board_size)
                        board = set_blocked_place(board, blocked_cells, file_name)
                        print_board(board, player)
                        break
    return ship_list_coordinates

def confirm_ships():
    ui.print_green('\nPress ENTER to hide your ships')
    input()
    time.sleep(0)
    for i in range(0,50):
        print('')

def checking_shoot(coordinates, board):
    coordinates_row = coordinates[ROW]
    coordinates_col = coordinates[COL]
    if board[coordinates_row][coordinates_col] == 'X':
        return 'shoot'
    if board[coordinates_row][coordinates_col] == '~' or board[coordinates_row][coordinates_col] == '-':
        return 'missed'

def sink_the_ship(board, ship_list):
    true_false_check = []
    counter = 1
    for sublist in ship_list:
        ships_sign = []
        for element in sublist:
            ships_sign.append(board[element[ROW]][element[COL]])
        check = set(ships_sign)
        if check == {'▬'}:
            true_false_check.append(0 + counter)
            counter += 1
        else:
            true_false_check.append(False)
    for element in true_false_check:
        if type(element) == int:
            ship_index = true_false_check.index(element)
            for coordination in ship_list[ship_index]:
                board[coordination[ROW]][coordination[COL]] = '▼'
            print('You sink the ship!')
    return board

def check_winner(board, ships_quantity):
    one_list = []
    for sublist in board:
        for item in sublist:
            one_list.append(item)
    if one_list.count('▼') == ships_quantity:
        return True
    else:
        return False

def shooting_the_ships(board_one, board_two, board_plr_one, board_plr_two, ship_list_one, ship_list_two, ships_quantity):
    ui.shooting_info()
    print_two_boards(board_one, board_two)
    while check_winner(board, ships_quantity) == True: 
        title_one = (f"PLAYER ONE: Enter coordinate: ")
        user_coordinate = user_coordinates_convert(board_two, user_coordinates(board_two, title_one))
        shoot = checking_shoot(user_coordinate, board_plr_two)
        if shoot == 'shoot':
            board_two[user_coordinate[ROW]][user_coordinate[COL]] = '▬'
            ui.print_green("\nYou hit the ship!")
            sink_the_ship(board_two, ship_list_two)
            print(check_winner(board_two, ships_quantity))
            if check_winner(board_two, ships_quantity) == True:
                ui.winner()
                print('PLAYER ONE win the battle!')
                break
        if shoot == 'missed':
            board_two[user_coordinate[ROW]][user_coordinate[COL]] = 'Ø'
            ui.print_red("\nYou missed the ship!")
        print_two_boards(board_one, board_two)
        title_two = (f"PLAYER TWO: Enter coordinate: ")
        user_coordinate = user_coordinates_convert(board_one, user_coordinates(board_one, title_two))
        shoot = checking_shoot(user_coordinate, board_plr_one)
        if shoot == 'shoot':
            board_one[user_coordinate[ROW]][user_coordinate[COL]] = '▬'
            ui.print_green("\nYou hit the ship!")
            sink_the_ship(board_one, ship_list_one)
            if check_winner(board_two, ships_quantity) == True:
                ui.winner()
                print('\nPLAYER TWO win the battle!')
                break
        if shoot == 'missed':
            board_one[user_coordinate[ROW]][user_coordinate[COL]] = 'Ø'
            ui.print_red("\nvb dfvbYou missed the ship!")
        print_two_boards(board_one, board_two)

def main():
    ui.start_title()
    board_size = choose_board()
    board_plr_one = data_menager.get_table_from_file('Battleship-Game/board_one.cvs')
    board_plr_two = data_menager.get_table_from_file('Battleship-Game/board_two.cvs')
    if board_size == 'big':
        ships_list = {'Carrier (5 blocks)': 5, 'Battleship (4 blocks)': 4, 'Cruiser (3 blocks)': 3, 'Submarine (3 blocks)': 3, 'Submarine 2 (3 blocks)': 3, 'Destroyer (2 blocks)': 2, 'Destroyer 2 (2 blocks)': 2, 'Destroyer 3 (2 blocks)': 2} #24
        board_one = BIG_BOARD_CODED_ONE
        board_two = BIG_BOARD_CODED_TWO
        ships_quantity = 24
    if board_size == 'small':
        ships_list = {'Submarine (3 blocks)': 3, 'Destroyer (2 blocks)': 2, 'Destroyer 2 (2 blocks)': 2} #6
        board_one = SMALL_BOARD_CODED_ONE
        board_two = SMALL_BOARD_CODED_TWO
        ships_quantity = 7
    available_ships(board_size, PLAYER_ONE)
    ship_list_one = setting_ship(board_plr_one, PLAYER_ONE, board_size, ships_list, FILE_BOARD_ONE)
    confirm_ships()
    available_ships(board_size, PLAYER_TWO)
    ship_list_two = setting_ship(board_plr_two, PLAYER_TWO, board_size, ships_list, FILE_BOARD_TWO)
    confirm_ships()
    ui.lets_start()
    shooting_the_ships(board_one, board_two, board_plr_one, board_plr_two, ship_list_one, ship_list_two, ships_quantity)




if __name__ == '__main__':
    main()

