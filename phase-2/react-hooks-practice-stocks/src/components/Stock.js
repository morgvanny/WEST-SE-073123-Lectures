import React from "react";

function Stock({ name, ticker, price, id, handleOnClick }) {
  return (
    <div
      onClick={() => {
        handleOnClick(id);
      }}
    >
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">{name}</h5>
          <p className="card-text">
            {ticker}: {price}
          </p>
        </div>
      </div>
    </div>
  );
}
export default Stock;
