import React, { useState } from "react";

function Registracija() {
  const [vardas, setVardas] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (vardas) {
      alert(`Įvestas vardas: ${vardas}`);
    } else {
      alert("Prašome įvesti vardą!");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Vardas:
        <input
          type="text"
          value={vardas}
          onChange={(e) => setVardas(e.target.value)}
        />
      </label>
      <button type="submit">Pateikti</button>
    </form>
  );
}

function App() {
  return <Registracija />;
}

export default App;
