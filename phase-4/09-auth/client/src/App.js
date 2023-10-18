import { useEffect, useState } from "react";
import { Redirect, Route, Switch } from "react-router-dom";
import { createGlobalStyle } from "styled-components";
import Home from "./components/Home";
import Login from "./components/Login";
import Navigation from "./components/Navigation";
import NotFound from "./components/NotFound";
import ProductionDetail from "./components/ProductionDetail";
import ProductionForm from "./components/ProductionForm";
import Signup from "./components/Signup";

function App() {
	const [productions, setProductions] = useState([]);
	const [user, setUser] = useState();

	useEffect(() => {
		fetch("/me").then((r) => {
			if (r.ok) {
				return r.json().then(setUser);
			} else {
				setUser(null);
			}
		});

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
		if (user === null) {
			return (
				<>
					<GlobalStyle />
					<Navigation setUser={setUser} />
					<Switch>
						<Route path="/login">
							<Login setUser={setUser} />
						</Route>
						<Route path="/signup">
							<Signup setUser={setUser} />
						</Route>
						<Redirect to="/login" />
					</Switch>
				</>
			);
		} else {
			return (
				<>
					<GlobalStyle />
					<Navigation />
					<p>Loading...</p>
				</>
			);
		}
	}

	return (
		<>
			<GlobalStyle />
			<Navigation setUser={setUser} />
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
