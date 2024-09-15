import "./App.css";

import Yoga from "./components/yoga/yoga.js";
import Routine from "./components/routine/routine.js";
import Home from "./components/home/home.js";

import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from "react-router-dom";
import { useState } from "react";

import { ConvexProvider, ConvexReactClient } from "convex/react";
import { ClerkProvider, useAuth } from "@clerk/clerk-react";
import { ConvexProviderWithClerk } from "convex/react-clerk";

const convex = new ConvexReactClient("https://greedy-warbler-756.convex.cloud");

function App() {
  const [entries, setEntries] = useState([]);
  const [landmarks, setLandmarks] = useState([]);

  return (
    <div className="App">
      <ConvexProvider client={convex}>
        <ClerkProvider publishableKey="pk_test_YWN0aXZlLXJvdWdoeS04MS5jbGVyay5hY2NvdW50cy5kZXYk">
          <ConvexProviderWithClerk client={convex} useAuth={useAuth}>
            <Router>
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/routine" element={<Routine entries={entries} setEntries={setEntries} />} />
                <Route path="/canvas" element={<Yoga entries={entries} landmarks={landmarks} setLandmarks={setLandmarks}/>} />
              </Routes>
              <Navigation />
            </Router>
          </ConvexProviderWithClerk>
        </ClerkProvider>
      </ConvexProvider>
    </div>
  );
}

function Navigation() {
  const navigate = useNavigate();
  const [currentPage, setCurrentPage] = useState("/");

  const handleNextPage = () => {
    if (currentPage === "/") {
      setCurrentPage("/routine");
      navigate("/routine");
    } else if (currentPage === "/routine") {
      setCurrentPage("/canvas");
      navigate("/canvas");
    }
  };

  return (
    <div>
      {currentPage !== "/canvas" && (
        <button className="navigation-button" onClick={handleNextPage}>
        {currentPage === "/" ? "Go to Routine" : "Go to Yoga"}
      </button>
      )}
    </div>
  );
}

export default App;
