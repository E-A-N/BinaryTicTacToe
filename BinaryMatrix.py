import random

#Add bit values representing present game state to this value
ticTacToe   = 0b0


#Bit equivalent to plane coordinates (tictactoe matrix table)
topLeft     = 0b100000000
topMid      = 0b10000000
topRight    = 0b1000000
midLeft     = 0b100000
midMid      = 0b10000
midRight    = 0b1000
bottomLeft  = 0b100
bottomMid   = 0b10
bottomRight = 0b1

#Winning Conditions
topHorWin     = 0b111000000
midHorWin     = 0b000111000
bottomHorWin  = 0b000000111
leftVertWin   = 0b100100100
midVertWin    = 0b010010010
rightVertWin  = 0b001001001
leftDiag      = 0b100010001
rightDiag     = 0b001010100

def bitCount(bit):
    '''
    This function counts the number of bits in a given number
    :type bit: int
    :param bit: A binary number
    '''
    count = 1
    while (bit > 1):
        bit/=2
        count += 1
    return count

def matrixData(dataX, dataO, _charX = "x", _charO = "o"):
    '''
    This function creates a new tic tac toe table
    :type dataX: int (binary)
    :param dataX: A binary number representing the choices made by player x
    :type dataO: int (binary)
    :param dataO: A binary number representing the choices made by player o
    :type _charX: string
    :param _charX: A character repesenting player x
    :type _charO: string
    :param _charO: A character repesenting player o
    '''
    trix = [0,0,0,0,0,0,0,0,0]
    base = 0b000000001

    #Track x/o coordinates on plane
    for i in range(9):
        base <<= i
        if (base & dataX == base):
            trix[i] = _charX
        elif (base & dataO == base):
            trix[i] = _charO
        else:
            trix[i] = ' '
        base = 1
    return trix

#void function
def displayMatrix(trix):
    '''
    This function takes prints a tic tac toe grid
    :type trix: list
    :param trix: a list that stores the current game decisions
    '''
    count = 1
    for i in trix:
        print("|%s|"%(i), end='')
        if (count % 3 == 0):
            print()
        count += 1

#returns int, binary number
def dataToBinary(data,chars):
    '''
    This function converts a data table representing game data to bits.
    Note: The value of a bit ascends from right to left.  The index of an array
    holding the the bit values ascend from left to right.
    :type data: int
    :param data: a number value that represents the game data
    :type chars: string
    :param chars: characters to check for within the game board
    '''
    result = 0
    count = 0
    data
    for x in chars:
        for z in data:
            if x == z:
                #shift bits by index value of count and add to result
                result += 1 << count
                #print(1 << count)
                #print(result)
            count += 1
        count = 0
    return result

def checkGameEnd(data, toBits, gameChars = "xo"):
    '''
    This function checks for a tictactoe within the current coordinates
    :type data: list
    :param data: an array of characters representing current game decisions
    :type toBits: function
    :param toBits: a callBack used to parse the game state and and return bits
    :type gameChars: string
    :param gameChars: characters used in the game table
    '''
    bitData = toBits(data,gameChars) #parse the game board
    result = False
    possibilities = [0b111000000, 0b000111000, 0b000000111, 0b100100100, 0b010010010, 0b001001001, 0b100010001, 0b001010100, 0b111111111]
    for i in possibilities:
        if (bitData & i == i):
            result = True
            break
    return result

#pass game characters and attributes using the "setGameOptions" function
gameSettings = {}
#create 50 50 chance of either player going firstTurn
diceRoll = random.randint(0,1)
def setGameOptions(ply1,ply2,diceRoll):
    '''
    This function uses input to create basic game settings.
    :type ply1: string
    :param ply1: A character that represents 1st players marks on game board
    :type ply2: string
    :param ply2: A charater that represents 2nd players marks on game board
    '''
    firstPlayerGoesFirst = (diceRoll == 0)
    turn = "player1"
    #create 50/50 change of player 2 going first
    if (not firstPlayerGoesFirst):
        turn = "player2"

    opts = {}
    opts["gameBoard"] = 0b0
    opts["player1"] = ply1
    opts["player2"] = ply2
    #choice formats should be in binary
    opts["p1Choice"] = "0b0"
    opts["p2Choice"]=  "0b0"

                                                                                                opts["player1Win"] = False
                                                                                                opts["player2Win"] = False
    opts["firstTurn"] = turn
    #"currentlyFirstturn" key should be boolean to allow seemless alternating between turns
    opts["currentlyFirstTurn"] = firstPlayerGoesFirst


    return opts

'''
    COLLECT INPUT FROM PLAYERS!!
'''
def characterRequest(debug = -77):
    '''
    This function returns the value of a users input that represents their gameboard
    character.
    :type debug: string
    :param debug: A default value that checks if this function will take user input
    '''
    decision = 0

    #if anything but -1 is passed to function then game is being simulated
    if (debug == -77):
        decision = int(input("Enter the character you would like to use: "))
    else:
        #simulation value that will eventually be added to tictactoe grid
        decision = debug

    return decision

def decideOnMove(debug = -66):
    '''
    This function returns the value of a users input
    that represents which spot on the grid they wish to choose.
    :type debug: string
    :param debug: A default value that checks if this function will take user input
    '''
    decision = 0
    isDebugging = debug
    notDebugging = -66
    badInput = -55

    #if anything but -66 is passed to function then game is being simulated
    if (debug == notDebugging):
        decision = input("Enter Binary value for where you wish to move: ")
    else:
        #simulation value that will eventually be added to tictactoe grid
        decision = isDebugging

    #Convert string to readable binary and parse
    if(type(decision) == str):
        #Sanitize Input
        for i in decision:
            if ((i != "0") and (i != "1")):
                decision = badInput
                break
        if(decision != badInput):
            decision = "0b" + decision
            decision = eval(decision)
    else:
        decision = badInput

    return decision

    #ADD GAME UPDATE FUNCTION
def update(state,*funcs):
    '''
    This function advances the state of the game using
    the current game state and a collection of methods.
    :type state: dict
    :param state: A dictionary containing game information
    '''
    newState = state
    p1 = decideOnMove()
    p2 = decideOnMove()
    return newState
