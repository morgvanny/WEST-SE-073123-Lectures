import React, { useState, useEffect } from "react";

function PizzaForm({ pizza, updatePizza }) {
  const initialState = pizza || {
    topping: "",
    size: "",
    vegetarian: true,
    id: "",
  };

  const [formState, setFormState] = useState(initialState);

  const handleChange = (e) => {
    const key = e.target.name;
    const value = e.target.value;
    setFormState((formState) => ({ ...formState, [key]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    updatePizza(formState);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-row">
        <div className="col-5">
          <input
            value={formState.topping}
            onChange={handleChange}
            className="form-control"
            type="text"
            name="topping"
            placeholder="Pizza Topping"
          />
        </div>
        <div className="col">
          <select
            onChange={handleChange}
            value={formState.size}
            className="form-control"
            name="size"
          >
            <option value="Small">Small</option>
            <option value="Medium">Medium</option>
            <option value="Large">Large</option>
          </select>
        </div>
        <div className="col">
          <div className="form-check">
            <input
              checked={formState.vegetarian}
              className="form-check-input"
              type="radio"
              name="vegetarian"
              value="Vegetarian"
              onChange={(e) =>
                setFormState((formState) => ({
                  ...formState,
                  vegetarian: true,
                }))
              }
            />
            <label className="form-check-label">Vegetarian</label>
          </div>
          <div className="form-check">
            <input
              checked={!formState.vegetarian}
              className="form-check-input"
              type="radio"
              name="vegetarian"
              value="Not Vegetarian"
              onChange={(e) =>
                setFormState((formState) => ({
                  ...formState,
                  vegetarian: false,
                }))
              }
            />
            <label className="form-check-label">Not Vegetarian</label>
          </div>
        </div>
        <div className="col">
          <button type="submit" className="btn btn-success">
            Submit
          </button>
        </div>
      </div>
    </form>
  );
}

export default PizzaForm;
