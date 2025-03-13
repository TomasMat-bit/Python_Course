import React from "react";
import Vartotojai from "./Vartotojai";

function App() {
  const duomenys = [
    { id: 1, vardas: "Jonas", amzius: 25 },
    { id: 2, vardas: "Laura", amzius: 30 },
    { id: 3, vardas: "Darius", amzius: 20 },
    { id: 4, vardas: "Ona", amzius: 40 },
    { id: 5, vardas: "Petras", amzius: 50 },
  ];

  return (
    <div>
      <Vartotojai vartotojai={duomenys} />
    </div>
  );
}

export default App;
