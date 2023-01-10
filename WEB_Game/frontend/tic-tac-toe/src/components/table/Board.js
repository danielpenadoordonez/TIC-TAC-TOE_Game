import React from "react";
import Field from "../field/Field";
import classes from './Board.css';

const Board = (props) => {
    const board = props.board;
    let fields = [];

    const createFields = () => {
        // for (let value = 1; value <= 9; value++) {
        //     fields.push(<Field value={value} />)
        // }
        for (let value = 0; value < board.length; value++) {
            //Loop for each row on the board
            for (let index = 0; index < board[value].length; index++) {
                let element = board[value][index]; //Value on the field
                let symbol = undefined;
                //Assing the symbol X or O, if there is a number then it is left as undefined
                if (element === "O") {
                    symbol = "O";
                } else {
                    if (element === "X") {
                        symbol = "X";
                    }
                }
                fields.push(<Field value={element} symbol={symbol} />);
            }
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