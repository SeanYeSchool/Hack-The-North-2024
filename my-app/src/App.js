import "./App.css";
import {useRef, useEffect, useState} from "react"

import Home from "./components/home/home.js";

function App() {
  return <div className="App">
    <div className="container">
      <Home/>
    </div>
  </div>;
}

export default App;