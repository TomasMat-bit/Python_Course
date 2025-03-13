import React, { useState } from "react";

function Skaiciuokle() {
  const [skaicius, setSkaicius] = useState(0);

  return (
    <div>
      <h1>{skaicius}</h1>
      <button onClick={() => setSkaicius(skaicius + 1)}>Padidinti</button>
      <button onClick={() => setSkaicius(skaicius - 1)}>Sumazinti</button>
    </div>
  );
}

export default Skaiciuokle;
