import React from "react";
import Pizza from "./Pizza";

function PizzaList({ pizzas, setPizzaIdEdit }) {
  const pizzaRows = pizzas.map((pizza) => {
    const { id, topping, size, vegetarian } = pizza;
    return (
      <Pizza
        key={id}
        id={id}
        topping={topping}
        size={size}
        vegetarian={vegetarian}
        setPizzaIdEdit={setPizzaIdEdit}
      />
    );
  });

  return (
    <table className="table table-striped">
      <thead>
        <tr>
          <th scope="col">Topping</th>
          <th scope="col">Size</th>
          <th scope="col">Vegetarian?</th>
          <th scope="col">Edit</th>
        </tr>
      </thead>
      <tbody>{pizzaRows}</tbody>
    </table>
  );
}

export default PizzaList;
