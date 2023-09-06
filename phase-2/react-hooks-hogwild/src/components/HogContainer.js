import HogCard from "./HogCard";
import { useState } from "react";

function HogContainer({ hogs }) {
  const [isFilterOn, setIsFilterOn] = useState(false);
  const [sortType, setSortType] = useState("");
  console.log(sortType);
  const filteredHogs = isFilterOn
    ? hogs.filter((hog) => {
        return hog.greased;
      })
    : hogs;

  const sortedHogs = sortType
    ? [...filteredHogs].sort((a, b) => {
        if (sortType == "name") {
          return a.name.localeCompare(b.name);
        } else {
          if (a.weight > b.weight) {
            return -1;
          } else if (a.weight < b.weight) {
            return 1;
          } else {
            return 0;
          }
        }
      })
    : filteredHogs;

  const hogCards = sortedHogs.map((hog) => {
    return <HogCard key={hog.name} hog={hog} />;
  });

  return (
    <>
      <label>Show Only Greased: </label>
      <input
        type="checkbox"
        checked={isFilterOn}
        onChange={() => {
          setIsFilterOn((isFilterOn) => !isFilterOn);
        }}
      />
      <br />
      <select
        value={sortType}
        onChange={(e) => setSortType(e.target.value)}
        name="sortType"
      >
        <option value="">Unsorted</option>
        <option value="name">Sort By Name</option>
        <option value="weight">Sort By Weight</option>
      </select>
      <br />
      <br />
      <br />
      <div className="ui three stackable cards">{hogCards}</div>
    </>
  );
}

export default HogContainer;
