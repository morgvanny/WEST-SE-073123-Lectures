import DogSummary from "./DogSummary";
import { useState } from "react";

const PupsContainer = ({ pups, toggleDog }) => {
  const [id, setId] = useState();

  const pupSpans = pups.map(({ name, id }) => {
    return (
      <span
        onClick={() => {
          setId(id);
        }}
        key={id}
      >
        {name}
      </span>
    );
  });

  const pup = pups.find((pup) => pup.id === id);

  return (
    <>
      <div id="dog-bar">{pupSpans}</div>
      <DogSummary {...pup} toggleDog={toggleDog} />
    </>
  );
};

export default PupsContainer;
