import data_menager
import ui

BOARD_PLR_ONE = data_menager.get_table_from_file('Battleship-Game/board_one.cvs') 
BOARD_PLR_TWO = data_menager.get_table_from_file('Battleship-Game/board_two.cvs')


COL = 1
ROW = 0

def choose_board():
    while True:
        user_input = input('Do you wanna play big or small board? [B] BIG / [S] SMALL: ').upper()
        if user_input == 'B':
            board = ui.board_big()
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_one.cvs')
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_two.cvs')
            break
        if user_input == 'S':
            board = ui.board_small()
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_one.cvs')
            data_menager.overwrite_table_to_file(board, 'Battleship-Game/board_two.cvs')
            break
        else:
            ui.print_red('\nYou should choose [B] or [S]! Try again.\n')            
            continue  

choose_board()

def print_board(board, player):
    ui.print_red('\n ' + player + '\n')
    for sublist in board:
        print(' '.join(sublist))

def print_two_boards(board_one, board_two):
    ui.print_red('\n PLAYER ONE', end = '\t\t')
    ui.print_red(' PLAYER TWO\n')
    for i in range(0,6):
        print(' '.join(board_one[i]), end = "\t\t")
        print(' '.join(board_two[i]))

def col_title(board):
    print(board)
    col_title = board[0]
    return col_title   #[' ', '1', '2', '3', '4', '5']

def row_title(board):
    row_title = []
    for sublist in board:
        row_title.append(sublist[0])
    return row_title  #[' ', 'A', 'B', 'C', 'D', 'E']

def user_coordinates(board):   
    while True:
        user_input = input('Please provide a coordinates: ').upper()
        if len(user_input) < 2 or not user_input[ROW].isalpha() or not user_input[COL].isnumeric():
            ui.print_red('\nWrong! You should write B4, A1, G7 etc etc.')
            continue
        else:
            if user_input[ROW] not in row_title(board) or user_input[COL] not in col_title(board):
                ui.print_red('Wrong! Try again')
                continue
            break
    return user_input

def user_coordinates_convert(board, user_input):
    user_input_convert = []
    for element in row_title(board):
        if element == user_input[ROW]:
            row_index = row_title(board).index(element)
            user_input_convert.append(row_index)
    for element in col_title(board):
        if element == user_input[COL]:
            col_index = col_title(board).index(element)
            user_input_convert.append(col_index)
    return user_input_convert

def set_ships():
    pass

def main():
    ui.start_title()

if __name__ == '__main__':
    main()

