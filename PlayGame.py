from random import randrange
import time 
import subprocess
from Game import Game

game = Game()
    
print(f"""
==============================
Player(You) = {game.BLUE}0{game.CLEAR}
Machine = {game.GREEN}X{game.CLEAR}
==============================
""")

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
                    continue
                else:
                    break
            elif game.winner == "machine":
                print("Game Over, MACHINE WINS\n")
                if Game.play_Again():
                    game.restartGame()
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
                    continue
                else:
                    break
            elif game.winner == "machine":
                print("Game Over, MACHINE WINS\n")
                if Game.play_Again():
                    game.restartGame()
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
                continue
            else:
                break 
     
