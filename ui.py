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
    board = [[' ', '1', '2', '3', '4', '5','6','7','8','9','10'], ['A', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['B', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['C', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['D', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['E', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['F', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['G', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['H', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['I', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ['J', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
    return board

def choose_ship_option():
    user_input = input('''
Choose option: 

    [1] 1-block-long ship 
    [2] 2-blocks-long ship
            
''')
    return user_input

def blocking_more_than_2_blocks(user_input):
    #A
    if user_input == [1,1]:
        available_user_inputs = [[1,2], [2,1]]
        return available_user_inputs
    if user_input == [1,2]:
        available_user_inputs = [[1,1], [2,2], [1,3]]
        return available_user_inputs
    if user_input == [1,3]:
        available_user_inputs = [[1,2], [2,3], [1,4]]
        return available_user_inputs
    if user_input == [1,4]:
        available_user_inputs = [[1,3], [2,4], [1,5]]
        return available_user_inputs
    if user_input == [1,5]:
        available_user_inputs = [[1,4], [2,5], [1,6]]
        return available_user_inputs
    if user_input == [1,6]:
        available_user_inputs = [[1,5], [2,6], [1,7]]
        return available_user_inputs
    if user_input == [1,7]:
        available_user_inputs = [[1,6], [2,7], [1,8]]
        return available_user_inputs
    if user_input == [1,8]:
        available_user_inputs = [[1,7], [2,8], [1,9]]
        return available_user_inputs
    if user_input == [1,9]:
        available_user_inputs = [[1,8], [2,9], [1,10]]
        return available_user_inputs
    if user_input == [1,10]:
        available_user_inputs = [[1,9], [2,10]]
        return available_user_inputs
    #B
    if user_input == [2,1]:
        available_user_inputs = [[1,1], [2,2], [3,1]]
        return available_user_inputs
    if user_input == [2,2]:
        available_user_inputs = [[1,2], [2,1], [3,2], [2,3]]
        return available_user_inputs
    if user_input == [2,3]:
        available_user_inputs = [[1,3], [2,2], [3,3], [2,4]]
        return available_user_inputs
    if user_input == [2,4]:
        available_user_inputs = [[1,4], [2,3], [3,4], [2,5]]
        return available_user_inputs
    if user_input == [2,5]:
        available_user_inputs = [[1,5], [2,4], [3,5], [2,6]]
        return available_user_inputs
    if user_input == [2,6]:
        available_user_inputs = [[1,6], [2,5], [3,6], [2,7]]
        return available_user_inputs
    if user_input == [2,7]:
        available_user_inputs = [[1,7], [2,6], [3,7], [2,8]]
        return available_user_inputs
    if user_input == [2,8]:
        available_user_inputs = [[1,8], [2,7], [3,8], [2,9]]
        return available_user_inputs
    if user_input == [2,9]:
        available_user_inputs = [[1,9], [2,8], [3,9], [2,10]]
        return available_user_inputs
    if user_input == [2,10]:
        available_user_inputs = [[1,10], [2,9], [3,10]]
        return available_user_inputs
#c
    if user_input == [3,1]:
        available_user_inputs = [[2,1], [3,2], [4,1]]
        return available_user_inputs
    if user_input == [3,2]:
        available_user_inputs = [[2,2], [3,1], [4,2], [3,3]]
        return available_user_inputs
    if user_input == [3,3]:
        available_user_inputs = [[2,3], [3,2], [4,3], [3,4]]
        return available_user_inputs
    if user_input == [3,4]:
        available_user_inputs = [[2,4], [3,3], [4,4], [3,5]]
        return available_user_inputs
    if user_input == [3,5]:
        available_user_inputs = [[2,5], [3,4], [4,5], [3,6]]
        return available_user_inputs
    if user_input == [3,6]:
        available_user_inputs = [[2,6], [3,5], [4,6], [3,7]]
        return available_user_inputs
    if user_input == [3,7]:
        available_user_inputs = [[2,7], [3,6], [4,7], [3,8]]
        return available_user_inputs
    if user_input == [3,8]:
        available_user_inputs = [[2,8], [3,7], [4,8], [3,9]]
        return available_user_inputs
    if user_input == [3,9]:
        available_user_inputs = [[2,9], [3,8], [4,9], [3,10]]
        return available_user_inputs
    if user_input == [3,10]:
        available_user_inputs = [[2,10], [3,9], [4,10]]
        return available_user_inputs
#D
    if user_input == [4,1]:
        available_user_inputs = [[3,1], [4,2], [5,1]]
        return available_user_inputs
    if user_input == [4,2]:
        available_user_inputs = [[3,2], [4,1], [5,2], [4,3]]
        return available_user_inputs
    if user_input == [4,3]:
        available_user_inputs = [[3,3], [4,2], [5,3], [4,4]]
        return available_user_inputs
    if user_input == [4,4]:
        available_user_inputs = [[3,4], [4,3], [5,4], [4,5]]
        return available_user_inputs
    if user_input == [4,5]:
        available_user_inputs = [[3,5], [4,4], [5,5], [4,6]]
        return available_user_inputs
    if user_input == [4,6]:
        available_user_inputs = [[3,6], [4,5], [5,6], [4,7]]
        return available_user_inputs
    if user_input == [4,7]:
        available_user_inputs = [[3,7], [4,6], [5,7], [4,8]]
        return available_user_inputs
    if user_input == [4,8]:
        available_user_inputs = [[3,8], [4,7], [5,8], [4,9]]
        return available_user_inputs
    if user_input == [4,9]:
        available_user_inputs = [[3,9], [4,8], [5,9], [4,10]]
        return available_user_inputs
    if user_input == [4,10]:
        available_user_inputs = [[3,10], [4,9], [5,10]]
        return available_user_inputs
#E
    if user_input == [5,1]:
        available_user_inputs = [[4,1], [5,2], [6,1]]
        return available_user_inputs
    if user_input == [5,2]:
        available_user_inputs = [[4,2], [5,1], [6,2], [5,3]]
        return available_user_inputs
    if user_input == [5,3]:
        available_user_inputs = [[4,3], [5,2], [6,3], [5,4]]
        return available_user_inputs
    if user_input == [5,4]:
        available_user_inputs = [[4,4], [5,3], [6,4], [5,5]]
        return available_user_inputs
    if user_input == [5,5]:
        available_user_inputs = [[4,5], [5,4], [6,5], [5,6]]
        return available_user_inputs
    if user_input == [5,6]:
        available_user_inputs = [[4,6], [5,5], [6,6], [5,7]]
        return available_user_inputs
    if user_input == [5,7]:
        available_user_inputs = [[4,7], [5,6], [6,7], [5,8]]
        return available_user_inputs
    if user_input == [5,8]:
        available_user_inputs = [[4,8], [5,7], [6,8], [5,9]]
        return available_user_inputs
    if user_input == [5,9]:
        available_user_inputs = [[4,9], [5,8], [6,9], [5,10]]
        return available_user_inputs
    if user_input == [5,10]:
        available_user_inputs = [[4,10], [5,9], [6,10]]
        return available_user_inputs
#f
    if user_input == [6,1]:
        available_user_inputs = [[5,1], [6,2], [7,1]]
        return available_user_inputs
    if user_input == [6,2]:
        available_user_inputs = [[5,2], [6,1], [7,2], [6,3]]
        return available_user_inputs
    if user_input == [6,3]:
        available_user_inputs = [[5,3], [6,2], [7,3], [6,4]]
        return available_user_inputs
    if user_input == [6,4]:
        available_user_inputs = [[5,4], [6,3], [7,4], [6,5]]
        return available_user_inputs
    if user_input == [6,5]:
        available_user_inputs = [[5,5], [6,4], [7,5], [6,6]]
        return available_user_inputs
    if user_input == [6,6]:
        available_user_inputs = [[5,6], [6,5], [7,6], [6,7]]
        return available_user_inputs
    if user_input == [6,7]:
        available_user_inputs = [[5,7], [6,6], [7,7], [6,8]]
        return available_user_inputs
    if user_input == [6,8]:
        available_user_inputs = [[5,8], [6,7], [7,8], [6,9]]
        return available_user_inputs
    if user_input == [6,9]:
        available_user_inputs = [[5,9], [6,8], [7,9], [6,10]]
        return available_user_inputs
    if user_input == [6,10]:
        available_user_inputs = [[5,10], [6,9], [7,10]]
        return available_user_inputs

        #g
    if user_input == [7,1]:
        available_user_inputs = [[6,1], [7,2], [8,1]]
        return available_user_inputs
    if user_input == [7,2]:
        available_user_inputs = [[6,2], [7,1], [8,2], [7,3]]
        return available_user_inputs
    if user_input == [7,3]:
        available_user_inputs = [[6,3], [7,2], [8,3], [7,4]]
        return available_user_inputs
    if user_input == [7,4]:
        available_user_inputs = [[6,4], [7,3], [8,4], [7,5]]
        return available_user_inputs
    if user_input == [7,5]:
        available_user_inputs = [[6,5], [7,4], [8,5], [7,6]]
        return available_user_inputs
    if user_input == [7,6]:
        available_user_inputs = [[6,6], [7,5], [8,6], [7,7]]
        return available_user_inputs
    if user_input == [7,7]:
        available_user_inputs = [[6,7], [7,6], [8,7], [7,8]]
        return available_user_inputs
    if user_input == [7,8]:
        available_user_inputs = [[6,8], [7,7], [8,8], [7,9]]
        return available_user_inputs
    if user_input == [7,9]:
        available_user_inputs = [[6,9], [7,8], [8,9], [7,10]]
        return available_user_inputs
    if user_input == [7,10]:
        available_user_inputs = [[6,10], [7,9], [8,10]]
        return available_user_inputs
         #h
    if user_input == [8,1]:
        available_user_inputs = [[7,1], [8,2], [9,1]]
        return available_user_inputs
    if user_input == [8,2]:
        available_user_inputs = [[7,2], [8,1], [9,2], [8,3]]
        return available_user_inputs
    if user_input == [8,3]:
        available_user_inputs = [[7,3], [8,2], [9,3], [8,4]]
        return available_user_inputs
    if user_input == [8,4]:
        available_user_inputs = [[7,4], [8,3], [9,4], [8,5]]
        return available_user_inputs
    if user_input == [8,5]:
        available_user_inputs = [[7,5], [8,4], [9,5], [8,6]]
        return available_user_inputs
    if user_input == [8,6]:
        available_user_inputs = [[7,6], [8,5], [9,6], [8,7]]
        return available_user_inputs
    if user_input == [7,7]:
        available_user_inputs = [[7,7], [8,6], [9,7], [8,8]]
        return available_user_inputs
    if user_input == [8,8]:
        available_user_inputs = [[7,8], [8,7], [9,8], [8,9]]
        return available_user_inputs
    if user_input == [8,9]:
        available_user_inputs = [[7,9], [8,8], [9,9], [8,10]]
        return available_user_inputs
    if user_input == [8,10]:
        available_user_inputs = [[7,10], [8,9], [9,10]]
        return available_user_inputs
         #i
    if user_input == [9,1]:
        available_user_inputs = [[8,1], [9,2], [10,1]]
        return available_user_inputs
    if user_input == [9,2]:
        available_user_inputs = [[8,2], [9,1], [10,2], [9,3]]
        return available_user_inputs
    if user_input == [9,3]:
        available_user_inputs = [[8,3], [9,2], [10,3], [9,4]]
        return available_user_inputs
    if user_input == [9,4]:
        available_user_inputs = [[8,4], [9,3], [10,4], [9,5]]
        return available_user_inputs
    if user_input == [9,5]:
        available_user_inputs = [[8,5], [9,4], [10,5], [9,6]]
        return available_user_inputs
    if user_input == [9,6]:
        available_user_inputs = [[8,6], [9,5], [10,6], [9,7]]
        return available_user_inputs
    if user_input == [9,7]:
        available_user_inputs = [[8,7], [9,6], [10,7], [9,8]]
        return available_user_inputs
    if user_input == [9,8]:
        available_user_inputs = [[8,8], [9,7], [10,8], [9,9]]
        return available_user_inputs
    if user_input == [9,9]:
        available_user_inputs = [[8,9], [9,8], [10,9], [9,10]]
        return available_user_inputs
    if user_input == [9,10]:
        available_user_inputs = [[8,10], [9,9], [10,10]]
        return available_user_inputs
    #J
    if user_input == [10,1]:
        available_user_inputs = [[10,2], [9,1]]
        return available_user_inputs
    if user_input == [10,2]:
        available_user_inputs = [[10,1], [9,2], [1,3]]
        return available_user_inputs
    if user_input == [10,3]:
        available_user_inputs = [[10,2], [9,3], [10,4]]
        return available_user_inputs
    if user_input == [10,4]:
        available_user_inputs = [[10,3], [9,4], [10,5]]
        return available_user_inputs
    if user_input == [10,5]:
        available_user_inputs = [[10,4], [9,5], [10,6]]
        return available_user_inputs
    if user_input == [10,6]:
        available_user_inputs = [[10,5], [9,6], [10,7]]
        return available_user_inputs
    if user_input == [10,7]:
        available_user_inputs = [[10,6], [9,7], [10,8]]
        return available_user_inputs
    if user_input == [10,8]:
        available_user_inputs = [[10,7], [9,8], [10,9]]
        return available_user_inputs
    if user_input == [10,9]:
        available_user_inputs = [[10,8], [9,9], [10,10]]
        return available_user_inputs
    if user_input == [10,10]:
        available_user_inputs = [[10,9], [9,10]]
        return available_user_inputs
    #B


    


    