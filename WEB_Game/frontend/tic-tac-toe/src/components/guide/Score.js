import React from "react";
import './Score.css';

const Score = (props) => {
    const score = props.score;

    return (
        <div className="guide-card">
            <section className="score" id="player-section">
                <h3>Player</h3>
                <div className="symbol-area" id="player-symbol">
                    <h3>{score.player}</h3>
                </div>
            </section>
            <section className="score" id="computer-section">
                <h3>Computer</h3>
                <div className="symbol-area" id="computer-symbol">
                    <h3>{score.machine}</h3>
                </div>
            </section>
        </div>
    );
}

export default Score;