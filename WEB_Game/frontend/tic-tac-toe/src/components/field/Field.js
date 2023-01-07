import React from "react";
import './Field.css';

const Field = (props) => {
    let value = props.value;
    let symbol = props.symbol;

    function test(){
        console.log(`Button Value: ${value}`);
    }

    return(
        <button className='field' value={value} onClick={test}>
            <h1>{symbol}</h1>
        </button>
    );
}

export default Field;