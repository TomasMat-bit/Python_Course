// import logo from "./logo.svg";
// import "./App.css";

// function App() {
//   const name = "TOMAS";
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Tomas is Editing <code>src/App.js</code> and after saving lounching
//           it.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

//TASK 1

// import "./App.css";

// function App() {
//   const name = "TOMAS";
//   const age = 25;
//   const currentYear = new Date().getFullYear();

//   return (
//     <div className="App">
//       <header className="App-header">
//         <img
//           src="https://images.pexels.com/photos/2116475/pexels-photo-2116475.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
//           alt="logo"
//         />
//         <h1>
//           {name} is {age} years old
//         </h1>{" "}
//         {}
//         <p>
//           Current Year: {currentYear} {}
//         </p>
//         <button onClick={() => alert("Sveiki, Tomai!")}>Click Me</button> {}
//       </header>
//     </div>
//   );
// }

// export default App;

//TASK 2

import React from "react";
import "./App.css";

function App() {
  function Profilis({ vardas, pomegis }) {
    return (
      <div>
        <h2>{vardas}</h2>
        <p>Pomėgis: {pomegis}</p>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <Profilis vardas="Jonas" pomegis="Fotografija" />
        <Profilis vardas="Eva" pomegis="Knygų skaitymas" />
        <Profilis vardas="Tomas" pomegis="Sportas" />
      </header>
    </div>
  );
}

export default App;
