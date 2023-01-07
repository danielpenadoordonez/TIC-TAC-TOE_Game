import React, { Fragment } from "react";
import Field from "../field/Field";
import classes from './Board.css';

const Board = (props) => {
    let fields = [];

    const createFields = () => {
        for (let value = 1; value <= 9; value++) {
            fields.push(<Field value={value} />)
        }
    }

    createFields();
    return (
        <div className="board">
            {fields}
        </div>
    )
}

export default Board;