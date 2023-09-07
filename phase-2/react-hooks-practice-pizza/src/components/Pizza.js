import React from "react";

function Pizza({ id, topping, size, vegetarian, setPizzaIdEdit }) {
  return (
    <tr>
      <td>{topping}</td>
      <td>{size}</td>
      <td>{vegetarian.toString()}</td>
      <td>
        <button
          onClick={() => setPizzaIdEdit(id)}
          type="button"
          className="btn btn-primary"
        >
          Edit Pizza
        </button>
      </td>
    </tr>
  );
}

export default Pizza;
