from random import randrange
import time 
import subprocess
import platform
from Game import Game

if __name__ == "__main__":

    #Las opciones para jugar dependen el SO en que corre
    RUNNING_OS = platform.system()
    playerOption = None
    machineOption = None

    game = Game()

    if RUNNING_OS == "Windows":
        playerOption = 'O'
        machineOption = 'X'
    else:
        playerOption = f'{game.BLUE}O{game.CLEAR}'
        machineOption = f'{game.GREEN}X{game.CLEAR}'

    game.playerOption = playerOption
    game.machineOption = machineOption

    #Diccionario con las opciones de inicio
    startOptions = {'1' : "Player", '2' : "Machine"}

    #Se pregunta quien inicia
    ops = ['1', '2']
    starter = input("""
........WHO IS GOING TO START ? / ¿Quién comienza?....................
    1. You / Usted
    2. Machine / Computadora

    > """)

    while starter not in ops:
        print("Invalid choice")
        time.sleep(1)
        starter = input("> ")
        
    print(f"""
==============================
Player(You) / Usted = {playerOption}
Machine / Computadora = {machineOption}
==============================
    """)

    def machine_Starts():
        """
        This runs if the machine starts first
        """
        print("MACHINE......")
        game.machineMove()
        game.displayBoard()

    #Si la maquina es la que empieza el juego
    if startOptions.get(starter) == "Machine":
        machine_Starts()

    while True:
        print("YOUR TURN......")
        game.displayBoard()
        move = input("Enter your move or type exit to close the game: ")

        if move == "exit":
            break
        numEntered = 0
        #Si el usuario no ingreso exit, se tiene que validar que haya ingresado un digito
        try:
            numEntered = int(move)
        except ValueError:
            print("INVALID MOVE, YOU MUST ENTER A NUMBER AVAILABLE ON THE BOARD OR TYPE EXIT TO CLOSE THE GAME\n")
            time.sleep(2)
            continue 
        #Se tiene que validar que el numero elegido por el usuario este en el tablero
        if not game.is_num_in_Board(numEntered):
            print("INVALID MOVE, THE OPTION YOU HAVE CHOSEN IS NOT AVAILABLE ON THE BOARD\n")
            time.sleep(2)

        else:
            print("YOUR TURN......")
            game.enterMove(numEntered)
            game.displayBoard()
            userWin = game.victory()
            #Despues que el usuario hace su jugada se verifica si esta hace un gane o no
            if userWin:
                if game.winner == "user":
                    print("Game Over, YOU WON\n")
                    #Si el usuario elige jugar de nuevo se reinicia el juego
                    #Si no, entonces se termina
                    #Este proceso se repite cada vez que haya un gane o un empate
                    if Game.play_Again():
                        game.restartGame()
                        if startOptions.get(starter) == "Machine":
                            machine_Starts()
                        continue
                    else:
                        break
                elif game.winner == "machine":
                    print("Game Over, MACHINE WINS\n")
                    if Game.play_Again():
                        game.restartGame()
                        if startOptions.get(starter) == "Machine":
                            machine_Starts()
                        continue
                    else:
                        break 
                else:
                    print("There was an error")
                    break
            #Se verifica si hay un empate luego de la jugada del usuario
            numsBoard = game.numbers_In_Board()
            if numsBoard == 0:
                print("Game Over, TIE\n")
                if Game.play_Again():
                    game.restartGame()
                    if startOptions.get(starter) == "Machine":
                        machine_Starts()
                    continue
                else:
                    break 
            print("MACHINE......")
            time.sleep(1)
            game.machineMove()
            game.displayBoard()
            #Despues que la maquina hace su jugada se verifica si esta hace un gane o no
            machineWin = game.victory()
            if machineWin:
                if game.winner == "user":
                    print("Game Over, YOU WON\n")
                    if Game.play_Again():
                        game.restartGame()
                        if startOptions.get(starter) == "Machine":
                            machine_Starts()
                        continue
                    else:
                        break
                elif game.winner == "machine":
                    print("Game Over, MACHINE WINS\n")
                    if Game.play_Again():
                        game.restartGame()
                        if startOptions.get(starter) == "Machine":
                            machine_Starts()
                        continue
                    else:
                        break 
                else:
                    print("There was an error")
                    break
            #Se verifica si hay un empate luego de la jugada de la maquina
            numsBoard = game.numbers_In_Board()
            if numsBoard == 0:
                print("Game Over, TIE\n")
                if Game.play_Again():
                    game.restartGame()
                    if startOptions.get(starter) == "Machine":
                        machine_Starts()
                    continue
                else:
                    break 
     
