import React, { useEffect } from "react";
import PokemonCard from "./PokemonCard";
import { Card } from "semantic-ui-react";

function PokemonCollection({ pokemons, setPokemons }) {
  useEffect(() => {
    fetch("http://localhost:3001/pokemon")
      .then((r) => r.json())
      .then((data) => {
        setPokemons(data);
      });
  }, []);

  const pokemonCards = pokemons.map((pokemon) => (
    <PokemonCard
      key={pokemon.id}
      name={pokemon.name}
      hp={pokemon.hp}
      sprites={pokemon.sprites}
    />
  ));

  return <Card.Group itemsPerRow={6}>{pokemonCards}</Card.Group>;
}

export default PokemonCollection;
