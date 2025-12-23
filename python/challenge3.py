
# Python Advanced Challenge: Tic-Tac-Toe Game
#
# Objective: Build a complete Tic-Tac-Toe game where two players (human vs human or human vs simple AI) take turns placing marks on a 3x3 grid. Detect wins, draws, and invalid moves. Include options for game mode and replay.
#
# Requirements:
# - Display the 3x3 grid clearly. x
# - Alternate turns between players (X and O). x
# - Validate moves (spot must be empty, within bounds). x
# - Check for win conditions (rows, columns, diagonals) after each move. x
# - Handle draws (full board, no winner). x
# - Offer game modes: Human vs Human, or Human vs AI (AI makes random valid moves). STILL NEEDED
# - Implement replay logic. x
# - Use functions/classes for organization (e.g., a Board class). x
#
# Hints:
# - Use a list of lists for the board: board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# - Loop for turns: while not game_over.
# - Win check: Check rows, cols, diags for three in a row.
# - AI: Use random.choice() for available spots.
# - Display: Print the board with indices.
#
# Bonus: Add difficulty levels for AI (e.g., unbeatable), or save/load games. STILL NEEDED
#
# Write your code below this comment block.

# Your code here


#TODO things needed still
# - add computer player  x
# - factor in how that might affect game play.  x 
# - adding difficulty levels (not yet)
import random

class Board:
    def __init__(self):
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def display(self):
        print()
        print(f"{game_board.board[0][0]} | {game_board.board[0][1]} | {game_board.board[0][2]}")
        print("--+---+--")
        print(f"{game_board.board[1][0]} | {game_board.board[1][1]} | {game_board.board[1][2]}")
        print("--+---+--")
        print(f"{game_board.board[2][0]} | {game_board.board[2][1]} | {game_board.board[2][2]}")
        print()
    


def display_menu():
    print("""
 /xxooxox /xx                 /oxxoxoox                        /xooxoxoox                 
|__  xx__/|__/                |__  oo__/                       |__  xx__/                 
   | ox    /xo  /ooxoxxo         | xo  /xooxox   /xooxoxo         | xx  /xooxxo   /xooxox 
   | oo   | oo /ox_____/         | ox |____  xx /ox_____/         | oo /xx__  xo /oo__  xx
   | xo   | ox| xx               | xx  /xooxoxx| ox               | xo| xx  \ oo| ooxxoxox
   | ox   | xx| xo               | xx /oo__  xx| xx               | ox| oo  | xx| xo_____/
   | xx   | oo|  xooxxox         | xo|  ooxoxxo|  xooxxox         | oo|  xxoxxo/|  xoxxox
   |__/   |__/ \_______/         |__/ \_______/ \_______/         |__/ \______/  \_______/
                                                                                          
                                                                                          
                                                                                          """)

# function to map input of 1-9 from user to board coordinates
def map_move(move):
    place = move -1
    row = place // 3
    col = place % 3
    return row, col

