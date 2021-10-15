#J. Bricker
#Text-based BattleShip clone that I made for additional practice during CS151


#Import Statements
import random
import time
import os

#This function clears the screen when it is called
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

#This function makes the game boards
def makeBoard(board):
	n = 1 #Used for the sides of the game board
	#Loop through to 121 filling the gameboard list with relavant information
	for  i in range (0, 122):
		#Fills in the top row
		if i == 0:
			board.append('# ')
		elif i == 1:
			board.append('A')
		elif i == 2:
			board.append('B')
		elif i == 3:
			board.append('C')
		elif i == 4:
			board.append('D')
		elif i == 5:
			board.append('E')
		elif i == 6:
			board.append('F')
		elif i == 7:
			board.append('G')
		elif i == 8:
			board.append('H')
		elif i == 9:
			board.append('I')
		elif i == 10:
			board.append('J')
		elif i in side: #Fills in the sides
			if n != 10:
				board.append(str(n) + ' ')
				n += 1
			else:
				board.append(str(n))
		else:
			board.append(' ') #This is the empty spaces on the game board

#This function is used to print the boards to the screen
def printBoard(board):
	for i in range (0, 111, 11): #each row has 11 spaces (side + 10 possible moves)
		n = i + 11
		print(board[i:n]) #Prints each row followed by a new line


#Used for placing horizontal parts for the computer
def horizontalPart(x, first): #x is the length of the part, first determines if it is the first 3 piece part or not
	y = 0 #This will be used for the starting postion of the part
	cx = x #Check Variable
	while y in illegalMove:
		y = random.randint(12, 121) #Generate the list postition for a possible move
		for i in range (0, cx + 1): #This loop checks that the part will not land out of bounds or cross over another part
			cy = y + i #cy is another check variable
			if cy in illegalMove or computerBoard[cy] == 'R': #If placement is not allowed process starts over
				y = 0
				break
	for i in range (0, x): #This loop places the part on the board
		del computerBoard[y] #remove whatever is at index y on the board
		computerBoard.insert(y, 'R') #Insert R at Index y
		#These if statements record the coordinates for each part which allows the player to know which part has been destroyed
		if x == 5:
			part5cord.insert(i, y)
		elif x == 4:
			part4cord.insert(i, y)
		elif x == 3:
			if first == 0:
				part3cord.insert(i, y)
				if len(part3cord) == 3:
					first = 1
			elif first == 1:
				part32cord.insert(i, y)
		elif x == 2:
			part2cord.insert(i, y)
		y = y + 1
	return first


#Used for setting vertical parts for the computer
def verticalPart(x, first):
	y = 0
	cx = 0
	for i in range (0, x): #Vertical spaces are 11 away in the list this sets check variable to 11 times the part length
		cx = cx + 11
	while y in illegalMove: #Checks for illegal placement
		y = random.randint(12, 121)
		for i in range (0, cx + 1, 11):
			cy = y + i
			if cy in illegalMove or computerBoard[cy] == 'R':
				y = 0
				break
	for i in range (0, x): #Places part on board
		del computerBoard[y]
		computerBoard.insert(y, 'R')
		#These if statements record the coordinates for each part which allow the player to know which part has been destroyed
		if x == 5:
			part5cord.insert(i, y)
		elif x == 4:
			part4cord.insert(i, y)
		elif x == 3:
			if first == 0:
				part3cord.insert(i, y)
				if len(part3cord) == 3:
					first = 1
			elif first == 1:
				part32cord.insert(i, y)
		elif x == 2:
			part2cord.insert(i, y)
		y = y + 11
	return first


#Used for placing player parts on the board
def playerPart(x):
	HorV = 0 #Horizontal or Vertical
	y = 0 #Starting postition variable
	while HorV != 'H' and HorV != 'V':
		HorV = input("Do you want to place the piece horizontally(H) or vertically(V): ").upper() #Get input to determine which orientation to place the part
	while y in illegalMove: #This loop gets input from the user and validates it
		playerPartInput = input("Type in coordinates for the start of the first piece separated by a comma starting with the letter: ").upper()
		if ',' not in playerPartInput: #Validates that a comma was entered if not restart the loop to prevent input errors
			continue
		playerPartInput = playerPartInput.split(',') #Split at the comma to break the input into a list of coordinates
		if not playerPartInput[1].isdigit(): #Discovered a bug at the last minute, This checks that the second cord entered was a number and not a letter
			continue 
		playerPartInput, error = conversion(playerPartInput) #Calls the conversion funtion which converts the letter to a number and checks for an error status if input outside of range
		if error == True: #Error will return True if conversion failed this will restart loop #Restart if letter was out of range
			continue
		y = (int(playerPartInput[1]) * 11) + int(playerPartInput[0]) #This line took over two hours because I am bad at math
		if HorV == 'H': #Checks validity of placement if the part is horizontal
			cx = x #cx is a check variable needed so I don't overwrite x
			for i in range (0, cx):
				cy = y + i
				if cy in illegalMove or playerBoard[cy] == 'R':
					y = 0
					break
		elif HorV == 'V': #Checks validity if part is vertical
			cx = 0 #cx is a check variable needed to verify placement
			for i in range (0, x): #This loop sets cx to the maximum value needed to check placement in the next loop. Each section of part is 11 away from previous
				cx += 11
			for i in range (0, cx, 11): #Check placement of vertical part
				cy = y + i
				if cy in illegalMove or playerBoard[cy] == 'R':
					y = 0
					break
	for i in range (0, x): #places part on board after all checks are passed
		del playerBoard[y]
		playerBoard.insert(y, 'R')
		if HorV =='V': #Vertical orientation spaces are 11 apart			
			y = y + 11
		elif HorV == 'H': #Horizontal orientation spaces are 1 apart
			 y = y + 1

