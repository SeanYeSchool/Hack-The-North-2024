import "./App.css";

import Home from "./components/home/home.js";
import Routine from "./components/routine/routine.js";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import { ConvexProvider, ConvexReactClient } from "convex/react";

const convex = new ConvexReactClient("https://greedy-warbler-756.convex.cloud");

function App() {
  return (
    <div className="App">
      <ConvexProvider client={convex}>
      <Router>
        <div>
        <Link to="/routine">Go to routine</Link>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/routine" element={<Routine />} />
            {/* ... other routes */}
          </Routes>
        </div>
      </Router>
      </ConvexProvider>
    </div>
  );
}

export default App;
