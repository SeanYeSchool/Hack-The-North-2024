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
    if (entries.length > 0 && countdown > 0) {
      const timer = setInterval(() => {
        setCountdown((prevCountdown) => prevCountdown - 1);
      }, 1000);

      return () => clearInterval(timer);
    } else if (countdown === 0 && currentIndex < entries.length - 1) {
      // Move to the next entry
      setCurrentIndex((prevIndex) => prevIndex + 1);
      fetch(
        "http://localhost:5000/setPoseIndex/" +
          JSON.stringify(entries[currentIndex])
      )
        .then((response) => response.text())
        .then((data) => {
          console.log("output: ", data);
        })
        .catch((error) => {
          console.error("Error sending data to backend:", error);
        });
      setCountdown(entries[currentIndex + 1].time);
    }
  }, [countdown, currentIndex, entries]);

  return (
    <div className="container-fluid">
      <div className="frame">
        <Canvas />
      </div>
      <div>
        {entries.length > 0 && (
          <>
            <h2>Current Position: {entries[currentIndex].position}</h2>
            <h3>Time Remaining: {countdown} sec</h3>
          </>
        )}
      </div>
      <SidePanel entries={entries} />
    </div>
  );
}

export default Yoga;

function SidePanel({ entries }) {
    return (
      <div className="container-fluid">
        <Button>Stop Routine</Button>
        <div>
          {entries.map((entry, index) => (
            <div key={index}>
              {entry.position}: {entry.time} sec
            </div>
          ))}
        </div>
      </div>
    );
  }