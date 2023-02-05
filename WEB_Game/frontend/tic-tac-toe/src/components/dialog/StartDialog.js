import React, { useState } from "react";
import { NotificationManager } from 'react-notifications';
import ReactDOM from "react-dom";
import './Dialog.css';
import 'react-notifications/lib/notifications.css';

const Backdrop = () => {
    return (
        <div className="backdrop"></div>
    )
}

const DialogOverlay = (props) => {
    const[selectedStarter, setSelectedStarter] = useState('');
    const[selectedLevel, setSelectedLevel] = useState('');

    const onStarterSelected = (event) => {
        let starter = event.target.value;
        setSelectedStarter(starter);
    }

    const onLevelSelected = (event) => {
        let level = event.target.value;
        setSelectedLevel(level);
    }

    const closeDialog = (event) => {
        event.preventDefault();
        //Check if user selected starter and level
        if(selectedStarter === ''){
            NotificationManager.error("You need to choose who starts", "No Starter", 5000);
        } else {
            if (selectedLevel === ''){
                NotificationManager.error("You need to choose a level", "No Level", 5000);
            } else {
                props.closeDialog(selectedStarter, selectedLevel);
            }
        }
    }

    return (
        <div className="dialog">
            <section>
                <h1>Who starts?</h1>
                <div className="btns" onChange={onStarterSelected}>
                    <div className="rdb">
                        <input type="radio" id="machine" value="machine" checked={selectedStarter === "machine"}/>
                        <label for="machine">Computer</label>
                    </div>
                    <div className="rdb">
                        <input type="radio" id="player" value="player" checked={selectedStarter === "player"}/>
                        <label for="player">Player</label>
                    </div>
                </div>
            </section>
            <section>
                <h1>Computer level</h1>
                <div className="btns" onChange={onLevelSelected}>
                    <div className="rdb">
                        <input type="radio" id="normal" value="normal" checked={selectedLevel === "normal"}/>
                        <label for="normal">Normal</label>
                    </div>
                    <div className="rdb">
                        <input type="radio" id="advanced" value="advanced" checked={selectedLevel === "advanced"}/>
                        <label for="advanced">Advanced</label>
                    </div>
                </div>
            </section>
            <footer>
                <button onClick={closeDialog} id="start">Start</button>
            </footer>
        </div>
    )
}

const StartDialog = (props) => {

    const closeDialog = (starter, level) => {
        props.closeDialog(starter,level);
    }

    return (
        <React.Fragment>
            {ReactDOM.createPortal(<Backdrop />, document.getElementById('backdrop-root'))}
            {ReactDOM.createPortal(<DialogOverlay closeDialog={closeDialog} />, document.getElementById('overlay-root'))}
        </React.Fragment>
    )
}

export default StartDialog;