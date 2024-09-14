import "./App.css";
import {useRef, useEffect, useState} from "react"

import SidePanel from "./components/home/home.js";
import Canvas from "./components/canvas/canvas.js";

function App() {
  return <div className="App">
    <div className="container">
      <Canvas />
      <SidePanel/>
    </div>
  </div>;
}

export default App;