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
    <><div>
            <h2>Hello world!</h2>
            <p>
                This is a simple hero unit, a simple Hero-style component for calling extra
                attention to featured content or information.
            </p>

            <hr class="my-4" />

            <p>
                It uses utility classes for typography and spacing to space content out within the
                larger container.
            </p>
            <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary">
                Learn more
            </button>
        </div>
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