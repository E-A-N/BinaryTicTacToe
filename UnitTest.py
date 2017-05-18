import unittest
import BinaryMatrix as binTrix

class binaryMatrixTest(unittest.TestCase):
    ###bitCount function tests###
    def test_bit_count_of_1_bit(self):
        bits = 1 #1
        binAmount = 0b1
        count = binTrix.bitCount(binAmount)
        statement = "This is the incorrect amound of bits."
        self.assertEqual(bits,count,statement)

    def test_bit_count_of_8_bits(self):
        bits = 8 #128
        binAmount = 0b10000000
        count = binTrix.bitCount(binAmount)
        statement = "This is the incorrect amound of bits."
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

    def test_setGameOptions_Dict_xo(self):
        x = "x"
        o = "o"
        opts = binTrix.setGameOptions(x,o)
        p1CharTest = opts["player1"] == "x"
        p2CharTest = opts["player2"] == "o"
        p1LoseTest = opts["player1Win"] == False
        p2LoseTest = opts["player2Win"] == False
        p1Statement = "Player 1 is not the correct character"
        p2Statement = "Player 2 is not the correct character"
        p1LoseStatement = "Player 1 has NOT won this test game"
        p2LoseStatement = "Plyaer 2 has NOT won this test game"
        self.assertTrue(p1CharTest,p1Statement)
        self.assertTrue(p2CharTest,p2Statement)
        self.assertTrue(p1LoseTest,p1LoseStatement)
        self.assertTrue(p2LoseTest,p2LoseStatement)

    def test_input_decideOnMove_top_left(self):
        debug = "0001"
        correct = 1
        decision = binTrix.decideOnMove(debug)
        result = decision == correct
        statement = "Decision should be 1 not %d"%(decision)
        self.assertTrue(result,statement)

    def test_input_decideOnMove_center(self):
        debug = "0101"
        correct = 5
        decision = binTrix.decideOnMove(debug)
        result = decision == correct
        statement = "Decision should be 5 not %d"%(decision)
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
