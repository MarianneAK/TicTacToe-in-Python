


def displayBoard(markers):
    print '|'+markers[0]+'|'+markers[1]+'|'+markers[2]+'|\n|'+markers[3]+'|'+markers[4]+'|'+markers[5]+'|\n|'+markers[6]+'|'+markers[7]+'|'+markers[8]+'|'
    board = [x for x in range (1,10)]
    return board


def playerInput():

    players= ['x','o']
    print 'Player 1: \'X\' or \'O\' ?'
    choice = raw_input()
   
    while choice.lower() != 'x' and choice.lower() != 'o':
        print 'Please choose either \'X\' or \'O\''
        choice = raw_input()

    if(choice.lower() == 'o'):
        players[0] = 'o'
        players[1] = 'x'
    
    print '\nPlayer 1: %s\nPlayer 2: %s'%(players[0],players[1])

    return players

def placeMarker(board, marker, position, place_marker):
    place_marker[board.index(position)] =  marker
    return place_marker

def winCheck(board,mark):
    firsts = [0,3,6]

    #checking diagonally
    if board[4] == mark:
        if board[2] == mark and board[6] == mark:
            return True
        elif board[8] == mark and board[0] == mark:
            return True 

    #checking horizontally
    for i in firsts:
        if board[i] == mark:
            if board[i+1] == mark and board[i+2] == mark:
                return True

    #checking vertically
    for i in range(0,3):
        if board[i] == mark:
            if board[i+3] == mark and board[i+6] == mark:
                return True
    
    return False


def chooseFirst():
    from random import randint
    random_num = randint(0, 1)

    if random_num == 0:
        print 'Player 1 goes first'
        return 0
    else:
        print 'Player 2 goes first'
        return 1


def spaceCheck(board, position):
    return board[int(position)-1]==''

def fullBoardCheck(board):
    for k,v in board.iteritems():
        if v == '':
            return False
    return True

def playerChoice(board):

    available = False
    print '\n----------------------------------- Choose your next position: -----------------------------------\n'

    while available == False:
        while True:
            try:
                choice = int(raw_input())
                break
            except ValueError:
                print '\n----------------------------------- Please enter ONLY a number -----------------------------------\n'
        

        while choice>9 or choice<1:
            print '\n----------------------------------- Please enter a position only between 1 and 9 -----------------------------------\n'
            choice = int(raw_input())
        
        
        available = spaceCheck(places, choice)
        if available:
            print 'Position saved.'
            return choice
        else:
            print 'Position not available. Please choose another one.'


def replay():
    print '\n----------------------------------- Play again? Y/N -----------------------------------\n'
    choice = raw_input()

    while choice.lower() != 'y' and choice.lower() != 'n':
        print 'Please answer with only Y or N'
        choice = raw_input()
    
    if choice.lower() == 'y':
        return True
    
    return False



continueGame = True
# while players still want to play
while continueGame:
    places = {}

    # fill dict 'places' with the position's INDEXES (position -1) as keys
    for i in range(0,9):
        places[i] = ''
    
    # display the board and fill list 'board' with empty slots
    markers = [' ']*9
    board = displayBoard(markers)

    # let the players choose X or O, returns array (0 is Player 1, 1 is Player 2)
    players = playerInput()

    # who plays first
    currentPlayer = chooseFirst()
    
    winningPlayer = 0
    # while there still are empty places on the board
    while fullBoardCheck(places) == False:
        
        print '\n----------------------------------- Player %s\'s turn. -----------------------------------\n'%(str(currentPlayer +1))
        # player chooses position
        choice = int(playerChoice(places))

        # put the correct marker on the correct position on the board
        markers[choice-1] = players[currentPlayer]
        board = displayBoard(markers)
      
        # player's marker (x or o) is saved as value of the position
        places = placeMarker(board, players[currentPlayer], choice, places)

        # check if current player won
        if winCheck(places, players[currentPlayer]):
            winningPlayer = currentPlayer + 1
            break
        else:
            if currentPlayer == 0:
                currentPlayer = 1
            else:
                currentPlayer = 0

    if winningPlayer == 0:
        text = 'IT\'S A TIE!'
        print text.center(50,'-')
    else:
        text = ' CONGRATS! Player %s won! '%(winningPlayer)
        print text.center(50,'-')
    

    
        
    continueGame = replay()

