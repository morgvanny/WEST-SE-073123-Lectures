import React, { useState, useEffect } from "react";
import Header from "./Header";
import PizzaForm from "./PizzaForm";
import PizzaList from "./PizzaList";

function App() {
  const [pizzas, setPizzas] = useState([]);
  const [pizzaIdEdit, setPizzaIdEdit] = useState();

  const updatePizza = (pizzaData) => {
    fetch(`http://localhost:3001/pizzas/${pizzaData.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(pizzaData),
    })
      .then((r) => r.json())
      .then((updatedPizza) => {
        setPizzas((pizzas) =>
          pizzas.map((pizza) => {
            if (pizza.id === updatedPizza.id) {
              return updatedPizza;
            } else {
              return pizza;
            }
          })
        );
        setPizzaIdEdit();
      });
  };

  const pizzaToEdit = pizzas.find((pizza) => pizza.id === pizzaIdEdit);

  useEffect(() => {
    fetch("http://localhost:3001/pizzas")
      .then((r) => r.json())
      .then(setPizzas);
  }, []);
  return (
    <>
      <Header />
      <PizzaForm
        key={pizzaIdEdit}
        pizza={pizzaToEdit}
        updatePizza={updatePizza}
      />
      <PizzaList pizzas={pizzas} setPizzaIdEdit={setPizzaIdEdit} />
    </>
  );
}

export default App;
