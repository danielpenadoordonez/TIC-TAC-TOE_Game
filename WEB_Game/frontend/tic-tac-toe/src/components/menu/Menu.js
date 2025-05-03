import React from "react"
import { Link } from "react-router-dom"
import './Menu.css'
import Logo from './Logo.png'

const Menu = (props) => {
    return(
        <div>
            <div>  
                <Link to="/computer-game" className="link">
                    <button className="menu-btn">Play against Computer</button>
                </Link>
            </div>
                <Link to="/player-menu" className="link">
                    <button className="menu-btn">Play against Person</button>
                </Link>
        </div>
    )
}

export default Menu;