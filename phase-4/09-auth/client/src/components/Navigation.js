import { useState } from "react";
import { GiHamburgerMenu } from "react-icons/gi";
import { Link, useHistory } from "react-router-dom";
import styled from "styled-components";

function Navigation({ setUser }) {
	const [menu, setMenu] = useState(false);
	const history = useHistory();

	const handleLogout = () => {
		fetch("/logout", {
			method: "DELETE",
		}).then((res) => {
			if (res.ok) {
				setUser(null);
				history.push("/login");
			}
		});
	};

	return (
		<Nav>
			<NavH1>Flatiron Theater Company</NavH1>
			<Menu>
				{!menu ? (
					<div onClick={() => setMenu(!menu)}>
						<GiHamburgerMenu size={30} />
					</div>
				) : (
					<ul>
						<li onClick={() => setMenu(!menu)}>x</li>
						<li>
							<Link to="/productions/new">New Production</Link>
						</li>
						<li>
							<Link to="/"> Home</Link>
						</li>
						<li>
							<Link to="/login"> Login</Link>
						</li>
						<li>
							<Link to="/signup"> Signup</Link>
						</li>
						<li onClick={handleLogout}> Logout </li>
					</ul>
				)}
			</Menu>
		</Nav>
	);
}

export default Navigation;

const NavH1 = styled.h1`
  font-family: "Splash", cursive;
`;
const Nav = styled.div`
  display: flex;
  justify-content: space-between;
`;

const Menu = styled.div`
  display: flex;
  align-items: center;
  a {
    text-decoration: none;
    color: white;
    font-family: Arial;
  }
  a:hover {
    color: pink;
  }
  ul {
    list-style: none;
  }
`;
