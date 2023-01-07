import React from "react";
import './Guide.css';

const Guide = () => {
    return (
        <div className="guide-card">
            <div className="symbol-area">
                <h3>X</h3>
            </div>
           <h3>Machine</h3>
           <br></br>
           <br></br>
           <div className="symbol-area">
                <h3>O</h3>
            </div>
            <h3>Player</h3>
        </div>
    );
}

export default Guide;