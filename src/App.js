import React from "react";
import Profilis from "./Profilis";
import Pasisveikinimas from "./Pasisveikinimas";

function App() {
  const vardas = "Ona";
  const pavarde = "Onaite";
  const amzius = 25;
  let dabartiniaiMetai = new Date().getFullYear();

  return (
    <div>
      <h1>Sveiki atvyke i React!</h1>
      <img
        src="https://images.pexels.com/photos/2116475/pexels-photo-2116475.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        alt="Keliautojos nuotrauka"
        width="300"
      />
      <Pasisveikinimas vardas={vardas} pavarde={pavarde} />

      <p>
        Vardas: {vardas}, Amzius: {amzius}
      </p>
      <p>Dabartiniai metai: {dabartiniaiMetai}</p>

      <button onClick={() => alert("Paspaudei mygruka!")}>Spausti cia</button>
      <br />
      <a href="https://react.dev/" target="_blank" rel="noreferrer">
        React
      </a>

      <h3>Vartotoju profiliai</h3>
      <Profilis vardas="Jonas" pomegis="Krepsinis" />
      <Profilis vardas="Elge" pomegis="Fotografija" />
    </div>
  );
}

export default App;
