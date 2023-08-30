import React, { useState, useEffect } from "react";
import ListingCard from "./ListingCard";

function ListingsContainer({ searchTerm }) {
  // const listing = {
  //   id: 1,
  //   description: "heater",
  //   image: "./images/heater.jpg",
  //   location: "BROOKLYN",
  // };
  // const { description, image, location } = listing;
  const [listings, setListings] = useState([]);

  const deleteListing = (id) => {
    fetch(`http://localhost:6001/listings/${id}`, {
      method: "DELETE",
    }).then(() => {
      setListings((listings) =>
        listings.filter((listing) => {
          return listing.id !== id;
        })
      );
    });
  };

  useEffect(() => {
    fetch("http://localhost:6001/listings")
      .then((r) => r.json())
      .then((listings) => setListings(listings));
  }, []);

  const searchedListings = listings.filter((listing) =>
    listing.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const listingLis = searchedListings.map(
    ({ id, description, image, location }) => {
      return (
        <ListingCard
          key={id}
          description={description}
          image={image}
          location={location}
          deleteListing={deleteListing}
          id={id}
        />
      );
    }
  );

  return (
    <main>
      <ul className="cards">{listingLis}</ul>
    </main>
  );
}

export default ListingsContainer;
