import React from "react";
import './Score.css';

const Score = (props) => {
    const score = props.score;

    return (
        <div className="guide-card">
            <div className="symbol-area" id="computer-symbol">
                <h3>{score.machine}</h3>
            </div>
           <h3>Computer</h3>
           <br></br>
           <br></br>
           <div className="symbol-area" id="player-symbol">
                <h3>{score.player}</h3>
            </div>
            <h3>Player</h3>
        </div>
    );
}

export default Score;