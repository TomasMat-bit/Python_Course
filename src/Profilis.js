import React from "react";

function Profilis(props) {
    return (
      <div>
        <h2>Profilis</h2>
        <p>{props.vardas}</p>
        <p>{props.pomegis}</p>
      </div>
    );
}

export default Profilis;

