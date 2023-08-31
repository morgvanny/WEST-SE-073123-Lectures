import React, { useState, useEffect } from "react";
import NewPlantForm from "./NewPlantForm";
import PlantList from "./PlantList";
import Search from "./Search";

function PlantPage() {
  const [plants, setPlants] = useState([]);
  const [searchInput, setSearchInput] = useState("");

  const addPlant = (plant) => {
    fetch("http://localhost:6001/plants", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(plant),
    })
      .then((r) => r.json())
      .then((plant) => {
        setPlants((plants) => [...plants, plant]);
      });
  };

  useEffect(() => {
    fetch("http://localhost:6001/plants")
      .then((r) => r.json())
      .then((plants) => setPlants(plants));
  }, []);

  const filteredPlants = searchInput
    ? plants.filter((plant) => {
        return plant.name.toLowerCase().includes(searchInput.toLowerCase());
      })
    : plants;

  return (
    <main>
      <NewPlantForm addPlant={addPlant} />
      <Search searchInput={searchInput} setSearchInput={setSearchInput} />
      <PlantList plants={filteredPlants} />
    </main>
  );
}

export default PlantPage;
