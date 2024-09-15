import * as pose from "@mediapipe/pose";
import smoothLandmarks from "mediapipe-pose-smooth"; // ES6
import * as cam from "@mediapipe/camera_utils";
import * as drawingUtils from "@mediapipe/drawing_utils";
import { useRef, useEffect, useState } from "react";

function Canvas() {
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);
  var camera = null;
  const [didLoad, setdidLoad] = useState(false);

  const [landmarks, setLandmarks] = useState([]);

  function onResults(results) {
    const canvasElement = canvasRef.current;
    const canvasCtx = canvasElement.getContext("2d");

    canvasCtx.save();
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    canvasCtx.drawImage(
      results.image,
      0,
      0,
      canvasElement.width,
      canvasElement.height
    );

    if (results.poseLandmarks) {
      drawingUtils.drawConnectors(
        canvasCtx,
        results.poseLandmarks,
        pose.POSE_CONNECTIONS,
        { visibilityMin: 0.65, color: "white" }
      );
      drawingUtils.drawLandmarks(
        canvasCtx,
        Object.values(pose.POSE_LANDMARKS_LEFT).map(
          (index) => results.poseLandmarks[index]
        ),
        { visibilityMin: 0.65, color: "white", fillColor: "blue" }
      );

      drawingUtils.drawLandmarks(
        canvasCtx,
        Object.values(pose.POSE_LANDMARKS_RIGHT).map(
          (index) => results.poseLandmarks[index]
        ),
        { visibilityMin: 0.65, color: "white", fillColor: "red" }
      );

      drawingUtils.drawLandmarks(
        canvasCtx,
        Object.values(pose.POSE_LANDMARKS_NEUTRAL).map(
          (index) => results.poseLandmarks[index]
        ),
        { visibilityMin: 0.65, color: "white", fillColor: "white" }
      );

      setLandmarks(results.poseLandmarks);
      fetch(
        "http://localhost:5000/setVectors/" +
          JSON.stringify(results.poseLandmarks)
      )
        .then((response) => response.text())
        .then((data) => {
          console.log("returned data: ", data);
        });
    }
    canvasCtx.restore();
  }

  useEffect(() => {
    if (!didLoad) {
      const mpPose = new pose.Pose({
        locateFile: (file) => {
          return `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`;
        },
      });
      mpPose.setOptions({
        selfieMode: true,
        modelComplexity: 1,
        smoothLandmarks: true,
        enableSegmentation: false,
        smoothSegmentation: true,
        minDetectionConfidence: 0.5,
        minTrackingConfidence: 0.5,
      });

      // eslint-disable-next-line react-hooks/exhaustive-deps
      camera = new cam.Camera(webcamRef.current, {
        onFrame: async () => {
          const canvasElement = canvasRef.current;
          const aspect = window.innerHeight / window.innerWidth;
          let width, height;
          if (window.innerWidth > window.innerHeight) {
            height = window.innerHeight;
            width = height / aspect;
          } else {
            width = window.innerWidth;
            height = width * aspect;
          }
          canvasElement.width = width;
          canvasElement.height = height;
          await mpPose.send({ image: webcamRef.current });
        },
      });
      camera.start();

      mpPose.onResults((results) => smoothLandmarks(results, onResults));
      setdidLoad(true);
    }
  }, [didLoad]);

  return (
    <>
      <video className="input_video" ref={webcamRef} />
      <canvas ref={canvasRef} className="output_canvas"></canvas>
    </>
  );
}

export default Canvas;
