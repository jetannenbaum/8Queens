# 8 Queens problem
# By: J.E. Tannenbaum
# Initial Release: 12/30/2021
# 01/01/2022: Add logging to the program
# See: https://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up the initial empty board
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
         
# Print the board, replacing 0s with dashes
def printBoard(board):
  print('Solution:')
  print('   0 1 2 3 4 5 6 7')
  for row in range(8):
    dataOut = str(row) + ':'
    for col in range(8):
      if board[row][col] != 0:
        dataOut = dataOut + ' ' + str(board[row][col])
      else:
        dataOut = dataOut + ' -'
    print(dataOut)

# Check to see if this is a safe place for a queen
def checkBoard(board, row, col):
  for i in range(row):  #check for queens on column
      if board[i][col]== 'Q':
          return False
          
  for i in range(row): #loop through rows
      for j in range(8): #and columns
          if board[i][j]== 'Q': #if there is a queen
              if abs(i - row) == abs(j - col): #and if there is another on a diagonal
                  return False
  return True #if every check clears, we can return true
  
# Put a queen on the board
def placeQueen(board, row, col):
  logging.debug('placeQueen at row: ' + str(row) + ' col: ' + str(col))
  board[row][col] = 'Q'

# Remove a queen from the board
def removeQueen(board, row):
  logging.debug('removeQueen from row: ' + str(row))
  for col in range(8):
    board[row][col] = 0
  
# Find the last column the queen was on
def findCol(board, row):
  col = 0
  while board[row][col] != 'Q':
    col = col + 1
  return col

# Try to solve the board by placing a queen at a row & col  
def solveBoard(board, row, col):
  global bDone

  # Are we done yet?
  bDone = bDone or row >= 8

  # Nope, so walk through each row, starting at the top
  while row < 8 and not bDone:

    # Can we place the queen?
    if checkBoard(board, row, col):

      # yup, do so
      placeQueen(board, row, col)
      row = row + 1

      # Check to see if we are past the bottom of the board
      if row < 8:
        solveBoard(board, row, 0)
      else:
        bDone = True
    else:

      # We couldn't place the queen at the current column, so move over and try again
      col = col + 1
      while col < 8 and row < 8 and not bDone:
        if checkBoard(board, row, col):
          placeQueen(board, row, col)
          row = row + 1
          if row < 8 and not bDone:
            solveBoard(board, row, 0)
          else:
            bDone = True
        else:
          col = col + 1
          if col < 8 and row < 8 and not bDone:
            solveBoard(board, row, col)
    
    # We got to the end of the row and still can't place the queen,
    # so back up a row, find where that queen is, move over one column,
    # then remove the queen fom that row and try again
    while col >= 8 and row < 8 and not bDone:
      row = row - 1
      col = findCol(board, row) + 1
      removeQueen(board, row)
    if row < 8 and not bDone:
      solveBoard(board, row, col)
    else:
      bDone = True

# Try to solve the board by placing a queen at the top left (row, col)
# board is passed by reference, so it will come back with the solution
bDone = False
logging.info('Starting to solve the puzzle')
solveBoard(board, 0, 0)
logging.info('Solved the puzzle, printing the solution')
printBoard(board)