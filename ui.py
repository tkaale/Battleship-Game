import time
import sys
import os
os.system("")

def print_red(skk): print("\033[91m{}\033[00m" .format(skk))
def print_green(skk): print("\033[92m {}\033[00m" .format(skk))
def print_yellow(skk): print("\033[93m {}\033[00m" .format(skk))

def start_title():
    title = "  BATTLESHIP"
    print('')
    for i in title:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
    print_red('''

  ____       _______ _______ _      ______  _____ _    _ _____ _____  
 |  _ \   /\|__   __|__   __| |    |  ____|/ ____| |  | |_   _|  __ \ 
 | |_) | /  \  | |     | |  | |    | |__  | (___ | |__| | | | | |__) |
 |  _ < / /\ \ | |     | |  | |    |  __|  \___ \|  __  | | | |  ___/ 
 | |_) / ____ \| |     | |  | |____| |____ ____) | |  | |_| |_| |     
 |____/_/    \_\_|     |_|  |______|______|_____/|_|  |_|_____|_|     
                            
                            
    ''')

def board_small():
    board = [[' ', '1', '2', '3', '4', '5'], ['A', '~', '~', '~', '~', '~'], ['B', '~', '~', '~', '~', '~'], ['C', '~', '~', '~', '~', '~'], ['D', '~', '~', '~', '~', '~'], ['E', '~', '~', '~', '~', '~']]
    return board

def board_big():
    board = [[' ', '1', '2', '3', '4', '5','6','7','8','9'], ['A', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['B', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['C', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['D', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['E', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['F', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['G', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['H', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['I', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
    return board


def big_board_info(player):
    print(f'''It's time for {player} to set ships. You have the following boats to use:\n
            -> Carrier (5 blocks)
            -> Battleship (4 blocks)
            -> Cruiser (3 blocks)
            -> 2x Submarine (3 blocks)
            -> 3x Destroyer (2 blocks)
        \nPress ENTER to set ships in the following order''')
    input()


def small_board_info(player):
    print(f'''It's time for {player} to set ships. You have the following boats to use:\n
            -> Submarine (3 blocks)
            -> 2x Destroyer (2 blocks)
        \nPress ENTER to set ships in the following order''')
    input()

def lets_start():
    print_red('''
    
  _      ______ _______ _  _____    _____ _______       _____ _______ _ 
 | |    |  ____|__   __( )/ ____|  / ____|__   __|/\   |  __ \__   __| |
 | |    | |__     | |  |/| (___   | (___    | |  /  \  | |__) | | |  | |
 | |    |  __|    | |     \___ \   \___ \   | | / /\ \ |  _  /  | |  | |
 | |____| |____   | |     ____) |  ____) |  | |/ ____ \| | \ \  | |  |_|
 |______|______|  |_|    |_____/  |_____/   |_/_/    \_\_|  \_\ |_|  (_)
                                                                        
                                                                        

    ''')
    input('Press ENTER to continue...')


def shooting_info():
    print_yellow('''\nYou have one shoot per round. 
     --> when you missed the ship, there will be [Ø]
     --> when you shoot one part of the ship, there will be [▬]
     --> when you sink all ship, there will be [▼]''')
    print_green('\nPLAYER ONE is starting.')

def winner():
    print_green('''
    
 __          _______ _   _ _   _ ______ _____  _ 
 \ \        / /_   _| \ | | \ | |  ____|  __ \| |
  \ \  /\  / /  | | |  \| |  \| | |__  | |__) | |
   \ \/  \/ /   | | | . ` | . ` |  __| |  _  /| |
    \  /\  /   _| |_| |\  | |\  | |____| | \ \|_|
     \/  \/   |_____|_| \_|_| \_|______|_|  \_(_)
                                                 
                                                 
''')








