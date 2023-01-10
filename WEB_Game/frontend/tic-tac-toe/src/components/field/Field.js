import React from "react";
import './Field.css';

const Field = (props) => {
    let value = props.value; //Value on the field
    let symbol = props.symbol; //Value that will be visible on the UI
    let button = <button className='field' value={value} onClick={postMove}>
                    <h1>{symbol}</h1>
                </button>;

    function postMove() {
        console.log(`Button Value: ${value}`);
    }

    //This if will determine if the field on the board will have a color and which one
    //depending on the id (computer ot player)
    if (symbol === "X") {
        button = <button className='field' id="computer-symbol" value={value} onClick={postMove}>
                   <h1>{symbol}</h1>
                </button>;
    } else {
        if (symbol === "O") {
            button = <button className='field' id="player-symbol" value={value} onClick={postMove}>
                        <h1>{symbol}</h1>
                    </button>;
        }
    }

    return (
        <React.Fragment>
            {button}
        </React.Fragment>
    );
}

export default Field;