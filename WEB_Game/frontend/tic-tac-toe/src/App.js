import React, { useState, useEffect } from 'react';
import { NotificationContainer, NotificationManager } from 'react-notifications';
import Board from './components/table/Board';
import Score from './components/guide/Score';
import Controls from './components/controls/Controls';
import StartDialog from './components/dialog/StartDialog';
import './App.css';
import 'react-notifications/lib/notifications.css';

function App() {
  const [board, setBoard] = useState([]);
  const [winner, setWinner] = useState(null);
  const[currentPlayer, setCurrentPlayer] = useState('user');
  const[starter, setStarter] = useState('user');
  const[level, setLevel] = useState('normal');
  const[gamesPlayed, setGamesPlayed] = useState(0);
  const[score, setScore] = useState({"player": 0, "machine": 0});
  const[disableBoard, setDisableBoard] = useState(true);

  async function loadBoard() {
    //Makes a GET Request to load the board
    const response = await fetch('/get-board');
    const data = await response.json();
    setBoard(data.board);
  }

  async function postMove(value) {
    const body = { 'move': value }
    //Makes a POST Request with the move the user made
    const response = await fetch('/move', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    });
    const data = await response.json();
    setBoard(data.board);

    //Check if the player won or if there is a tie
    checkWinner();
    //Set the next turn for the computer
    setCurrentPlayer('machine');
    //Disable board temporarely
    setDisableBoard(true);
  }

  async function getComputerMove() {
    //Make a GET Request to fetch the computer move
    const response = await fetch('/machine-move?level=' + level);
    const data = await response.json();
    setBoard(data.board);

    //Check if the computer won or if there is a tie
    checkWinner();
    //Set the next turn for the user
    setCurrentPlayer('user');
    //Enable the board again
    setDisableBoard(false);
  }

  async function restartGame() {
    //Makes a POST Request to restart the game
    //There are two calls to the restart endpoint to implement a workaround
    //for a bug where the board wasn't restarted properly
    await fetch('/restart', {
      method: 'PUT',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const response = await fetch('/restart', {
      method: 'PUT',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const data = await response.json();
    setBoard(data.board);
    checkWinner();
    //setCurrentPlayer('user');
    setGamesPlayed(gamesPlayed + 1);
  }

  async function checkWinner() {
    //Makes a GET request to check if there is already a winner
    const response = await fetch('/winner');
    const data = await response.json();
    setWinner(data.winner);
  }

  const startGame = () => {
    setStarter('');
    setScore({"player": 0, "machine": 0});
    restartGame();
  }

  const closeDialog = (starter, level) => {
    setStarter(starter);
    setLevel(level);
    //Activate the board for the game
    setDisableBoard(false);
}

  useEffect(() => {
    loadBoard();
  }, []);

  useEffect(() => {
    if (winner === 'user') {
      NotificationManager.success("You won!!", "", 5000);
      restartGame();
      setStarter(winner);
      setScore({"player": score.player += 1, "machine": score.machine})
    } else {
      if (winner === 'machine') {
        NotificationManager.warning("Machine won!!", "", 5000);
        restartGame();
        setStarter(winner);
        setScore({"player": score.player, "machine": score.machine += 1})
      } else{
        if (winner === 'tie'){
          NotificationManager.info("Tie!!", "", 5000);
          restartGame();
        }
      }
    }
  }, [winner]);

  useEffect(() => {
    if(currentPlayer === 'machine'){
      getComputerMove();
    }
  }, [currentPlayer]);

  useEffect(() => {
    //Each time the starter changes or a new game start this code runs
    if(starter === 'machine'){
      getComputerMove();
    }
  }, [starter, gamesPlayed]);

  return (
    <div className="App">
      {!starter && <StartDialog closeDialog={closeDialog}/>}
      <h1 className='main-title'>TIC-TAC-TOE</h1>
      <Controls startGame={startGame} restartGame={restartGame} />
      <Board board={board} postMove={postMove} enabled={disableBoard}/>
      <Score score={score}/>
      <NotificationContainer />
    </div>
  );
}

export default App;
