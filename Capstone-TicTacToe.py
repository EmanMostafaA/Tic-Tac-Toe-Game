
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

game_is_running = True

winner = None

current_player = "X"



def play_game():

  # initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_is_running:

    handle_turn(current_player)

    check_if_game_over()

    change_player()

  if winner == "X" or winner == "O":
    print( "the winner is "+winner )
  elif winner == None:
    print("Tie.")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("\n")



def handle_turn(player):

  
  print("your turn " + player)
  position = input("Choose your position on the board from 1-9: ")
 
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose your position on the board from 1-9: ")

    
    position = int(position) - 1

    
    if board[position] == "-":
      valid = True
    else:
      print("Choose a number from 1-9 . Go again.")

 
  board[position] = player

  
  display_board()



def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
 
  global winner
  
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
 
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a winner
def check_rows():
 
  global game_is_running
  
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  
  if row_1 or row_2 or row_3:
    game_is_running = False
 
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
 
  else:
    return None


# Check the columns for a winner
def check_columns():
  
  global game_is_running
 
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  
  if column_1 or column_2 or column_3:
    game_is_running = False
  
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  
  else:
    return None


# Check the diagonals for a winner
def check_diagonals():
  
  global game_is_running
 
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  if diagonal_1 or diagonal_2:
    game_is_running = False
  
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  
  else:
    return None


# Check if there is a tie
def check_for_tie():
  
  global game_is_running
  
  if "-" not in board:
    game_is_running = False
    return True
  
  else:
    return False


# change the current player from X to O, or O to X
def change_player():
  
  global current_player
  
  if current_player == "X":
    current_player = "O"
  
  elif current_player == "O":
    current_player = "X"


play_game()
