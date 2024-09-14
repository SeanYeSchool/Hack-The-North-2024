import "./App.css";

import Home from "./components/home/home.js";
import Routine from "./components/routine/routine.js";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <div className="App">
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
      <Home/>
    </div>
  );
}

export default App;
