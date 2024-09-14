import "../../routine.css";
import React, { useState } from 'react';

function Routine() {
    const [entries, setEntries] = useState([]);

    const [selectedPosition, setSelectedPosition] = useState('');
    const [time, setTime] = useState(5);

    const addEntry = () => {
        if (selectedPosition) {
            const newEntry = {
                position: selectedPosition,
                time: time
            };

            setEntries([...entries, newEntry]);

            setSelectedPosition('');
            setTime(5);
        } else {
            alert("Please select a position");
        }
    };

    return (
        <div className="main">
            <h1>Routine Tracker</h1>

            <div className="table">
                <table>
                    <thead>
                        <tr className="headers">
                            <th>#</th>
                            <th> Position </th>
                            <th> Time </th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr className="add">
                            <td></td>
                            <td> 
                                <Dropdown 
                                    selectedPosition={selectedPosition} 
                                    setSelectedPosition={setSelectedPosition} 
                                /> 
                            </td>
                            <td> 
                                <Slider 
                                    time={time} 
                                    setTime={setTime} 
                                /> 
                            </td>
                            <td>
                                <Button onClick={addEntry} />
                            </td>
                        </tr>
                        {/* Render the entries */}
                        {entries.map((entry, index) => (
                            <tr key={index}>
                                <td>{index+1}</td>
                                <td>{entry.position}</td>
                                <td>{entry.time} sec</td>
                                <td></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Routine;

function Slider({ time, setTime }) {
    const handleChange = (event) => {
        setTime(event.target.value);
    };

    return (
        <div>
            <input
                type="range"
                min="5"
                max="120"
                step="5"
                value={time}
                onChange={handleChange}
            />
            <p>{time} seconds</p>
        </div>
    );
}

function Dropdown({ selectedPosition, setSelectedPosition }) {
    const handleChange = (event) => {
        setSelectedPosition(event.target.value);
    };

    return (
        <div>
            <select value={selectedPosition} onChange={handleChange}>
                <option value="" disabled className="hidden-option">Positions</option>
                <option value="Doggy 1">Doggy 1</option>
                <option value="Doggy 2">Doggy 2</option>
                <option value="Doggy 3">Doggy 3</option>
                <option value="Doggy 4">Doggy 4</option>
            </select>
        </div>
    );
}

function Button({ onClick }) {
    return (
        <button onClick={onClick}>
            Add
        </button>
    );
}
