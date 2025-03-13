import React from "react";

function Vartotojai({ vartotojai }) {
  return (
    <ul>
      {vartotojai.map((vartotojas) => (
        <li>
          {vartotojas.id}, {vartotojas.vardas}, {vartotojas.amzius}
        </li>
      ))}
    </ul>
  );
}

export default Vartotojai;
