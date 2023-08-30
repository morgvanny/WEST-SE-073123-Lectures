import React, { useState } from "react";
import Header from "./Header";
import ListingsContainer from "./ListingsContainer";

function App() {
  const [searchTerm, setSearchTerm] = useState("");

  return (
    <div className="app">
      <Header setSearchTerm={setSearchTerm} />
      <ListingsContainer searchTerm={searchTerm} />
    </div>
  );
}

export default App;
