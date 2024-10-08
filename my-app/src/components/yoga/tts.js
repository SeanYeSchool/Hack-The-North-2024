import React, { useState, useEffect } from "react";

const TextToSpeech = ({ text }) => {
  const [isPaused, setIsPaused] = useState(false);
  const [utterance, setUtterance] = useState(null);
  const [voice, setVoice] = useState(null);

  useEffect(() => {
    const synth = window.speechSynthesis;

    const u = new SpeechSynthesisUtterance(text);
    u.voice = voice; // Set the selected voice
    setUtterance(u);

    return () => {
      synth.cancel();
    };
  }, [text, voice]);

  useEffect(() => {
    if (utterance) {
      handlePlay(); // Automatically play when utterance is updated
    }
  }, [utterance]);

  const handlePlay = () => {
    const synth = window.speechSynthesis;

    if (isPaused) {
      synth.resume();
    } else {
      if (utterance) {
        synth.speak(utterance);
      }
    }

    setIsPaused(false);
  };


//   const handlePlay = () => {
//     const synth = window.speechSynthesis;

//     if (isPaused) {
//     synth.resume();
//     }

//     synth.speak(utterance);

//     setIsPaused(false);
//   };
  
  const handlePause = () => {
    const synth = window.speechSynthesis;

    synth.pause();

    setIsPaused(true);
  };

  const handleStop = () => {
    const synth = window.speechSynthesis;

    synth.cancel();

    setIsPaused(false);
  };

  const handleVoiceChange = (event) => {
    const voices = window.speechSynthesis.getVoices();
    setVoice(voices.find((v) => v.name === event.target.value));
  };

//   return (
//     // <><div>
//     //       <label>
//     //           Voice:
//     //           <select value={voice?.name} onChange={handleVoiceChange}>
//     //               {window.speechSynthesis.getVoices().map((voice) => (
//     //                   <option key={voice.name} value={voice.name}>
//     //                       {voice.name}
//     //                   </option>
//     //               ))}
//     //           </select>
//     //       </label>
//     //   </div><br /><div>
//     //         <button onClick={handlePause}>Pause</button>
//     //         <button onClick={handlePlay}>Start</button>
//     //         <button>Hello</button>
//     //         {handlePlay}
//     //           {/* <div className="handlePlay"></div>
//     //           <button onClick={handleStop}>Stop</button> */}
//     //       </div></>
//   );
};

export default TextToSpeech;