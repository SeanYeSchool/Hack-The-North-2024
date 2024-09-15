import "../../routine.css";
import React, { useState, useEffect } from "react";
import { DndProvider, useDrag, useDrop } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import Modal from "react-modal";

// Set up Modal root element
Modal.setAppElement("#root");

// Define styles for the modal
const customModalStyles = {
  content: {
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    transform: "translate(-50%, -50%)",
    width: "300px", // Adjust width for a smaller modal
    padding: "20px",
    borderRadius: "8px",
    overflow: "hidden", // Hide overflow to prevent scrollbars in modal
  },
};

// Function to lock or unlock body scroll
const toggleBodyScroll = (lock) => {
  if (lock) {
    document.body.style.overflowY = "hidden"; // Lock y-scroll only
  } else {
    document.body.style.overflowY = "auto"; // Unlock y-scroll
  }
  document.body.style.overflowX = "hidden"; // Always lock x-scroll
};

function Routine({ entries, setEntries }) {
  const [selectedPosition, setSelectedPosition] = useState("");
  const [time, setTime] = useState("5");
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editIndex, setEditIndex] = useState(null);
  const [editPosition, setEditPosition] = useState("");
  const [editTime, setEditTime] = useState("5");

  useEffect(() => {
    toggleBodyScroll(isModalOpen);
    return () => toggleBodyScroll(false); // Ensure scroll is unlocked when modal closes
  }, [isModalOpen]);

  useEffect(() => {
    // Extract positions and update backendEntries
    const positions = entries.map((entry) => entry.position);

    // Send data to the backend
  }, [entries]);

  const addEntry = () => {
    if (selectedPosition) {
      const newEntry = {
        position: selectedPosition,
        time: time,
      };

      setEntries([...entries, newEntry]);

      setSelectedPosition("");
      setTime("5");
    } else {
      alert("Please select a position");
    }
  };

  const deleteEntry = (indexToRemove) => {
    setEntries(entries.filter((_, index) => index !== indexToRemove));
  };

  const moveRow = (dragIndex, hoverIndex) => {
    const dragEntry = entries[dragIndex];
    const newEntries = [...entries];
    newEntries.splice(dragIndex, 1);
    newEntries.splice(hoverIndex, 0, dragEntry);
    setEntries(newEntries);
  };

  const openEditModal = (index) => {
    setEditIndex(index);
    setEditPosition(entries[index].position);
    setEditTime(entries[index].time);
    setIsModalOpen(true);
  };

  const closeEditModal = () => {
    setIsModalOpen(false);
    setEditIndex(null);
  };

  const saveEdit = () => {
    const updatedEntries = [...entries];
    updatedEntries[editIndex] = {
      position: editPosition,
      time: editTime,
    };
    setEntries(updatedEntries);
    closeEditModal();
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
                  <Slider time={time} setTime={setTime} />
                </td>
                <td>
                  <Button onClick={addEntry} />
                </td>
              </tr>
              {entries.map((entry, index) => (
                <DraggableRow
                  key={index}
                  index={index}
                  entry={entry}
                  moveRow={moveRow}
                  deleteEntry={() => deleteEntry(index)}
                  openEditModal={() => openEditModal(index)}
                />
              ))}
            </tbody>
          </table>
        </div>

        {/* Modal for editing */}
        <Modal
          isOpen={isModalOpen}
          onRequestClose={closeEditModal}
          contentLabel="Edit Entry"
          style={customModalStyles}
        >
          <h2>Edit Entry</h2>
          <label>
            Position:
            <Dropdown
              selectedPosition={editPosition}
              setSelectedPosition={setEditPosition}
              isModal={true}
            />
          </label>
          <br />
          <label>
            Time:
            <Slider time={editTime} setTime={setEditTime} isModal={true} />
          </label>
          <br />
          <button onClick={saveEdit}>Save</button>
          <button onClick={closeEditModal}>Cancel</button>
        </Modal>
      </div>
    </DndProvider>
  );
}

function DraggableRow({ entry, index, moveRow, deleteEntry, openEditModal }) {
  const [, ref] = useDrag({
    type: "ROW",
    item: { index },
  });

  const [, drop] = useDrop({
    accept: "ROW",
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
        <button className="edit-button" onClick={openEditModal}>
          Edit
        </button>
        <button className="del-button" onClick={deleteEntry}>
          -
        </button>
      </td>
    </tr>
  );
}

function Slider({ time, setTime, isModal }) {
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

function Dropdown({ selectedPosition, setSelectedPosition, isModal }) {
  const handleChange = (event) => {
    setSelectedPosition(event.target.value);
  };

  return (
    <div>
      <select value={selectedPosition} onChange={handleChange}>
        <option value="" disabled={isModal} className="hidden-option">
          Positions
        </option>
        <option value="Downward Dog">Downward Dog</option>
        <option value="Goddess">Goddess</option>
        <option value="Plank">Plank</option>
        <option value="Tree">Tree</option>
        <option value="Warrior 2">Warrior 2</option>
      </select>
    </div>
  );
}

function Button({ onClick }) {
  return <button onClick={onClick}>Add</button>;
}

export default Routine;
