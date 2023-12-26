from random import randrange, choice
from GL.MachineAI import MachineAI

class AdvancedAI(MachineAI):

    def __init__(self, board: list, playerOption, machineOption):
        super().__init__(board, playerOption, machineOption)

    def runAI(self) -> int:
        #Obtener la jugada devuelta por el nivel normal
        tempOption = super().runAI()
        
        #Si la jugada no es 0 entonces se tiene que jugar la esa opcion
        if tempOption != 0:
            return tempOption
        
        #Jugada avanzada 1
        advanced_result = self.advanced_block_corners_move()
        if advanced_result != 0 and MachineAI.turns == 2:
            return advanced_result

        return 0


    def advanced_block_corners_move(self) -> int:
        #Opciones que tiene que seleccionar si hay esta jugada
        side_options = [2, 4, 6, 8]
        corner_pairs = [[1, 9], [3, 7]]

        for pair in corner_pairs:
            if pair[0] not in self.currentBoard[0] and pair[1] not in self.currentBoard[2]:
                #Tiene que retornar una de las opciones laterales
                return choice(side_options)
        
        return 0
