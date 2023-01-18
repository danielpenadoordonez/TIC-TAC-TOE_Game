from random import randrange
from GL.MachineAI import MachineAI

class AdvancedAI(MachineAI):

    def __init__(self, board: list, playerOption, machineOption):
        super().__init__(board, playerOption, machineOption)