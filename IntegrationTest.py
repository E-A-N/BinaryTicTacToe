import unittest
import BinaryMatrix as game1

class binaryMatrixIntegrationTest(unittest.TestCase):
    ###bitCount function tests###
    def test_gamePath_p1_win(self):
        '''
        For the sake of testing it's assumed
        that player 1 goes first by passing 0 into diceRoll
        '''
        game1.diceRoll = 0 #defaults to 1st player
        p1Char = game1.characterRequest("X!")
        p2Char = game1.characterRequest("o")
        game1.gameSettings = game1.setGameOptions(p1Char,p2Char,game1.diceRoll)
        p1Move = decideOnMove("01")
        currentPly = game1.gameSettings["currentCharacter"]
        statement = "This is the incorrect amound of bits."
        self.assertEqual(bits,count,statement)


if __name__ == "__main__":
    unittest.main()
