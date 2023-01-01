from random import randrange

class MachineAI:

    turns = 0
    #hasCenterPosition : bool = False
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CLEAR = '\033[0m'

    def __init__(self, board:list, playerOption, machineOption):
        self.currentBoard = list()
        self.backupBoard = board
        self.playerOption = playerOption
        self.machineOption = machineOption
        self.build_Current_Board(board)
        MachineAI.turns += 1

    def build_Current_Board(self, board):
        self.currentBoard.clear()
        #Se crea una copia de cada fila del tablero
        self.currentBoard = [row[:] for row in board]

    def runAI(self) -> int:
        #Evaluacion de jugadas
        move = self.study_Moves()
        if move > 0:
            return move

        if MachineAI.turns == 2:
            #Primero se tiene que ver si el jugador ya tiene opcion de gane
            playerwinningPosition = self.study_Player_Positions()
            if playerwinningPosition > 0:
                return playerwinningPosition
            
        #Tiene que buscar un patrón de posible gane
        machineWinningPositions = self.study_Machine_Positions()
        if machineWinningPositions > 0:
            return machineWinningPositions
        
        playerWinningPosition = self.study_Player_Positions()
        if playerWinningPosition > 0:
            return playerWinningPosition
            
        return randrange(1, 10)

    def study_Player_Positions(self):
        #Se traen los espacios disponibles
        freeSpaces = self.get_free_Spaces()
        #Por cada espacio disponible se tiene que ver si puede ser 
        #una victoria para el usuario
        for space in freeSpaces:
            self.test_User_Move(space)
            if self.test_Victory() == 'user':
                return space
            #Se tiene que restaurar el tablero
            self.build_Current_Board(self.backupBoard)
        return 0

    def study_Machine_Positions(self):
        #Se traen los espacios disponibles
        freeSpaces = self.get_free_Spaces()
        for space in freeSpaces:
            self.test_Machine_Move(space)
            if self.test_Victory() == 'machine':
                return space
            self.build_Current_Board(self.backupBoard)
        return 0

    def study_Moves(self):
        """
          Returns a move if it is necesary
        """
        if MachineAI.turns == 1:
            cornerNums = [1, 3, 7 , 9]
            allCornersAvailable = True
            for corner in cornerNums:
                if corner not in self.currentBoard[0] and corner not in self.currentBoard[2]:
                    allCornersAvailable = False
                    return 5
        return 0

    def get_free_Spaces(self):
        freeSpaces = list()
        for row in range(len(self.currentBoard)):
            for column in range(len(self.currentBoard[0])):
                space = self.currentBoard[row][column]
                try:
                    space = str(space)
                except ValueError:
                    pass
                else:
                    if space.isdigit():
                        freeSpaces.append(int(space))
        return freeSpaces

    def test_User_Move(self, space):
        #Recorre las tres filas del tablero
        for row in range(len(self.currentBoard)):
            #Recorre cada una de las filas dependiendo del contador, este indica la fila que va evaluar
            for col in range(len(self.currentBoard[0])):
                if self.currentBoard[row][col] == space:
                    self.currentBoard[row][col] = self.playerOption

    def test_Machine_Move(self, space):
        #Recorre las tres filas del tablero
        for row in range(len(self.currentBoard)):
            #Recorre cada una de las filas dependiendo del contador, este indica la fila que va evaluar
            for col in range(len(self.currentBoard[0])):
                if self.currentBoard[row][col] == space:
                    self.currentBoard[row][col] = self.machineOption

    def test_Victory(self):
        #Se recorre todas las filas del tablero 
        for row in self.currentBoard:
            #Se recorre primero las filas horizontalmente para validar que haya gane
            if row[0] == self.playerOption and row[1] == self.playerOption and row[2] == self.playerOption:
                return "user"
            if row[0] == self.machineOption and row[1] == self.machineOption and row[2] == self.machineOption:
                return "machine"
        #Si no hubo un gane de manera horizontal se revisa de manera vertical
        for index in range(len(self.currentBoard)):
            if self.currentBoard[0][index] == self.playerOption and self.currentBoard[1][index] == self.playerOption and self.currentBoard[2][index] == self.playerOption:
                return "user"
            if self.currentBoard[0][index] == self.machineOption and self.currentBoard[1][index] == self.machineOption and self.currentBoard[2][index] == self.machineOption:
                return "machine"
        #Si tampoco hubo gane de manera horizontal se tiene que revisar si hubo un gane de forma diagonal
        if self.currentBoard[1][1] == self.machineOption:
            if self.currentBoard[0][0] == self.machineOption and self.currentBoard[2][2] == self.machineOption or self.currentBoard[0][2] == self.machineOption and self.currentBoard[2][0] == self.machineOption:
                return "machine"
        if self.currentBoard[1][1] == self.playerOption:
            if self.currentBoard[0][0] == self.playerOption and self.currentBoard[2][2] == self.playerOption or self.currentBoard[0][2] == self.playerOption and self.currentBoard[2][0] == self.playerOption:
                return "user"
        return None

        