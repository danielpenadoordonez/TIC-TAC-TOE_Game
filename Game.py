from random import randrange
import time

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
                        self.row1[j] = f'{self.BLUE}O{self.CLEAR}'
                elif cont == 2:
                    if self.row2[j] == move:
                        self.row2[j] = f'{self.BLUE}O{self.CLEAR}'
                elif cont == 3:
                    if self.row3[j] == move:
                        self.row3[j] = f'{self.BLUE}O{self.CLEAR}'
            cont += 1            

    def machineMove(self):
        invalid = True
        #Ciclo para validar que la opcion aleatoria este disponible
        machineOption = 0
        while invalid:
            randNum = randrange(1,10)
            if randNum in self.row1 or randNum in self.row2 or randNum in self.row3:
                invalid = False 
                machineOption = randNum 
        cont = 1   
        #Recorre las tres filas del tablero
        for i in range(len(self.board)):
            #Recorre cada una de las filas dependiendo del contador, este indica la fila que va evaluar
            for j in range(len(self.row1)):
                if cont == 1:
                    if self.row1[j] == machineOption:
                        self.row1[j] = f'{self.GREEN}X{self.CLEAR}'
                elif cont == 2:
                    if self.row2[j] == machineOption:
                        self.row2[j] = f'{self.GREEN}X{self.CLEAR}'
                elif cont == 3:
                    if self.row3[j] == machineOption:
                        self.row3[j] = f'{self.GREEN}X{self.CLEAR}'
            cont += 1

    def numbers_In_Board(self):
        #Para verificar que haya un empate hay que asegurarse que no haya habido gane y que 
        #todas los campos del tablero esten con 0 o x, en otras palabras que no haya numeros en el tablero
        numbers = 0
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                space = self.board[row][column]
                if space != f'{self.BLUE}O{self.CLEAR}' and space != f'{self.GREEN}X{self.CLEAR}':
                    numbers += 1
        return numbers 


    def victory(self):
        userOption = f'{self.BLUE}O{self.CLEAR}'
        machineOption = f'{self.GREEN}X{self.CLEAR}'
        #Se recorre todas las filas del tablero 
        for row in self.board:
            #Se recorre primero las filas horizontalmente para validar que haya gane
            if row[0] == userOption and row[1] == userOption and row[2] == userOption:
                self.winner = "user"
                return True 
            if row[0] == machineOption and row[1] == machineOption and row[2] == machineOption:
                self.winner = "machine"
                return True 
        #Si no hubo un gane de manera horizontal se revisa de manera vertical
        for index in range(len(self.board)):
            if self.row1[index] == userOption and self.row2[index] == userOption and self.row3[index] == userOption:
                self.winner = "user"
                return True
            if self.row1[index] == machineOption and self.row2[index] == machineOption and self.row3[index] == machineOption:
                self.winner = "machine"
                return True 
        #Si tampoco hubo gane de manera horizontal se tiene que revisar si hubo un gane de forma diagonal
        if self.row2[1] == machineOption:
            if self.row1[0] == machineOption and self.row3[2] == machineOption or self.row1[2] == machineOption and self.row3[0] == machineOption:
                self.winner = "machine"
                return True
        if self.row2[1] == userOption:
            if self.row1[0] == userOption and self.row3[2] == userOption or self.row1[2] == userOption and self.row3[0] == userOption:
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
            ===========================
            RESTARTING THE GAME  
            ===========================""")
            time.sleep(2)  
            return True
        else:
            return False
