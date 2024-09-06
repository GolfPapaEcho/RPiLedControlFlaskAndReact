import React, { useState, useEffect } from 'react';

function App() {
  const [ledStatus, setLedStatus] = useState(false);  // This defines setLedStatus


const API_URL = 'http://192.168.1.2:5000';  // Replace with your backend IP

useEffect(() => {
  fetch(`${API_URL}/led`)
    .then((response) => response.json())
    .then((data) => setLedStatus(data.status));
}, []);

const handleTurnOn = () => {
  fetch(`${API_URL}/led/on`, { method: 'POST' })
    .then((response) => response.json())
    .then((data) => setLedStatus(data.status));
};

const handleTurnOff = () => {
  fetch(`${API_URL}/led/off`, { method: 'POST' })
    .then((response) => response.json())
    .then((data) => setLedStatus(data.status));
};

const handleToggle = () => {
  fetch(`${API_URL}/led/toggle`, { method: 'POST' })
    .then((response) => response.json())
    .then((data) => setLedStatus(data.status));
};

  return (
    <div className="App">
      <h1>LED Control</h1>
      <p>LED is currently: {ledStatus ? 'On' : 'Off'}</p>
      <button onClick={handleTurnOn}>Turn On</button>
      <button onClick={handleTurnOff}>Turn Off</button>
      <button onClick={handleToggle}>Toggle</button>
    </div>
  );
}

export default App;
