import React, { useState, useEffect } from 'react';
import Board from './components/table/Board';
import Guide from './components/guide/Guide';
import Controls from './components/controls/Controls';
import './App.css';

function App() {
  const [board, setBoard] = useState([]);
  const [winner, setWinner] = useState(null);
  const[currentPlayer, setCurrentPlayer] = useState('user');

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
    setCurrentPlayer('computer');
  }

  async function getComputerMove() {
    //Make a GET Request to fetch the computer move
    const response = await fetch('/machine-move');
    const data = await response.json();
    setBoard(data.board);

    //Check if the computer won or if there is a tie
    checkWinner();
    //Set the next turn for the user
    setCurrentPlayer('user');
  }

  async function restartGame() {
    //Makes a POST Request to restart the game
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
    setCurrentPlayer('user');
  }

  async function checkWinner() {
    const response = await fetch('/winner');
    const data = await response.json();
    setWinner(data.winner);
  }

  useEffect(() => {
    loadBoard();
  }, []);

  useEffect(() => {
    if (winner === 'user') {
      alert("You won!!");
      restartGame()
    } else {
      if (winner === 'machine') {
        alert("Machine won!!");
        restartGame();
      } else{
        if (winner === 'tie'){
          alert("Tie!!");
          restartGame();
        }
      }
    }
  }, [winner]);

  useEffect(() => {
    if(winner === null && currentPlayer === 'computer'){
      getComputerMove();
    }
  }, [currentPlayer]);

  return (
    <div className="App">
      <h1 className='main-title'>TIC-TAC-TOE</h1>
      <Controls restartGame={restartGame} />
      <Board board={board} postMove={postMove} />
      <Guide />
    </div>
  );
}

export default App;
