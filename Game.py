from random import randrange
import time
from MachineAI import MachineAI

class Game:

    #Colores para las opciones de jugador
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CLEAR = '\033[0m'

    def __init__(self):
        self.board = []
        self.row1 = [1, 2, 3]
        self.row2 = [4, 5, 6]
        self.row3 = [7, 8, 9]
        self.winner = None
        self.playerOption = None
        self.machineOption = None
        self.createBoard()

    def createBoard(self):
        self.board.append(self.row1)
        self.board.append(self.row2)
        self.board.append(self.row3)

    def restartGame(self):
        self.winner = None
        self.board = []
        self.row1 = [1, 2, 3]
        self.row2 = [4, 5, 6]
        self.row3 = [7, 8, 9]
        self.board.append(self.row1)
        self.board.append(self.row2)
        self.board.append(self.row3)
        MachineAI.turns = 0
        MachineAI.hasCenterPosition = False

    def displayBoard(self):
        r1, r2, r3 = self.row1, self.row2, self.row3
        print("""
            |       |       
            |       |        
     """,r1[0],"""    |""",r1[1],"""    |""",r1[2],"""    
            |       |       
    +-------+-------+-------+
            |       |        
     """,r2[0],"""    |""",r2[1],"""    |""",r2[2],"""           
            |       |       
    +-------+-------+-------+
            |       |        
     """,r3[0],"""    |""",r3[1],"""    |""",r3[2],"""    
            |       |       
            |       |       """)

    def enterMove(self, move):
        cont = 1
        #Recorre las tres filas del tablero
        for i in range(len(self.board)):
            #Recorre cada una de las filas dependiendo del contador, este indica la fila que va evaluar
            for j in range(len(self.row1)):
                if cont == 1:
                    if self.row1[j] == move:
                        self.row1[j] = self.playerOption
                elif cont == 2:
                    if self.row2[j] == move:
                        self.row2[j] = self.playerOption
                elif cont == 3:
                    if self.row3[j] == move:
                        self.row3[j] = self.playerOption
            cont += 1            

    def machineMove(self):
        machineAI = MachineAI(self.board, self.playerOption, self.machineOption)
        #Ciclo para validar que la opcion aleatoria este disponible
        machineChoice = 0
        invalid = True
        while invalid:
            randNum = machineAI.runAI()
            if randNum in self.row1 or randNum in self.row2 or randNum in self.row3:
                invalid = False 
                machineChoice = randNum 
        cont = 1   
        #Recorre las tres filas del tablero
        for i in range(len(self.board)):
            #Recorre cada una de las filas dependiendo del contador, este indica la fila que va evaluar
            for j in range(len(self.row1)):
                if cont == 1:
                    if self.row1[j] == machineChoice:
                        self.row1[j] = self.machineOption
                elif cont == 2:
                    if self.row2[j] == machineChoice:
                        self.row2[j] = self.machineOption
                elif cont == 3:
                    if self.row3[j] == machineChoice:
                        self.row3[j] = self.machineOption
            cont += 1

    def numbers_In_Board(self):
        #Para verificar que haya un empate hay que asegurarse que no haya habido gane y que 
        #todas los campos del tablero esten con 0 o x, en otras palabras que no haya numeros en el tablero
        numbers = 0
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                space = self.board[row][column]
                if space != self.playerOption and space != self.machineOption:
                    numbers += 1
        return numbers 


    def victory(self):
        #Se recorre todas las filas del tablero 
        for row in self.board:
            #Se recorre primero las filas horizontalmente para validar que haya gane
            if row[0] == self.playerOption and row[1] == self.playerOption and row[2] == self.playerOption:
                self.winner = "user"
                return True 
            if row[0] == self.machineOption and row[1] == self.machineOption and row[2] == self.machineOption:
                self.winner = "machine"
                return True 
        #Si no hubo un gane de manera horizontal se revisa de manera vertical
        for index in range(len(self.board)):
            if self.row1[index] == self.playerOption and self.row2[index] == self.playerOption and self.row3[index] == self.playerOption:
                self.winner = "user"
                return True
            if self.row1[index] == self.machineOption and self.row2[index] == self.machineOption and self.row3[index] == self.machineOption:
                self.winner = "machine"
                return True 
        #Si tampoco hubo gane de manera horizontal se tiene que revisar si hubo un gane de forma diagonal
        if self.row2[1] == self.machineOption:
            if self.row1[0] == self.machineOption and self.row3[2] == self.machineOption or self.row1[2] == self.machineOption and self.row3[0] == self.machineOption:
                self.winner = "machine"
                return True
        if self.row2[1] == self.playerOption:
            if self.row1[0] == self.playerOption and self.row3[2] == self.playerOption or self.row1[2] == self.playerOption and self.row3[0] == self.playerOption:
                self.winner = "user"
                return True
        return False #Se retorna False si no hubo gane de ninguna forma


    def is_num_in_Board(self, num):
        return num in self.row1 or num in self.row2 or num in self.row3

    @staticmethod
    def play_Again():
        answer = input("PLAY AGAIN ??? (Y/N): ")
        if answer == 'Y' or answer == 'y' or answer == "Yes" or answer == "yes":
            print("""
            ===========================================
            RESTARTING THE GAME / REINICIANDO EL JUEGO 
            ===========================================""")
            time.sleep(2)  
            return True
        else:
            return False
