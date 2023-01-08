import React from 'react';
import Board from './components/table/Board';
import Guide from './components/guide/Guide';
import Controls from './components/controls/Controls';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1 className='main-title'>TIC-TAC-TOE</h1>
      <Controls />
      <Board />
      <Guide />
    </div>
  );
}

export default App;
