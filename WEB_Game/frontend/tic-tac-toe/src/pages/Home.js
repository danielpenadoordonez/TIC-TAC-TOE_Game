import React from "react";
import Menu from "../components/menu/Menu";

function Home() {
    const miniBoard = ['X', 'O', '', '', 'X', '', 'O', '', 'X'];

    return (
        <React.Fragment>
            <div className="App">
                <h1 className='main-title'>TIC-TAC-TOE</h1>
                <div className="board-wrapper">
                <div className="mini-board">
                    {miniBoard.map((val, i) => (
                    <div key={i} className={`cell ${val === 'X' ? 'x' : val === 'O' ? 'o' : ''}`}>
                        {val}
                    </div>
                    ))}
                </div>
                </div>
                <Menu />
            </div>
        </React.Fragment>
    )
}

export default Home;