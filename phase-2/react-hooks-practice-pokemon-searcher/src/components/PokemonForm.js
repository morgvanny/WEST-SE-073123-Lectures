import React, { useState } from "react";
import { Form } from "semantic-ui-react";

function PokemonForm({ submitPokemon }) {
  const initialState = {
    name: "",
    hp: "",
    frontUrl: "",
    backUrl: "",
  };
  const [formState, setFormState] = useState(initialState);
  const { name, hp, frontUrl, backUrl } = formState;

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormState((formState) => {
      return { ...formState, [name]: value };
    });
  };

  return (
    <div>
      <h3>Add a Pokemon!</h3>
      <Form
        onSubmit={(e) => {
          e.preventDefault();
          submitPokemon({
            name,
            hp,
            sprites: {
              front: frontUrl,
              back: backUrl,
            },
          });
          setFormState(initialState);
        }}
      >
        <Form.Group widths="equal">
          <Form.Input
            value={name}
            fluid
            label="Name"
            placeholder="Name"
            name="name"
            onChange={handleChange}
          />
          <Form.Input
            value={hp}
            fluid
            label="hp"
            placeholder="hp"
            name="hp"
            onChange={handleChange}
          />
          <Form.Input
            fluid
            value={frontUrl}
            label="Front Image URL"
            placeholder="url"
            name="frontUrl"
            onChange={handleChange}
          />
          <Form.Input
            fluid
            value={backUrl}
            label="Back Image URL"
            placeholder="url"
            name="backUrl"
            onChange={handleChange}
          />
        </Form.Group>
        <Form.Button>Submit</Form.Button>
      </Form>
    </div>
  );
}

export default PokemonForm;
