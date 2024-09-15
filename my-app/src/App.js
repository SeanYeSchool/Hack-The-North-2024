import "./App.css";

import Yoga from "./components/yoga/yoga.js";
import Routine from "./components/routine/routine.js";
import Home from "./components/home/home.js";

import { BrowserRouter as Router, Routes, Route, Link, useLocation } from "react-router-dom";
import { useState } from "react";

import { ConvexProvider, ConvexReactClient } from "convex/react";
import { ClerkProvider, useAuth } from "@clerk/clerk-react";
import { ConvexProviderWithClerk } from "convex/react-clerk";

const convex = new ConvexReactClient("https://greedy-warbler-756.convex.cloud");

function App() {
  const [entries, setEntries] = useState([]);

  return (
    <div className="App">
      <ConvexProvider client={convex}>
        <ClerkProvider publishableKey="pk_test_YWN0aXZlLXJvdWdoeS04MS5jbGVyay5hY2NvdW50cy5kZXYk">
          <ConvexProviderWithClerk client={convex} useAuth={useAuth}>
            <Router>
              <Navigation />
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/routine" element={<Routine entries={entries} setEntries={setEntries} />} />
                <Route path="/canvas" element={<Yoga entries={entries} />} />
              </Routes>
            </Router>
          </ConvexProviderWithClerk>
        </ClerkProvider>
      </ConvexProvider>
    </div>
  );
}

function Navigation() {
  const location = useLocation();
  const showLinks = location.pathname === '/' || location.pathname === '/routine';

  return (
    <>
      {showLinks && (
        <div>
          <Link to="/">To Home</Link> <br />
          <Link to="/routine">To Routine</Link> <br />
          <Link to="/canvas">To Yoga</Link>
        </div>
      )}
    </>
  );
}

export default App;
