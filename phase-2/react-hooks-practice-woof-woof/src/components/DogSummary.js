function DogSummary({ image, name, id, isGoodDog, toggleDog }) {
  if (!id) return null;
  return (
    <div id="dog-summary-container">
      <h1>DOGGO:</h1>
      <div id="dog-info">
        <img src={image} alt={name} />
        <h2>{name}</h2>
        <button
          onClick={() => {
            toggleDog(id);
          }}
        >
          {isGoodDog ? "Good" : "Bad"} Dog!
        </button>
      </div>
    </div>
  );
}

export default DogSummary;
