import React, { useState } from "react";

export default function Skaitiklis() {
  const [skaicius, setSkaicius] = useState(0);

  const padidinti = () => setSkaicius(skaicius + 1);
  const sumazinti = () => {
    if (skaicius > 0) setSkaicius(skaicius - 1);
  };

  return (
    <div>
      <h2>Skaicius: {skaicius}</h2>
      <button onClick={padidinti}>+1</button>
      <button onClick={sumazinti}>-1</button>
    </div>
  );
}
