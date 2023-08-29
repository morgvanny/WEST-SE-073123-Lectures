import React, { useState, useEffect } from "react";
import StockContainer from "./StockContainer";
import PortfolioContainer from "./PortfolioContainer";
import SearchBar from "./SearchBar";

function MainContainer() {
  const [stocks, setStocks] = useState([]);
  const [portfolioIds, setPortfolioIds] = useState([]);

  const [filterType, setFilterType] = useState("");
  const [sortType, setSortType] = useState("");

  useEffect(() => {
    fetch("http://localhost:3001/stocks")
      .then((r) => r.json())
      .then((data) => {
        setStocks(data);
      });
  }, []);

  const addToPortfolio = (id) => {
    if (!portfolioIds.includes(id)) {
      setPortfolioIds((ids) => [...ids, id]);
    }
  };
  const removeFromPortfolio = (id) => {
    setPortfolioIds((ids) => ids.filter((portfolioId) => portfolioId !== id));
  };

  const portfolioStocks = portfolioIds.map((id) => {
    return stocks.find((stock) => stock.id === id);
  });

  const filteredStocks = filterType
    ? stocks.filter((stock) => {
        return stock.type === filterType;
      })
    : stocks;

  if (sortType === "Alphabetically") {
    filteredStocks.sort((a, b) => {
      return a.name.toLowerCase().localeCompare(b.name.toLowerCase());
    });
  } else if (sortType === "Price") {
    filteredStocks.sort((a, b) => {
      if (a.price < b.price) {
        return -1;
      } else if (a.price > b.price) {
        return 1;
      } else {
        return 0;
      }
    });
  }

  return (
    <div>
      <SearchBar
        filterType={filterType}
        setFilterType={setFilterType}
        sortType={sortType}
        setSortType={setSortType}
      />
      <div className="row">
        <div className="col-8">
          <StockContainer
            addToPortfolio={addToPortfolio}
            stocks={filteredStocks}
          />
        </div>
        <div className="col-4">
          <PortfolioContainer
            stocks={portfolioStocks}
            removeFromPortfolio={removeFromPortfolio}
          />
        </div>
      </div>
    </div>
  );
}

export default MainContainer;