#Letter to number conversion function
def conversion(playerPartInput):
	if playerPartInput[0] == 'A':
		convert = 1
	elif playerPartInput[0] == 'B':
		convert = 2
	elif playerPartInput[0] == 'C':
		convert = 3
	elif playerPartInput[0] == 'D':
		convert = 4
	elif playerPartInput[0] == 'E':
		convert = 5
	elif playerPartInput[0] == 'F':
		convert = 6
	elif playerPartInput[0] == 'G':
		convert = 7
	elif playerPartInput[0] == 'H':
		convert = 8
	elif playerPartInput[0] == 'I':
		convert = 9
	elif playerPartInput[0] == 'J':
		convert = 10
	else: #In case input out of range
		error = True
		return playerPartInput, error
	del playerPartInput[0]
	playerPartInput.insert(0, convert)
	error = False
	return playerPartInput, error


#Player turn function
def playerTurn(playerHits):
	playerMove = 0 #Set playerMove to an illegal move by default
	#Print the required boards
	print("Attack Board")
	printBoard(displayBoard)
	print("Player Board")
	printBoard(playerBoard)
	while playerMove in illegalMove or playerMove in playerMoves: #Loop while inputted move is illegal or already been used
		playerMoveInput = input("Type in a coordinate to attack separated with a comma starting with the letter: ").upper()
		if ',' not in playerMoveInput: #Validates that a comma was entered if not restart the loop to prevent error
			continue
		playerMoveInput = playerMoveInput.split(',') #Split input to create a list
		if not playerMoveInput[1].isdigit(): #Discovered a bug at the last minute, This checks that the second cord entered was a number and not a letter
			continue 
		playerMoveInput, error = conversion(playerMoveInput) #Call conversion function for letter input
		if error == True: #If input out of range start loop over
			continue
		playerMove = (int(playerMoveInput[1]) * 11) + int(playerMoveInput[0]) #Determine which list index inputted
	print("Attacking")
	time.sleep(1)
	playerMoves.append(playerMove)
	#If a hit occurs
	if computerBoard[playerMove] == 'R':
		print("Direct Hit!")
		del displayBoard[playerMove]
		displayBoard.insert(playerMove, 'X')
		playerHits += 1 #This variable has the power to end the game
		#Check if any of the parts have been destroyed
		if playerMove in part5cord:
			part5cord.append(0)
			if len(part5cord) == 10:
				print("You destroyed the computer's Robot Command Station (5 length robot ship)")
		elif playerMove in part4cord:
			part4cord.append(0)
			if len(part4cord) == 8:
				print("You destroyed the computer's Robot Command Ship (4 length robot ship")
		elif playerMove in part3cord:
			part3cord.append(0)
			if len(part3cord) == 6:
				print("You destroyed one of the computer's Robot Attack Ships (3 length robot ship)")
		elif playerMove in part32cord:
			part32cord.append(0)
			if len(part32cord) == 6:
				print("You destroyed one of the computer's Robot Attack Ships (3 length robot ship)")
		elif playerMove in part2cord:
			part2cord.append(0)
			if len(part2cord) == 4:
				print("You destroyed the computer's Robot Shield Ship (2 length robot ship)")
	#If a miss occurs
	else:
		print("Miss")
		del displayBoard[playerMove]
		displayBoard.insert(playerMove, 'M')
	return playerHits


