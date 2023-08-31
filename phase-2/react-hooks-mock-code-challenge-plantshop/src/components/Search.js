import React from "react";

function Search({ searchInput, setSearchInput }) {
  return (
    <div className="searchbar">
      <label htmlFor="search">Search Plants:</label>
      <input
        value={searchInput}
        type="text"
        id="search"
        placeholder="Type a name to search..."
        onChange={(e) => setSearchInput(e.target.value)}
      />
    </div>
  );
}

export default Search;
