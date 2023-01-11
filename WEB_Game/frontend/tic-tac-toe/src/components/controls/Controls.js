import React from "react";
import './Controls.css'

const Controls = (props) => {

    const restartGame = () => {
        props.restartGame();
    }

    return(
        <div className="btn-container">
            <button className="control-btn" id="start-btn">Start Game</button>
            <button className="control-btn" id="again-btn" onClick={restartGame}>Play Again</button>
        </div>
    );
}

export default Controls;