import React from "react";
import Nav from "./Nav";
import hogs from "../porkers_data";
import HogContainer from "./HogContainer";

function App() {
  return (
    <div className="ui grid container App">
      <div className="sixteen wide column centered">
        <Nav />
      </div>
      <div className="sixteen wide column centered">
        <HogContainer hogs={hogs} />
      </div>
    </div>
  );
}

export default App;
