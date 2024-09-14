import "./App.css";

import Yoga from "./components/yoga/yoga.js";
import Routine from "./components/routine/routine.js";
import Home from "./components/home/home.js"
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import { ConvexProvider, ConvexReactClient } from "convex/react";

const convex = new ConvexReactClient("https://greedy-warbler-756.convex.cloud");

function App() {
  return (
    <div className="App">
      <ConvexProvider client={convex}>
      <Router>
        <div>
          <Link to="/routine">Landing page =\ Routine</Link> <br />
          <Link to="/canvas">Routine =\ Yoga</Link>
          <Routes>
            <Route path="/" element = {<Home />} />
            <Route path="/routine" element={<Routine />} />
            <Route path="/canvas" element={<Yoga />} /> {/* Change the name of the Home component to Canvas */}
          </Routes>
        </div>
      </Router>
      </ConvexProvider>
    </div>
  );
}

export default App;
