import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import Button from 'react-bootstrap/Button'
import Canvas from "../canvas/canvas.js";
import "../../App.css";


const SidePanel = () => {
    return (
    <div className="container">   
    <Button> 
        Good Morning
    </Button>
    <Button>
        Bad Morning
    </Button>
    </div>
    )
}

const Home = () => {
    return (

    <div className="container">
        <div className="frame">
            <Canvas/>
        </div>
        <SidePanel/>
    </div>
    );
}


export default Home