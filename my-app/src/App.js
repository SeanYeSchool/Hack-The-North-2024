import "./App.css";

import Yoga from "./components/yoga/yoga.js";
import Routine from "./components/routine/routine.js";
import Home from "./components/home/home.js"
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import { ConvexProvider, ConvexReactClient } from "convex/react";
import { ConvexProvider, ConvexReactClient, Authenticated, Unauthenticated, useQuery, useMutation } from "convex/react";
import { ClerkProvider, useAuth, SignIn, UserButton } from "@clerk/clerk-react";
import { ConvexProviderWithClerk } from "convex/react-clerk";

import { api } from "./convex/_generated/api.js";

const convex = new ConvexReactClient("https://greedy-warbler-756.convex.cloud");

function Temp(){
  const updateUser = useMutation(api.users.updateUser, {});
  updateUser(); //Just going to update the user all the time
}

function App() {
  

  return (
    <div className="App">
      <ConvexProvider client={convex}>
      <ClerkProvider publishableKey="pk_test_YWN0aXZlLXJvdWdoeS04MS5jbGVyay5hY2NvdW50cy5kZXYk">
      <ConvexProviderWithClerk client={convex} useAuth={useAuth}>
      <Router>
        <div>
<<<<<<< Updated upstream
          <Link to="/routine">Landing page =\ Routine</Link> <br />
          <Link to="/canvas">Routine =\ Yoga</Link>
=======
        <Unauthenticated>
          <SignIn></SignIn>
        </Unauthenticated>
        <Authenticated>
          <UserButton></UserButton>
          <Temp></Temp>
        </Authenticated>
        <Link to="/routine">Go to routine</Link>
>>>>>>> Stashed changes
          <Routes>
            <Route path="/" element = {<Home />} />
            <Route path="/routine" element={<Routine />} />
            <Route path="/canvas" element={<Yoga />} /> {/* Change the name of the Home component to Canvas */}
          </Routes>
        </div>
      </Router>
      </ConvexProvider>
      </ConvexProviderWithClerk>
      </ClerkProvider>
    </div>
  );
}

export default App;
