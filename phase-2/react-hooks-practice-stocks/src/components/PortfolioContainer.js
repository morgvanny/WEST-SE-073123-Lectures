import React from "react";
import Stock from "./Stock";

function PortfolioContainer({ stocks, removeFromPortfolio }) {
  const stockDivs = stocks.map(({ ticker, name, price, id }) => {
    return (
      <Stock
        key={id}
        ticker={ticker}
        name={name}
        price={price}
        id={id}
        handleOnClick={removeFromPortfolio}
      />
    );
  });
  return (
    <div>
      <h2>My Portfolio</h2>
      {stockDivs}
    </div>
  );
}

export default PortfolioContainer;
