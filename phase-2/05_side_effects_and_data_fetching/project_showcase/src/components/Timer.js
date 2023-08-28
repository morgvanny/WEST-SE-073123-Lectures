// Deliverable 3: Demonstrate the unmounting and cleanup
// phase of a component through `useEffect`

// Return a cleanup function inside the `useEffect`
// with a console.log()

// Open up the devtools to observe when the cleanup
// will occur during the stages of Component Lifecycle

import { useState, useEffect } from "react";

function Timer() {
  const [num, setNum] = useState(0);

  useEffect(() => {
    console.log("adding another setInterval");
    const intervalId = setInterval(() => {
      setNum((prevNum) => prevNum + 1);
      console.log("running");
    }, 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);
  return <p>Timer: {num}</p>;
}

export default Timer;
