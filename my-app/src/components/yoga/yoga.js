import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import Button from 'react-bootstrap/Button'
import Canvas from "../canvas/canvas.js";
import "../../App.css";


const SidePanel = () => {
    return (
    <div className="container-fluid">   
    <Button> 
        Good Morning
    </Button>
    <Button>
        Bad Morning
    </Button>
    </div>
    )
}

const Yoga = () => {
    return (
    <>
        <div className="container-fluid">
                <div className="frame">
                    <Canvas />
                </div>
                <SidePanel />
                
        </div>
    </>
    );
}


export default Yoga;