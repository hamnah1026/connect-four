# Function for getting input
def get_input():
  while True:
    try:
        column = int(input('Enter Column from 0 -6 : '))
        if column in range(7):
          return column
          break
    except:
        pass
    print ('\nIncorrect input, try again')

#



# Board formation
print("WELCOME TO CONNECT 4 !!!!")

board = [[' ' for i in range(7)] for j in range(6)]
print(*list(range(7)), sep='   ')
for i in range(6):
  print(*board[i], sep=' | ')
  print(' - ' * 9)
print(*list(range(7)), sep='   ')


game_over = False

# Players
player_one = str(input("Enter Name of Player 1 : "))
player_two = str(input("Enter Name of Player 2 : "))

turn_no = 0
while turn_no < 42 :

  # Which player's turn
  if turn_no % 2 == 0:
    symbol, current_player = 'O', player_one
  else:
    symbol, current_player = 'Z', player_two
  print(current_player,'play',symbol)

  # Choosing tile
  column =  get_input()
  turn_no += 1

  # Check for invalid inputs
  if column > 6 or column < 0 :
    print("Column does not exist ! ")
    continue
  if board[0][column] != ' ' :
    print("Column Full ! ")
    continue

  # Input Value and Display board
  print(*list(range(7)), sep=' _ ')
  for j in range(5,-1,-1):
    if board[j][column] == ' ':
      row = j
      board[j][column]=symbol
      break
  for i in range(6):
    print(*board[i], sep=' | ')
    print(' - ' * 9)
  print(*list(range(7)), sep=' _ ')


  # Winning Conditions
  # rows
  for k in range(4):
    if board[row][k:k+4] == [symbol for e in range(4)] :
      print(current_player,'wins !!!')
      game_over = True
      break

  # Columns
  for y in range(3):
    check = [board[z][column] for z in range(y, y+4)]
    if check == [symbol for l in range(4)]:
        print(current_player,'wins !!!')
        game_over = True
        break

  # Primary Diagonal (Top Left to Bottom Right)
  primary_diagonal_check=[]
  min_index = min(row,column)
  root_row, root_column = row - min_index, column - min_index
  for i in range(7):
    current_row = root_row + i
    current_column = root_column + i
    if current_row > 5 or current_column > 6:
      break
    primary_diagonal_check.append(board[current_row][current_column])
  for k in primary_diagonal_check[::-1]:
    if k ==' ':
          primary_diagonal_check.remove(' ')
  if primary_diagonal_check == [symbol for j in range(4)]:
    print(current_player," wins !!! ")
    game_over = True
    break
  print(primary_diagonal_check)

  # Secondary Diagonal (Top Right to Bottom Left)
  secondary_diagonal_check=[]
  min_index= min(row,6-column)
  root_row = row - min_index
  root_column = column + min_index
  for i in range (6):
    current_row = root_row + i
    current_column = root_column - i
    if current_row > 5 or current_column < 0 :
        break
    secondary_diagonal_check.append(board[current_row][current_column])
  for k in secondary_diagonal_check:
    if k ==' ':
      secondary_diagonal_check.remove(' ')
  if secondary_diagonal_check == [symbol for j in range(4)]:
    print(current_player,' wins !!! ')
    game_over = True
    break

  # End Game
  if game_over :
    break