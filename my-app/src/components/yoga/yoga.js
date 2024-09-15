import "bootstrap/dist/css/bootstrap.min.css";
import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import Canvas from "../canvas/canvas.js";
import "../../yoga.css";

function Yoga({ entries }) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [countdown, setCountdown] = useState(
    entries.length > 0 ? entries[0].time : 0
  );

  useEffect(() => {
    const timer = setInterval(() => {
      setCountdown((prevCountdown) => prevCountdown - 1);
      if (countdown === 0 && currentIndex < entries.length - 1) {
        setCurrentIndex((prevIndex) => prevIndex + 1);
        setCountdown(entries[currentIndex + 1].time);
      } else if (countdown === 0 && currentIndex == entries.length - 1) {
        clearInterval(timer);
      }
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  });

  useEffect(() => {
    const updateGuessedPoseInterval = setInterval(() => {
      fetch(
        "http://localhost:5000/setPoseIndex/" +
          JSON.stringify(entries[currentIndex].position)
      )
        .then((response) => response.text())
        .then((data) => {
          console.log("user pose has been set: ", data);
        })
        .catch((error) => {
          console.error("Error sending data to backend:", error);
        });
    }, 5000);

    return () => {
      clearInterval(updateGuessedPoseInterval);
    };
  });

  return (
    <div className="container-fluid">
      <div className="frame">
        <Canvas />
      </div>
      <SidePanel
        entries={entries}
        countdown={countdown}
        currentIndex={currentIndex}
      />
      <NextPose entries={entries} />
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
            <h3 className="countdown-text">Time Remaining: {countdown} sec</h3>
          </>
        )}
      </div>
      <Button className="side-panel-button" variant="danger">
        Stop Routine
      </Button>
    </div>
  );
}

function NextPose({ entries }) {
  return (
    <div className="next-pose">
      <h2 className="next-pose-title">Pose Queue</h2>
      <ul className="pose-panel-list">
        {entries.map((entry, index) => (
          <li key={index} className="pose-panel-item">
            {entry.position}: {entry.time} sec
          </li>
        ))}
      </ul>
    </div>
  );
}
