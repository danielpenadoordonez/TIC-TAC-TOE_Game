import React, { useState, useEffect } from 'react';
import Board from './components/table/Board';
import Guide from './components/guide/Guide';
import Controls from './components/controls/Controls';
import './App.css';

function App() {
  const[board, setBoard] = useState([]);

  async function loadBoard(){
    //Makes a GET Request to load the board
    const response = await fetch('/get-board');
    const data = await response.json();
    setBoard(data.board);
  }
  
  async function postMove(value){
    const body = {'move': value}
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
  }

  async function restartGame(){
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
  }

  useEffect(() => {
    loadBoard();
  }, []);

  return (
    <div className="App">
      <h1 className='main-title'>TIC-TAC-TOE</h1>
      <Controls restartGame={restartGame}/>
      <Board board={board} postMove={postMove}/>
      <Guide />
    </div>
  );
}

export default App;
