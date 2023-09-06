import { useState } from "react";
function HogCard({ hog }) {
  const [isShowingDetails, setIsShowingDetails] = useState(false);

  return (
    <div
      onClick={() => {
        setIsShowingDetails((isShowingDetails) => !isShowingDetails);
      }}
      key={hog.name}
      className={`ui card eight wide column pigTile ${
        isShowingDetails ? "maxPigTile" : "minPigTile"
      }`}
    >
      <div className="image">
        <img src={hog.image} />
      </div>
      <div className="content">
        <h3 className="header">{hog.name}</h3>
        {isShowingDetails ? (
          <>
            <p className="description">Specialty: {hog.specialty}</p>
            <p>Highest Medal Achieved: {hog["highest medal achieved"]}</p>
            <p>Weight: {hog.weight}</p>
            <p>Greased: {hog.greased + ""}</p>
          </>
        ) : null}
      </div>
    </div>
  );
}

export default HogCard;
