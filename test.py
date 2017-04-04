import unittest
import binaryMatrix as binTrix

class binaryMatrixTest(unittest.TestCase):

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
        
    def test_matrix_data_one(self):
        dataX = 0b010100000
        dataY = 0b001000001
        testData = binTrix.matrixData(dataX,dataY,'x','y')
        correctList = [" ","x","o","x"," "," "," "," ","o",]
        statement = "This table is incorrect."
        self.assertEqual(correctList,testData,statment)
                         
    def test_matrix_data_size(self):
        dataX = 0b010100000
        dataY = 0b001000001
        testData = binTrix.matrixData(dataX,dataY,'x','y')
        testSize = len(testData)
        correctSize = 9
        statement = "This table is incorrect."
        self.assertEqual(correctSize,testSize,statement)

if __name__ == "__main__":
    unittest.main()
