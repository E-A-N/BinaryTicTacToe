import unittest
import BinaryMatrix as binTrix

class binaryMatrixUnitTest(unittest.TestCase):
    ###bitCount function tests###
    def test_bit_count_of_1_bit(self):
        bits = 1 #1
        binAmount = 0b1
        count = binTrix.bitCount(binAmount)
        statement = "This is the incorrect amount of bits."
        self.assertEqual(bits,count,statement)

    def test_bit_count_of_8_bits(self):
        bits = 8 #128
        binAmount = 0b10000000
        count = binTrix.bitCount(binAmount)
        statement = "This is the incorrect amount of bits."
        self.assertEqual(bits,count,statement)

    ###matrixData function tests###
    def test_matrix_data_one(self):
        dataX = 0b010100000
        dataO = 0b001000001
        testData = binTrix.matrixData(dataX,dataO,'x','o')
        correctList = ['o', ' ', ' ', ' ', ' ', 'x', 'o', 'x', ' ']
        statement = "This table is incorrect."
        self.assertEqual(correctList,testData,statement)

    def test_matrix_data_two(self):
        dataX = 0b111110000
        dataO = 0b000001111
        testData = binTrix.matrixData(dataX,dataO,'x','o')
        correctList = ['x', 'x', 'x', 'x', 'x', 'o', 'o', 'o', 'o']
        correctList.reverse() #Align list with with bits correctly
        statement = "This table is incorrect."
        self.assertEqual(correctList,testData,statement)

    def test_matrix_data_all_Xs(self):
        dataX = 0b111111111
        dataO = 0b000000000
        testData = binTrix.matrixData(dataX,dataO,'x','o')
        correctList = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
        correctList.reverse() #Align list with with bits correctly
        statement = "This table is incorrect."
        self.assertEqual(correctList,testData,statement)

    def test_matrix_data_all_Os(self):
        dataX = 0b000000000
        dataO = 0b111111111
        testData = binTrix.matrixData(dataX,dataO,'x','o')
        correctList = ['o', 'o', 'o', 'o', 'o','o','o','o','o']
        statement = "This table is incorrect."
        self.assertEqual(correctList,testData,statement)

    def test_matrix_data_size(self):
        dataX = 0b010100000
        dataO = 0b001000001
        testData = binTrix.matrixData(dataX,dataO,'x','o')
        testSize = len(testData)
        correctSize = 9
        statement = "This table is incorrect."
        self.assertEqual(correctSize,testSize,statement)

    ###table conversion to binary test###
    def test_table_data_to_binary(self):
        testData = ['o', ' ', ' ', ' ', ' ', 'x', 'o', 'x', ' ']
        testBits = binTrix.dataToBinary(testData,'o') #0b001000001
        correctBits = 0b001000001
        statement = "Bit amount is not correct."
        self.assertEqual(correctBits,testBits,statement)

    def test_table_data_to_binary_all_x(self):
        testData = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
        testBits = binTrix.dataToBinary(testData,'x') #0b001000001
        correctBits = 0b111111111
        statement = "Bit amount is not correct."
        self.assertEqual(correctBits,testBits,statement)

    ###test game winning conditions
    def test_win_top_hor_x(self):
        winConditionX = 0b111000000
        player = "x"
        testGame = [' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_top_hor_o(self):
        winConditionX = 0b111000000
        player = "o"
        testGame = ['', '', ' ', ' ', ' ', ' ', 'o', 'o', 'o']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_mid_hor_x(self):
        winConditionX = 0b000111000
        player = "x"
        testGame = [' ', ' ', ' ', 'x', 'x', 'x', '', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_mid_hor_o(self):
        winConditionX = 0b000111000
        player = "o"
        testGame = ['', '', '', 'o', 'o', 'o', '', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_bottom_hor_x(self):
        winConditionX = 0b000111000
        player = "x"
        testGame = ['x', 'x', 'x', '', '', '', '', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_bottom_hor_o(self):
        winConditionX = 0b000111000
        player = "o"
        testGame = ['o', 'o', 'o', '', '', '', '', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_left_vert_x(self):
        winConditionX = 0b100100100
        player = "x"
        testGame = ['x', '', '', 'x', '', '', 'x', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_left_vert_o(self):
        winConditionX = 0b100100100
        player = "o"
        testGame = ['o', '', '', 'o', '', '', 'o', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_mid_vert_x(self):
        winConditionX = 0b010010010
        player = "x"
        testGame = ['', 'x', '', '', 'x', '', '', 'x', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_mid_vert_o(self):
        winConditionX = 0b010010010
        player = "o"
        testGame = ['', 'o', '', '', 'o', '', '', 'o', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_right_vert_x(self):
        winConditionX = 0b001001001
        player = "x"
        testGame = ['', '', 'x', '', '', 'x', '', '', 'x']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_right_vert_o(self):
        winConditionX = 0b001001001
        player = "o"
        testGame = ['', '', 'o', '', '', 'o', '', '', 'o']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_diagonal_to_right_x(self):
        winConditionX = 0b001010100
        player = "x"
        testGame = ['', '', 'x', '', 'x', '', 'x', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_diagonal_to_right_o(self):
        winConditionX = 0b001010100
        player = "o"
        testGame = ['', '', 'o', '', 'o', '', 'o', '', '']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_diagonal_to_left_x(self):
        winConditionX = 0b100010001
        player = "x"
        testGame = ['x', '', '', '', 'x', '', '', '', 'x']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_win_diagonal_to_left_o(self):
        winConditionX = 0b100010001
        player = "o"
        testGame = ['o', '', '', '', 'o', '', '', '', 'o']
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player) #should return a boolean
        statement = "The game should be over"
        self.assertTrue(result,statement)

    def test_cats_game(self):
        winConditionX = 0b111111111
        player = "xo"
        testGame = ["o","x","o","o","x","o","x","o","x"]
        callBack = binTrix.dataToBinary
        result = binTrix.checkGameEnd(testGame,callBack,player)
        statement = "This is a cats game, game should end in a draw!"
        self.assertTrue(result,statement)

    def test_diceRoll(self):
        result = (binTrix.diceRoll == 0) | (binTrix.diceRoll == 1)
        statement = "Somehow diceRoll is %s, and not 1 or 0"%(str(binTrix.diceRoll))
        self.assertTrue(result,statement)

    def test_setGameOptions_Dict_xo_xFirst(self):
        x = "x"
        o = "o"
        isFirst = 0
        opts = binTrix.setGameOptions(x,o,isFirst)
        p1CharTest = opts["player1"] == "x"
        p2CharTest = opts["player2"] == "o"
        p1LoseTest = opts["player1Win"] == False
        p2LoseTest = opts["player2Win"] == False
        playerTurnTest = opts["firstTurn"] == "player1"
        currentFirstTest = opts["currentlyFirstTurn"] == True
        p1Statement = "Player 1 is not the correct character"
        p2Statement = "Player 2 is not the correct character"
        p1LoseStatement = "Player 1 has NOT won this test game"
        p2LoseStatement = "Player 2 has NOT won this test game"
        playerIsntFirst = "Player1 should be having their turn 1st!"

    def test_setGameOptions_Dict_xo_oFirst(self):
        x = "x"
        o = "o"
        isFirst = 1
        opts = binTrix.setGameOptions(x,o,isFirst)
        p1CharTest = opts["player1"] == "x"
        p2CharTest = opts["player2"] == "o"
        p1LoseTest = opts["player1Win"] == False
        p2LoseTest = opts["player2Win"] == False
        playerTurnTest = opts["firstTurn"] == "player2"
        currentFirstTest = opts["currentlyFirstTurn"] == True
        p1Statement = "Player 1 is not the correct character"
        p2Statement = "Player 2 is not the correct character"
        p1LoseStatement = "Player 1 has NOT won this test game"
        p2LoseStatement = "Player 2 has NOT won this test game"
        playerIsntFirst = "Player1 should be having their turn 1st!"

        self.assertTrue(p1CharTest,p1Statement)
        self.assertTrue(p2CharTest,p2Statement)
        self.assertTrue(p1LoseTest,p1LoseStatement)
        self.assertTrue(p2LoseTest,p2LoseStatement)
        self.assertTrue(playerTurnTest,playerIsntFirst)
    '''
    **************TEST USER INPUT********************
    *************************************************
    *************************************************
    '''
    def test_input_decideOnMove_badInput1(self):
        debug = "badInput"
        correctOutput = -55
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be -77 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_badInput2(self):
        debug = " Hi, I'm Cyborg Ean! :D"
        correctOutput = -55
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be -77 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_badInput3(self):
        debug = "01001010LOLJUSTKIDDING"
        correctOutput = -55
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be -77 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_badInput4(self):
        debug = "0 10 1 01 01 01 0"
        correctOutput = -55
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be -77 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_badInput5(self):
        debug = 77
        correctOutput = -55
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be -77 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_badInput6(self):
        debug = True
        correctOutput = -55
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be -77 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_badInput7(self):
        debug = False
        correctOutput = -55
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be -77 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_top_left(self):
        debug = "0001"
        correctOutput = 1
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_top_center(self):
        debug = "0010"
        correctOutput = 2
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_top_right(self):
        debug = "0011"
        correctOutput = 3
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_mid_left(self):
        debug = "0100"
        correctOutput = 4
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_mid_center(self):
        debug = "0101"
        correctOutput = 5
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 5 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_mid_right(self):
        debug = "0110"
        correctOutput = 6
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_bottom_left(self):
        debug = "0111"
        correctOutput = 7
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_bottom_center(self):
        debug = "1000"
        correctOutput = 8
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_bottom_right(self):
        debug = "1001"
        correctOutput = 9
        decision = binTrix.decideOnMove(debug)
        result = decision == correctOutput
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_characterRequest_x(self):
        testChar = "x"
        choice = binTrix.characterRequest(testChar)
        result = choice == testChar
        statement = "This is not the correct character"
        self.assertTrue(result,statement)

    def test_characterRequest_o(self):
        testChar = "o"
        choice = binTrix.characterRequest(testChar)
        result = choice == testChar
        statement = "This is not the correct character"
        self.assertTrue(result,statement)

    def test_characterRequest_9(self):
        testChar = "9"
        choice = binTrix.characterRequest(testChar)
        result = choice == testChar
        statement = "This is not the correct character"
        self.assertTrue(result,statement)

if __name__ == "__main__":
    unittest.main()
