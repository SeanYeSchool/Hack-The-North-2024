import { Authenticated, Unauthenticated, useMutation } from "convex/react";
import { SignIn, SignedOut, SignInButton, UserButton } from '@clerk/clerk-react'


//Home imports these since api cannot be imported easily from home
//import { api } from "./convex/_generated/api.js";
import { api } from "../../convex/_generated/api.js";
import Stack from "react-bootstrap/Stack";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import image from "../../assets/yoga-person.png";

import "../../home.css";

export function Temp() {
  const updateUser = useMutation(api.users.updateUser, {});
  updateUser(); //Just going to update the user all the time
}

function Home() {
  return (
    <div>
      <h1 className="saman-font">Yoga Yogi</h1>
      <Unauthenticated>
        <div className="unauthenticated">
          <div className="image-container">
            <img src={image} alt="yoga yogi" className="unauthenticated-image" />
          </div>
          <div className="login-container">
            <SignIn />
          </div>
        </div>
      </Unauthenticated>
      <Authenticated>
        <UserButton />
        <Temp />
      </Authenticated>
    </div>
  );
}


export default Home;
