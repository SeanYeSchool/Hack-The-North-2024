import "../../routine.css";
import React, { useState } from 'react';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';

function Routine() {
    const [entries, setEntries] = useState([]);

    const [selectedPosition, setSelectedPosition] = useState('');
    const [time, setTime] = useState("5");

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

    // Delete entry handler
    const deleteEntry = (indexToRemove) => {
        setEntries(entries.filter((_, index) => index !== indexToRemove));
    };

    // Drag and Drop Logic
    const moveRow = (dragIndex, hoverIndex) => {
        const dragEntry = entries[dragIndex];
        const newEntries = [...entries];
        newEntries.splice(dragIndex, 1);
        newEntries.splice(hoverIndex, 0, dragEntry);
        setEntries(newEntries);
    };

    return (
        <DndProvider backend={HTML5Backend}>
            <div className="main">
                <h1>Routine Tracker</h1>

                <div className="table">
                    <table>
                        <thead>
                            <tr className="headers">
                                <th className="row-counter">#</th>
                                <th>Position</th>
                                <th>Time</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr className="add-row">
                                <td className="row-counter"></td>
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
                                <DraggableRow
                                    key={index}
                                    index={index}
                                    entry={entry}
                                    moveRow={moveRow}
                                    deleteEntry={() => deleteEntry(index)}
                                />
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </DndProvider>
    );
}

function DraggableRow({ entry, index, moveRow, deleteEntry }) {
    const [, ref] = useDrag({
        type: 'ROW',
        item: { index },
    });

    const [, drop] = useDrop({
        accept: 'ROW',
        hover: (item) => {
            if (item.index !== index) {
                moveRow(item.index, index);
                item.index = index;
            }
        },
    });

    return (
        <tr ref={(node) => ref(drop(node))}>
            <td className="row-counter">{index + 1}</td>
            <td>{entry.position}</td>
            <td>{entry.time} sec</td>
            <td>
                <button className='del-button' onClick={deleteEntry}>-</button>
            </td>
        </tr>
    );
}

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

export default Routine;