import React from "react";
import './Controls.css'

const Controls = () => {
    return(
        <div className="btn-container">
            <button className="control-btn" id="start-btn">Start Game</button>
            <button className="control-btn" id="again-btn">Play Again</button>
        </div>
    );
}

export default Controls;