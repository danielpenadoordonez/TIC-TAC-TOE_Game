import React from "react";
import Menu from "../components/menu/Menu";

function Home() {
    return (
        <React.Fragment>
            <div className="App">
                <h1 className='main-title'>TIC-TAC-TOE</h1>
                <Menu />
            </div>
        </React.Fragment>
    )
}

export default Home;