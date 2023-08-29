import React from "react";

function SearchBar({ filterType, setFilterType, sortType, setSortType }) {
  const handleChange = (e) => {
    setSortType(e.target.value);
  };

  return (
    <div>
      <strong>Sort by:</strong>
      <label>
        <input
          type="radio"
          value="Alphabetically"
          name="sort"
          checked={sortType === "Alphabetically"}
          onChange={handleChange}
        />
        Alphabetically
      </label>
      <label>
        <input
          type="radio"
          value="Price"
          name="sort"
          checked={sortType === "Price"}
          onChange={handleChange}
        />
        Price
      </label>
      <br />
      <label>
        <strong>Filter:</strong>
        <select
          value={filterType}
          onChange={(e) => setFilterType(e.target.value)}
        >
          <option value="">Select your option</option>
          <option value="Tech">Tech</option>
          <option value="Sportswear">Sportswear</option>
          <option value="Finance">Finance</option>
        </select>
      </label>
    </div>
  );
}

export default SearchBar;
