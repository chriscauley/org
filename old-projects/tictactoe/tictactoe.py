import sys

board = []
players = ['X','O']
current_turn = 0
turns = []
winner = "D"

get_input = raw_input

tests =[
  ("O",['0,0', '0,1', '0,2', '1,0', '2,2', '1,1', '1,2']),
]

if len(sys.argv) > 1: # we're in a test
  test_winner, test_turns = tests[int(sys.argv[1])]
  def get_input(*args):
    return test_turns[current_turn-1]

for i in range(3):
  board.append([' ',' ',' '])

def check_winner():
  """ return who won if there's a winner. If not return None """
  diagonals = [
    [board[i][j] for i in range(3) for j in range(3)],
    [board[i][j] for i in range(3) for j in range(3)[::-1]],
  ]
  for _board in [board, zip(*board), diagonals]:
    for row in _board:
      if len(set(row)) == 1 and row[0] != " ":
        return row[0]

while True:
  current_turn += 1
  current_player = players[current_turn%len(players)]

  for row in board:
    print " | ".join(row)
    print "-"*12

  turn = get_input("%s's turn. Enter a row,column: "%current_player).split(",")
  turns.append(turn)
  if len(turn) !=2:
    print "Invalid move please enter the row and column like r,c." 
    continue
  #! TODO check that RC are both numbers 0-2
  #! TODO make sure that the spot isn't taken

  x,y = [int(t) for t in turn]
  board[x][y] = current_player
  winner = check_winner()
  if winner:
    print "%s won in %s turns!"%(current_player,current_turn)
    break

  if current_turn == 9:
    print "Game is a draw"
    break

if len(sys.argv) > 1:
  assert(winner == test_winner)
else:
  print turns