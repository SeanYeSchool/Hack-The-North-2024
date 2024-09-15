import { Authenticated, Unauthenticated, useMutation } from "convex/react";
import { SignIn, UserButton } from "@clerk/clerk-react";
import StartButton from "../button/StartButton.js";

import { api } from "../../convex/_generated/api.js";

function Temp() {
  const updateUser = useMutation(api.users.updateUser, {});
  updateUser(); //Just going to update the user all the time
}

function Home() {
  return (
    <div>
      Home page
      {/* <Unauthenticated>
        <SignIn></SignIn>
      </Unauthenticated> */}
      <StartButton />
      <Authenticated>
        <UserButton></UserButton>
        <Temp></Temp>
      </Authenticated>
    </div>
  );
}

export default Home;
