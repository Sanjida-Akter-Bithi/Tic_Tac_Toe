# -*- coding: utf-8 -*-
"""Tic_Tac_Toe.ipnyb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tyBWYZjpxKyrvAtRqP-YyS2zhTOo4Yz8
"""

from pickle import FALSE
from IPython.display import clear_output
import time
#All the variables needed
board = [[1,2,3],[4,5,6],[7,8,9]] #The players will be placing their characters in this list
#and the whole game be conducted based on the current status of this list.
current_player_char = 'X' #The character of the current player
next_player_char = 'O' # The character of the next player
totalInputs = 9 #Since there are 9 slots in total in the whole board.
winner = None

def checkHorizontal():
    global winner
    for row in board:
        if row[0] == row[1] == row[2]:  # Check if all elements in a row are the same
            winner = "Player 1" if row[0] == 'X' else "Player 2"  # Determine the winner based on the symbol
            return True  # Horizontal win found
    return False  # No horizontal win
#Remove the pass statement and write your code.

def checkVertical():
    global winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:  # Check if all elements in a column are the same
            winner = "Player 1" if board[0][col] == 'X' else "Player 2"  # Determine the winner based on the symbol
            return True  # Vertical win found
    return False  # No vertical win
#Remove the pass statement and write your code.

def checkDiagonal():
    global winner
    if board[0][0] == board[1][1] == board[2][2]:  # Check diagonal from top-left to bottom-right
        winner = "Player 1" if board[0][0] == 'X' else "Player 2"  # Determine the winner based on the symbol
        return True  # Diagonal win found
    if board[0][2] == board[1][1] == board[2][0]:  # Check diagonal from top-right to bottom-left
        winner = "Player 1" if board[0][2] == 'X' else "Player 2"  # Determine the winner based on the symbol
        return True  # Diagonal win found
    return False  # No diagonal win
 #Remove the pass statement and write your code.


def checkBoard():
    if checkHorizontal() or checkVertical() or checkDiagonal():
        return True  # There is a win
    elif sum(board[i].count('X') + board[i].count('O') for i in range(3)) == 9:
        return False  # The board is full (game ended in a draw)
    return False  # Game is ongoing
 #Remove the pass statement and write your code.

def placeCharacterOnBoard(position):
    global current_player_char
    row = (position - 1) // 3  # Calculate the row index
    col = (position - 1) % 3  # Calculate the column index

    if board[row][col] != 'X' and board[row][col] != 'O':  # Check if the position is not already occupied
        board[row][col] = current_player_char  # Place the character on the board
        return 1  # Valid move, return 1
    else:
        print("Invalid position. Please enter a valid position.")
        return 0  # Invalid move, return 0
 # Invalid move, return 0
 #Remove the pass statement and write your code.

#This function prints the current status of the 'board' list in particular format.
def printCurrentBoard():
  print("-------------")
  for eachRow in board:
    print("|",end="")
    for eachCol in eachRow:
      print(f" {eachCol} ",end="|")
    print() #To move to the next row
    print("-------------")

#This function will be simulating the whole game.
def runGame():
  global current_player_char
  global next_player_char
  global winner
  welcome_msg = '''Welcome to the TIC-TAC-TOE game. The first player to place character on the board will be Player 1(Character X) and the other player will be Player 2(Character O).'''
  print(welcome_msg)
  inputCount= 0 #This variable is for counting the number of inputs and controlling the loop based on it.
  while inputCount < totalInputs:
    printCurrentBoard() #This function prints the current state of the board as a player needs to see it before making the next move.
    position = int(input(f"Player {(inputCount%2)+1},enter a position that does not contain any X or O:")) #The user needs to enter a position that does contain any X or O.
    validityofInput = placeCharacterOnBoard(position) #validityofInput will be 1 if the user inputs a valid "position"; otherwise it will be 0.
    inputCount+= validityofInput # If the inputs a valid "position", the inputCount will increase by one; otherwise it will remain as it is.
    if inputCount>=5: #There is no need to check the board before 5 valid inputs as there will be no winners before 5 valid inputs.
      if checkBoard(): #If checkBoard() returned True then current player won the game.
        winner = "Player 1" if current_player_char == 'X' else "Player 2"
        clear_output() #This function clears the output panel.
        break
    if validityofInput: #Only if the player inputs a valid "position", the player characters will be swapped for the next move.
      current_player_char,next_player_char = next_player_char,current_player_char #The players will place characters alternatively. So if X is the current player's character, in the next turn O will be the current player's character.
    clear_output() #This function clears the output panel before printing the current board status for the next player.
  printCurrentBoard()
  #After the while loop if the value of  winner is still none, that means the game ended in a draw; otherwise we have a winner.
  if winner != None:
    print(f"Well done, {winner}. You have won the game.")
  else:
    print(f"The game ended in a draw")


runGame()