import React, { useState, useEffect } from "react";
import PokemonCollection from "./PokemonCollection";
import PokemonForm from "./PokemonForm";
import Search from "./Search";
import { Container } from "semantic-ui-react";

function PokemonPage() {
  const [pokemons, setPokemons] = useState([]);
  const [searchInput, setSearchInput] = useState("");

  const searchedPokemons = pokemons.filter((pokemon) => {
    return pokemon.name.toLowerCase().includes(searchInput.toLowerCase());
  });

  const submitPokemon = (pokemon) => {
    fetch("http://localhost:3001/pokemon", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(pokemon),
    })
      .then((r) => r.json())
      .then((newPokemon) => {
        setPokemons((pokemons) => [...pokemons, newPokemon]);
      });
  };

  return (
    <Container>
      <h1>Pokemon Searcher</h1>
      <br />
      <PokemonForm submitPokemon={submitPokemon} />
      <br />
      <Search searchInput={searchInput} setSearchInput={setSearchInput} />
      <br />
      <PokemonCollection
        pokemons={searchedPokemons}
        setPokemons={setPokemons}
      />
    </Container>
  );
}

export default PokemonPage;
