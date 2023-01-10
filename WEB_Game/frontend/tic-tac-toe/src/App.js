import React, { useState, useEffect } from 'react';
import Board from './components/table/Board';
import Guide from './components/guide/Guide';
import Controls from './components/controls/Controls';
import './App.css';

function App() {
  const[board, setBoard] = useState([]);

  async function loadBoard(){
    const response = await fetch('http://localhost:8080/');
    const data = await response.json();
    setBoard(data.board);
  } 

  useEffect(() => {
    loadBoard();
  }, []);

  return (
    <div className="App">
      <h1 className='main-title'>TIC-TAC-TOE</h1>
      <Controls />
      <Board board={board}/>
      <Guide />
    </div>
  );
}

export default App;
