import unittest
from GL.AdvancedAI import AdvancedAI

class TestAdvancedAI(unittest.TestCase):

    def test_advanced_block_corners_move(self):
        board = []
        row1 = [1, 2, '0']
        row2 = [4, 'X', 6]
        row3 = ['0', 8, 9]
        board.append(row1)
        board.append(row2)
        board.append(row3)

        machineAI = AdvancedAI(board, 'O', 'X')
        result = machineAI.advanced_block_corners_move()
        #Prueba de unidad falla si el resultado da 0
        #Con ese tablero de prueba, el resultado no deberia ser 0
        self.assertNotEqual(result, 0)


if __name__ == "__main___":
    unittest.main()