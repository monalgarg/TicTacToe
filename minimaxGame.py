import array

# O - user 
# X - computer

# creating 2D int matrix as board for game
# * - empty, O, X
board = [["*","*","*"], ["*","*","*"], ["*","*","*"]]

# keeps track of who is going
# true - "O" turn, false "X" turn
first = raw_input("Do you want to go first? (y/n)")
if first == "y" : 
	turn = "O"
else : 
	turn = "X"

# checks if somone has won the game
# returns * - if no one has one; O - "O" wins; X - "X" wins
def isEndGame(board): 
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

def printBoard(board):
	print board[0][0] + " | " + board[0][1] + " | " + board[0][2]
	print "----------"
	print board[1][0] + " | " + board[1][1] + " | " + board[1][2]
	print "----------"
	print board[2][0] + " | " + board[2][1] + " | " + board[2][2]

def emptySpaces(board): 
	space = []
	for i in range(3): 
		for j in range(3): 
			if board[i][j] == "*" : 
				space.append([i,j])
	return space

def minimax(board, player):
	if isEndGame(board) == "X" : 
		return (1, [])
	elif isEndGame(board) == "t" : 
		return (0, [])
	elif isEndGame(board) == "O" : 
		return (-1, [])

	if player == "X" : 
		newplayer = "O"
	else : 
		newplayer = "X"

	spaces = emptySpaces(board)
	result = [0] * len(spaces)

	for i in range(len(spaces)) : 
		newBoard = board

		s = spaces[i]
		newBoard[s[0]][s[1]] = player

		(res, coord) = minimax(newBoard, newplayer)
		result[i] = res

		newBoard[s[0]][s[1]] = "*"

	minRes = result[0]
	maxRes = result[0]
	indexMax = 0
	indexMin = 0

	for r in range(len(result)) : 
		if result[r] > maxRes : 
			maxRes = result[r]
			indexMax = r
		if result[r] < minRes : 
			minRes = result[r]
			indexMin = r

	if player == "X" : 
		return (maxRes, [spaces[indexMax][0], spaces[indexMax][1]])
	elif player == "O" : 
		return (minRes, [spaces[indexMin][0], spaces[indexMin][1]])

# playing game by asking user x and y coordinates
while isEndGame(board) == "*" : 
	print 
	printBoard(board)
	print

	if turn == "O" : 
		xcoor = input("x coordinate?") 
		ycoor = input("y coordinate?")

		while (xcoor > 2 or xcoor < 0 or ycoor > 2 or ycoor < 0 or board[xcoor][ycoor] != "*") : 
			print ("Try again")
			xcoor = input(askUserX) 
			ycoor = input(askUserY)

		board[xcoor][ycoor] = "O"

		turn = "X"
	else : 
		(num, coor) = minimax(board, "X"); 
		board[coor[0]][coor[1]] = "X"
		turn = "O"

print 
printBoard(board)
print

if isEndGame(board) == "t" : 
	print "Tie!"
else : 
	print isEndGame(board) + " wins!"