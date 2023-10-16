import { Route, Switch, Redirect } from "react-router-dom";
import { createGlobalStyle } from "styled-components";
import { useEffect, useState } from "react";
import Home from "./components/Home";
import ProductionForm from "./components/ProductionForm";
import Navigation from "./components/Navigation";
import ProductionDetail from "./components/ProductionDetail";
import NotFound from "./components/NotFound";
import Login from "./components/Login";
import Signup from "./components/Signup";

function App() {
  const [productions, setProductions] = useState([]);
  const [user, setUser] = useState();

  useEffect(() => {
    fetchProductions();
  }, []);

  const fetchProductions = () =>
    fetch("/productions")
      .then((res) => {
        if (res.ok) {
          return res.json();
        }
      })
      .then(setProductions);

  const addProduction = (production) =>
    setProductions((current) => [...current, production]);

  if (!user) {
    if (user == null) {
      return (
        <>
          <GlobalStyle />
          <Navigation />
          <Switch>
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/signup">
              <Signup />
            </Route>
            <Route>
              <Redirect to="/login" />
            </Route>
          </Switch>
        </>
      );
    } else {
      return (
        <>
          <p>Loading...</p>
        </>
      );
    }
  }

  return (
    <>
      <GlobalStyle />
      <Navigation />
      <Switch>
        <Route path="/productions/new">
          <ProductionForm addProduction={addProduction} />
        </Route>
        <Route path="/productions/:id">
          <ProductionDetail />
        </Route>
        <Route exact path="/">
          <Home productions={productions} />
        </Route>
        <Route>
          <NotFound />
        </Route>
      </Switch>
    </>
  );
}

export default App;

const GlobalStyle = createGlobalStyle`
    body{
      background-color: black; 
      color:white;
    }
    `;
