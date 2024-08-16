import React from "react";
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from "./pages/Home";
import ComputerGame from "./pages/ComputerGame";
import PlayerMenu from "./pages/PlayerMenu";
 
function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home />}/>
        <Route path="/home" element={<Home />}/>
        <Route path="/computer-game" element={<ComputerGame />}/>
        <Route path="/player-menu" element={<PlayerMenu />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
