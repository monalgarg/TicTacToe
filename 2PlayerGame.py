import array

# creating 2D int matrix as board for game
# * - empty, O, X
board = [["*","*","*"], ["*","*","*"], ["*","*","*"]]

# keeps track of who is going
# true - "O" turn, false "X" turn
# by default, O goes first
turn = "O" 

# checks if somone has won the game
# returns * - if no one has one; O - "O" wins; X - "X" wins
def isEndGame(): 
	for i in range(3) :
		if board[i][0] == board[i][1] == board[i][2]  and board[i][0] != 0 :
			return board[i][0]
		if board[0][i] == board[1][i] == board[2][i]  and board[0][i] != 0 :
			return board[0][i]

	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0 : 
		return board[0][0]

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0 : 
		return board[0][2]
			
	for i in range(3) :
		for j in range(3) : 
			if board[i][j] == "*" : 
				return "*"
	return "t"

def printBoard():
	print board[0][0] + " | " + board[0][1] + " | " + board[0][2]
	print "----------"
	print board[1][0] + " | " + board[1][1] + " | " + board[1][2]
	print "----------"
	print board[2][0] + " | " + board[2][1] + " | " + board[2][2]

# playing game by asking user x and y coordinates
while isEndGame() == "*" : 
	print 
	printBoard()
	print

	askUserX = turn + ": x coordinate?"
	askUserY = turn + ": y coordinate?"
	xcoor = input(askUserX) 
	ycoor = input(askUserY)

	while (xcoor > 2 or xcoor < 0 or ycoor > 2 or ycoor < 0 or board[xcoor][ycoor] != "*") : 
		print ("Try again")
		xcoor = input(askUserX) 
		ycoor = input(askUserY)
	board[xcoor][ycoor] = turn

	if turn == "O" : 
		turn = "X"
	else : 
		turn = "O"

print 
printBoard()
print

if isEndGame() == "t" : 
	print "Tie!"
else : 
	print turn + " wins!"