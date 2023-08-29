import Stock from "./Stock";

function StockContainer({ stocks, addToPortfolio }) {
  const stockDivs = stocks.map(({ ticker, name, price, id }) => {
    return (
      <Stock
        key={id}
        ticker={ticker}
        name={name}
        price={price}
        handleOnClick={addToPortfolio}
        id={id}
      />
    );
  });

  return (
    <div>
      <h2>Stocks</h2>
      {stockDivs}
    </div>
  );
}

export default StockContainer;