#Computer's Turn Function
def computerTurn(computerHits, computerOnTarget):
	computerMove = 0 #Set the computer move to illegal by default
	#These if statements until the else provide the computer with some limited intelligence
	#If the computer has successfully hit a target within the last 4 moves it will "search" the area around unless it already has then it defaults to random until next turn
	#Pattern is to the right, left, up, down
	if computerOnTarget == 1:
		computerMove = computerMoves[-1] + 1 #last move plus 1 space over
		while computerMove in illegalMove or computerMove in computerMoves:
			computerMove = random.randint(12, 120)
	elif computerOnTarget == 2:
		computerMove = computerMoves[-2] - 1 #second to last move plus 1 space over
		while computerMove in illegalMove or computerMove in computerMoves:
			computerMove = random.randint(12, 120)
	elif computerOnTarget == 3:
		computerMove = computerMoves[-3] - 11 #third to last move plus 1 space up
		while computerMove in illegalMove or computerMove in computerMoves:
			computerMove = random.randint(12, 120)
	elif computerOnTarget == 4:
		computerMove = computerMoves[-4] + 11 #fourth to last move plus 1 space down
		while computerMove in illegalMove or computerMove in computerMoves:
			computerMove = random.randint(12, 120)
	else: #Was possible to get an error where computerOnTarget would equal more than 4 causing computerMove to remain 0 resulting in illegal move, the else statement fixes bug
		while computerMove in illegalMove or computerMove in computerMoves:
			computerMove = random.randint(12, 120)
	x = computerMove // 11 #Use floor divsion to get the row
	y = computerMove % 11 #Use the modulus to get the column
	#These if statements convert the column number to the letter that prints out
	if y == 1:
		y = 'A'
	elif y == 2:
		y = 'B'
	elif y == 3:
		y = 'C'
	elif y == 4:
		y = 'D'
	elif y == 5:
		y ='E'
	elif y == 6:
		y = 'F'
	elif y == 7:
		y = 'G'
	elif y == 8:
		y = 'H'
	elif y == 9:
		y = 'I'
	elif y == 10:
		y = 'J'
	print("You are under attack at coordinates %s,%s" %(y, x)) #Print the coordinates of the place the computer attacks
	time.sleep(1)
	computerMoves.append(computerMove) #Add the computer's move to its list of moves
	#If a hit occurs, update board, hit total, and recent hit variable
	if playerBoard[computerMove] == 'R':
		print("You've Been Hit")
		del playerBoard[computerMove]
		playerBoard.insert(computerMove, 'X')
		computerHits += 1
		if computerOnTarget != 1:
			computerOnTarget = 1
	#If a miss occurs, update board and recent hit variable
	else:
		print("The computer was off target")
		del playerBoard[computerMove]
		playerBoard.insert(computerMove, 'M')
		if computerOnTarget >= 1:
			computerOnTarget += 1
		elif computerOnTarget == 4:
			computerOnTarget = 0
	return computerHits, computerOnTarget


#Variable and List declarations
playerHits = 0 #Used to determine winner
computerHits = 0 #Used to determine winner
playerBoard = [] #Player's board
computerBoard = [] #Computer's board
displayBoard = [] #Player's guess board
illegalMove = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133] #List of moves that are illegal from the start
side = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110] #List of the side area
parts = [5, 4, 3, 3, 2] #Number and size of parts
computerMoves = [] #Empty list for the computer's moves
playerMoves = [] #Empty list for the player's moves
part5cord = [] #5 length part coordinates
part4cord =[] #4 length part coordinates
part3cord = [] #first 3 length part coordinates
part32cord = [] #second 3 length part coordinates
part2cord = [] #2 length part coordinates			
first = 0 #Used to determine which part the computer is placing with the 3 length parts
computerOnTarget = 0 #Computer's 'Intelligence'

#Three boards needed, playerBoard is the board the player uses, display board is the board that the player see for when they attack, computerBoard is the board the computer uses
makeBoard(playerBoard)
makeBoard(computerBoard)
makeBoard(displayBoard)


clear() #Clear the screen of previous commands to start the game
print("Space Robot Battle, definitely not a BattleShip knock off")
print("Placing the computer's parts")
time.sleep(1)
#This loop places the computer's parts
for i in range (len(parts)):
	placement = random.randint(0, 1)
	if placement == 0:
		first = horizontalPart(parts[i], first)
	else:
		first = verticalPart(parts[i], first)
#Begin Player part placement process
print("Begin placing your parts")
printBoard(playerBoard)
for i in range (len(parts)):
	print("Placing a part that is " + str(parts[i]) + " long.")
	playerPart(parts[i])
	clear()
	printBoard(playerBoard)

clear() #clear the screen
print("All pieces have been placed")
time.sleep(1)
print("Picking the first player")
time.sleep(1)
#Pick a player to go first
whoIsFirst = random.randint(0,1)
if whoIsFirst == 0: #If the player goes first
	print("You go first")
	while playerHits <= 17 and computerHits <= 17: #17 hits means all parts destroyed and game ends
		playerHits = playerTurn(playerHits)
		if playerHits == 17: #Check if game is over after player turn
			winner = 0
			break
		time.sleep(3)
		clear()
		computerHits, computerOnTarget = computerTurn(computerHits, computerOnTarget)
		if computerHits == 17: #Check if game is over after computer's turn
			winner = 1
			break
		
	
else: #The computer goes first
	print("The Computer goes first")
	while playerHits <= 17 and computerHits<= 17:
		computerHits, computerOnTarget = computerTurn(computerHits, computerOnTarget)
		if computerHits == 17: #Check if computer won
			winner = 1
			break
		playerHits = playerTurn(playerHits)
		if playerHits == 17: #Check if player won
			winner = 0
			break
		time.sleep(3)	
		clear()

		

if winner == 0: #If player won
	clear()
	print("Attack Board")
	printBoard(displayBoard)
	print("Player Board")
	printBoard(playerBoard)
	print("You Win!!!")
else: #If computer won
	clear()
	print("You Lose.")
	printBoard(computerBoard) #Display computer board to see where parts were

#The End
input("Press Enter to Quit")			