def get_move(player):
    while True:
        # user input comes from here
        input_move = input("enter your a number from 1-9 for your move: ")
        # move validation 
        try:
            move = int(input_move) #convert input to integer
            if move > 9 or move < 1:
                print("Not a valid move, chose a number between 1-9")
                continue
            if game_board.board[(move-1) //3][(move-1) % 3].isalpha():
                print('That spot is already in play, try another one')
                continue
            else:
                # map the input to a board position and replace the number withan x or o depending on who's turn it is
                game_board.board[(move-1) //3][(move-1) % 3] = player
                break

        except ValueError:
            print("not a valid move, chose a number")
    
# implement win cases
def check_for_win():
    # horizontal line
    for row in range(3):
        if game_board.board[row][0] == game_board.board[row][1] == game_board.board[row][2]:
            return True
    # vertical line check
    for col in range(3):
        if game_board.board[0][col] == game_board.board[1][col] == game_board.board[2][col]:
            return True
    # there is only 2 diagonal possibilites so we can check for them explicitly
    if game_board.board[0][0] == game_board.board[1][1] == game_board.board[2][2]:
            return True
    if game_board.board[0][2] == game_board.board[1][1] == game_board.board[2][0]:
        return True
    #if none of these cases are reached return false and keep playing
    else:
        return False

# no decision tree, just make random moves in valid spots
def easy_ai(player):
    # new implementation of easy_ai, but without recursion.  going to try and create a list of available moves then use random.choice to make the play, 
    # this way I can also handle the no move available case better.
    moves = []
    for i in range(3):
        for j in range(3):
            if game_board.board[i][j] not in ['x','o']:
                moves.append(game_board.board[i][j])
    if not moves:
        return
    else:
        ai_move = int(random.choice(moves) )
        game_board.board[(ai_move-1) //3][(ai_move-1) % 3] = player

def find_empty_space(line, player):
    # add one for each item in line if that item is player (x or o) and add one for each item in line if time is not x or o
    # that basically checks if two elements in a line are an x or an o and one is not, this passes
    if sum(1 for item in line if item == player) == 2 and sum(1 for item in line if item not in ['x','o']) == 1:
        for i, item in enumerate(line):
                if item not in ['x','o']:
                    empty_spot = i
                    return empty_spot

def ai_move(player, is_player):
    moved = False
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    for row in range(3):
        if not moved:
            line = game_board.board[row]
            empty_spot = find_empty_space(line, player)
            if empty_spot is not None:
                if not is_player:
                    game_board.board[row][empty_spot] = opponent
                else:
                    game_board.board[row][empty_spot] = player
                moved = True
                return moved
    
    for col in range(3):
        if not moved:
            line = [game_board.board[r][col] for r in range(3)] # I don't understand this syntax, specifically the bracket on the outside ask about that
            empty_spot = find_empty_space(line, player)
            if empty_spot is not None:
                if not is_player:
                    game_board.board[empty_spot][col] = opponent
                else:
                    game_board.board[empty_spot][col] = player
                moved = True
                return moved

    if not moved:
        line = [game_board.board[0][0], game_board.board[1][1],game_board.board[2][2]]
        empty_spot = find_empty_space(line, player)
        if empty_spot is not None:
            if not is_player:
                game_board.board[empty_spot][empty_spot] = opponent
            else:
                game_board.board[empty_spot][empty_spot] = player
            moved = True
            return moved
    
    if not moved:
        line = [game_board.board[0][2], game_board.board[1][1],game_board.board[2][0]]
        empty_spot = find_empty_space(line, player)
        if empty_spot is not None:
            if not is_player:
                game_board.board[empty_spot][2 - empty_spot] = opponent
            else:
                game_board.board[empty_spot][2 - empty_spot] = player  
            moved = True
            return  moved

# check for a win and acts accordingly, random elsewise
def medium_ai(player):
    # check for 2 out of three situation, and place it there, this should work for blocking, but isn't
    moved = False
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    # check for win case before blocking 
    moved = ai_move(player, True)
    if not moved:
        # next check for blocks
        moved = ai_move(opponent, False)
    # if no win or block go with a random free space
    if not moved:
        easy_ai(player)

# TODO learn and implement minimax algorithm, probably want to come back to this after learning more.
# def hard_ai(player):


def man_or_machine():
    try:
        game_type = int(input("""Chose your oponent:
                1: Human vs Human
                2: Human vs Computer \n"""))
        if game_type == 1:
            print("PvP")
            return 1
        elif game_type == 2:
            print("War of the machines")
            return 2
        else:
            print("you must chose 1 or 2")
            man_or_machine()
    except ValueError:
            print('I didn\'t understand that, try again')
            man_or_machine()


def play_game(game_type):
    # prints the board, might want to make this prettier later
    turn_count = 0
    game_over = False
    while not game_over:
        if turn_count % 2 == 0:
            player = 'x'
        if turn_count % 2 == 1:
            player = 'o'
        game_board.display()
            
        if game_type == 2 and turn_count % 2 == 1:
            easy_ai(player)
            turn_count += 1
        elif game_type == 3 and turn_count % 2 == 1:
            medium_ai(player)
            turn_count += 1
        else:
            get_move(player)
            turn_count += 1
        if check_for_win():
            print(f"Congrats {player} wins!")
            game_over = True
            game_board.display()
        if turn_count > 9:
            print("Game was a draw")
            game_over = True
            game_board.display()
        

# play and replay implementation borrowed and improved upon from previous challenges
while True:
    display_menu()
    play_again = input('Do you want to play A game y/n: ').strip().lower()
    if play_again == 'y':
        game_type = man_or_machine()
        if game_type == 2:
            print("Select difficulty:")
            difficulty= int(input("""
                1: easy 
                2: Hard 
                  """))
            if difficulty == 2:
                game_type = 3
        game_board = Board()
        play_game(game_type)
    else:
        break




# What I learned doing this:
# 1. I learned about classes, and how to use instances of a class 
# 2. I learned a lot about dealing with 2d matricies and traversing them to find specific cases
# 3. I learned How long complex files can sometimes be difficult to traverse and remember states through it all.
