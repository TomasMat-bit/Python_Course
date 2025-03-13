import React, { useState } from "react";
import Skaitiklis from "./Skaitiklis";

function Sveikinimas() {
  const [tekstas, setTekstas] = useState("Sveiki");

  const keistiTeksta = () => {
    setTekstas("Labas, React!");
  };

  return (
    <div>
      <h1>{tekstas}</h1>
      <button onClick={keistiTeksta}>Keisti</button>
    </div>
  );
}

function App() {
  return (
    <div>
      <Sveikinimas />
      <Skaitiklis />
    </div>
  );
}

export default App;
