import unittest
import BinaryMatrix as game1

class binaryMatrixIntegrationTest(unittest.TestCase):
    ###bitCount function tests###
    def test_gamePath_p1_win(self):

        '''
        For the sake of testing it's assumed
        that player 1 goes first by passing 0 into diceRoll
        '''
        game1.diceRoll = 0
        p1Char = "x"
        p2Char = "o"
        game1.gameSettings = game1.setGameOptions(p1Char,p2Char,game1.diceRoll)
        currentPlayer =
        statement = "This is the incorrect amound of bits."
        self.assertEqual(bits,count,statement)


if __name__ == "__main__":
    unittest.main()
