import React, { useState, useEffect } from "react";
import PupsContainer from "./PupsContainer";

function App() {
  const [isFilterOn, setIsFilterOn] = useState(false);
  const [pups, setPups] = useState([]);

  useEffect(() => {
    fetch("http://localhost:3001/pups")
      .then((r) => r.json())
      .then((pups) => {
        setPups(pups);
      });
  }, []);

  const toggleDog = (id) => {
    const pup = pups.find((pup) => pup.id === id);

    fetch(`http://localhost:3001/pups/${id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ isGoodDog: !pup.isGoodDog }),
    })
      .then((r) => r.json())
      .then((updatedPup) => {
        setPups((pups) => {
          return pups.map((p) => {
            if (p.id === updatedPup.id) {
              return updatedPup;
            } else {
              return p;
            }
          });
        });
      });
  };

  const toggleFilter = () => {
    setIsFilterOn((isFilterOn) => !isFilterOn);
  };

  const filteredPups = isFilterOn ? pups.filter((pup) => pup.isGoodDog) : pups;

  return (
    <div className="App">
      <div id="filter-div">
        <button onClick={toggleFilter} id="good-dog-filter">
          Filter good dogs: {isFilterOn ? "ON" : "OFF"}
        </button>
      </div>
      <PupsContainer pups={filteredPups} toggleDog={toggleDog} />
    </div>
  );
}

export default App;
