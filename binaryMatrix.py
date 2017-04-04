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
    count = 1
    while (bit > 1):
        bit/=2
        count += 1
    return count

def matrixData(dataX, dataY, _charX = "x", _charY = "y"):
    trix = [0,0,0,0,0,0,0,0,0]
    base = 0b000000001
    print(bin(dataX))
    #Track x/y coordinates on plane
    for i in range(9):
        base <<= i
        print("base is: %d"%(base)) #debugging
        print("   i is: %d"%(i))
        if (base & dataX == base):
            trix[i] = 'x'
        elif (base & dataY == base):
            trix[i] = 'y'
        else:
             trix[i] = ' '
        base = 1
    return trix
    
_dataX = 0b010100000
_dataY = 0b001000001

trix = matrixData(_dataX,_dataY)
#print(trix)
