# SIMPLE GAME OF TIC TAC TOE WILL PROGRSS LATER

import time
import sys
import math
from IPython.display import clear_output
import random

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def player_ip():
    choice = ''
    while choice.upper() not in ['X','O']:
        type_text("Please enter the choice of Player 1: 'X' or 'O'")
        choice = input().upper()
        if choice not in ['X','O']:
            type_text("⚠️ Invalid choice! Please enter 'X' or 'O' only.", 0.04)
            clear_output()
    return choice
     
def print_board(mlist):
    for i in range(3):
        row = " | ".join(f" {cell} " for cell in mlist[i])
        print(row)
        if i < 2:
            print("===============")
    
print_board([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])

def place_marker(posX,posY, choice, mlist):
    mlist[posX][posY] = choice
    return mlist

def win_check(mlist,choice):
    #ROWS:
    if mlist[0][0] == mlist[0][1] and mlist[0][1] == mlist[0][2] and mlist[0][2] == choice:
        return True
    elif mlist[1][0] == mlist[1][1] and mlist[1][1] == mlist[1][2] and mlist[1][2] == choice:
        return True
    elif mlist[2][0] == mlist[2][1] and mlist[2][1] == mlist[2][2] and mlist[2][2] == choice:
        return True
    
    #DIAGONAL:
    elif mlist[0][0] == mlist[1][1] and mlist[1][1] == mlist[2][2] and mlist[2][2] == choice:
        return True
    elif mlist[0][2] == mlist[1][1] and mlist[1][1] == mlist[2][0] and mlist[2][0] == choice:
        return True
    
    #COLUMNS:
    elif mlist[0][0] == mlist[1][0] and mlist[1][0] == mlist[2][0] and mlist[2][0] == choice:
        return True
    elif mlist[0][1] == mlist[1][1] and mlist[1][1] == mlist[2][1] and mlist[2][1] == choice:
        return True
    elif mlist[0][2] == mlist[1][2] and mlist[1][2] == mlist[2][2] and mlist[2][2] == choice:
        return True

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(posX, posY,mlist):
    return mlist[posX][posY] == ' '

def full_board_check(mlist):
    for i in range(3):
        for j in range(3):
            if space_check(i, j, mlist):  # ✅ FIXED ORDER
                return False
    return True

def player_choice(mlist):
    while True:
        try:
            posX = int(input('Choose your next posX (0-2): '))
            posY = int(input('Choose your next posY (0-2): '))
            if posX in [0,1,2] and posY in [0,1,2]:
                if space_check(posX, posY, mlist):
                    return posX, posY
                else:
                    print("That spot is already taken.")
            else:
                print("Invalid input. Choose values from 0 to 2.")
        except ValueError:
            print("Please enter a valid integer.")

def play_game():
    type_text("🎮 Welcome to Tic Tac Toe! 🎮", 0.07)
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player1_marker = player_ip()
    player2_marker = 'O' if player1_marker.upper() == 'X' else 'X'
    
    turn = choose_first()
    type_text(f"🔄 {turn} will go first.\n", 0.06)
    
    game_on = True
    
    while game_on:
        print_board(board)
        
        if turn == 'Player 1':
            type_text("👉 Player 1's turn", 0.05)
            posX, posY = player_choice(board)
            board = place_marker(posX, posY, player1_marker, board)

            if win_check(board, player1_marker):
                print_board(board)
                type_text("🏆 Player 1 wins!", 0.07)
                game_on = False
            elif full_board_check(board):
                print_board(board)
                type_text("🤝 It's a draw!", 0.07)
                game_on = False
            else:
                turn = 'Player 2'
        else:
            type_text("👉 Player 2's turn", 0.05)
            posX, posY = player_choice(board)
            board = place_marker(posX, posY, player2_marker, board)

            if win_check(board, player2_marker):
                print_board(board)
                type_text("🏆 Player 2 wins!", 0.07)
                game_on = False
            elif full_board_check(board):
                print_board(board)
                type_text("🤝 It's a draw!", 0.07)
                game_on = False
            else:
                turn = 'Player 1'

play_game()
