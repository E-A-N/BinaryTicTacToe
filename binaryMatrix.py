ticTacToe   = 0

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

    #Track x/y coordinates on plane
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




_dataX = 0b010100000
_dataY = 0b001000001

trix = matrixData(_dataX,_dataY)
displayMatrix(trix)
