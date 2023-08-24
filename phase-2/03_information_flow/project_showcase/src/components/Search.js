const Search = ({ searchQuery, setSearchQuery, setPhase }) => {
  const handleOnChange = (e) => setSearchQuery(e.target.value);

  return (
    <>
      <div className="filter">
        <button onClick={() => setPhase("All")}>All</button>
        <button onClick={() => setPhase("5")}>Phase 5</button>
        <button onClick={() => setPhase("4")}>Phase 4</button>
        <button onClick={() => setPhase("3")}>Phase 3</button>
        <button onClick={() => setPhase("2")}>Phase 2</button>
        <button onClick={() => setPhase("1")}>Phase 1</button>
      </div>
      <input
        value={searchQuery}
        type="text"
        placeholder="Search..."
        onChange={handleOnChange}
      />
    </>
  );
};

export default Search;
