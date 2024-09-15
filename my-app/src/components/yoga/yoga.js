import "bootstrap/dist/css/bootstrap.min.css";
import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import Canvas from "../canvas/canvas.js";
import "../../yoga.css";
import TextToSpeech from './tts.js';


function Yoga({ entries }) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [countdown, setCountdown] = useState(
    entries.length > 0 ? entries[0].time : 0
  );
  const [poseUpdateCounter, setPoseUpdateCounter] = useState(5); // For pose update interval
  const [messages, setMessage] = useState([]);
  const [landmarks, setLandmarks] = useState([]);
 
  useEffect(() => {
    const timer = setInterval(() => {
      setCountdown((prevCountdown) => {
        if (prevCountdown === 0) {
          if (currentIndex < entries.length - 1) {
            // Move to the next position and reset countdown
            setCurrentIndex((prevIndex) => prevIndex + 1);
            setPoseUpdateCounter(5); // Reset pose update interval
            return entries[currentIndex + 1].time; // Set countdown for the next position
          } else {
            // Stop the timer if the last position is finished
            clearInterval(timer);
            return 0; // Ensure countdown doesn't go negative
          }
        } else {
          return prevCountdown - 1; // Decrease countdown by 1 second
        }
      });

      setPoseUpdateCounter((prevCounter) => {
        if (prevCounter === 1) {
          sendPoseUpdate();
          getFeedbackMessage(landmarks);
          verifyPose(landmarks);
          return 5; // Reset counter to send the next pose update in 5 seconds
        } else {
          return prevCounter - 1; // Decrease pose update counter by 1 second
        }
      });
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  }, [currentIndex, entries, landmarks]);

  const getFeedbackMessage = (landmarks) => {
    console.log("Sending pose update");
    fetch(
      "http://localhost:5000/getComment/10.0/" +
        JSON.stringify(landmarks)
    )
      .then((response) => response.text())
      .then((data) => {
        setMessage(prevItems => [...prevItems, data]);
        console.log("Feedback message: ", data);
      })
      .catch((error) => {
        console.error("Feedback message error:", error);
      });
  };

  const sendPoseUpdate = () => {
    console.log("Sending pose update");
    fetch(
      "http://localhost:5000/setPoseIndex/" +
        JSON.stringify(entries[currentIndex].position)
    )
      .then((response) => response.text())
      .then((data) => {
        console.log("User pose has been set: ", data);
      })
      .catch((error) => {
        console.error("Error sending data to backend:", error);
      });
  };

  const verifyPose = (landmarks) => {
    fetch("http://localhost:5000/verifyPose/" + JSON.stringify(landmarks))
      .then((response) => response.text())
      .then((data) => {
        console.log("pose verified as: ", data);
      });
  };

  return (
    <div className="container-fluid">
      <div className="frame">
        <Canvas setLandmarks={setLandmarks} />
      </div>
      <SidePanel
        entries={entries}
        countdown={countdown}
        currentIndex={currentIndex}
      />
      <FeedbackMessage entries={entries} messages={messages} currentIndex={currentIndex}/>
    </div>
  );
}

export default Yoga;

function SidePanel({ entries, currentIndex, countdown }) {
  return (
    <div className="side-panel">
      <div className="info-panel">
        {entries.length > 0 && (
          <>
            <h2 className="position-text">
              Current Position: {entries[currentIndex].position}
            </h2>
            <div> {currentIndex < entries.length - 1 && 'Next Position: ' + entries[currentIndex+1].position}</div>
            <h3 className="countdown-text">Time Remaining: {countdown} sec</h3>
          </>
        )}
      </div>
      <Button className="side-panel-button" variant="danger">
        <a href="/">Stop Routine and Return Home</a>
      </Button>
    </div>
  );
}

function FeedbackMessage({ entries, messages, currentIndex }) {
  return (
    <div className="next-pose">
      <h2 className="next-pose-title">Pose Queue</h2>
      <ul className="pose-panel-list">
        {messages.map((msg, index) => (
          <>
            <li key={index} className="pose-panel-item">
              {msg}
            </li><TextToSpeech text={msg} />
          </>
        ))}
      </ul>
    </div>
  );
}
