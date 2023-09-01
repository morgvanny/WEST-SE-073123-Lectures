// Deliverable 3: Add navigation to the application using the `Link` and
// `NavLink` components

// - Convert any html anchor tags to `Link` or `NavLink`

// - Demonstrate the difference between `Link` and `NavLink`

import { Link, NavLink } from "react-router-dom";

const Header = ({ isDarkMode, onToggleDarkMode }) => {
  const buttonTextContent = isDarkMode ? "Light Mode" : "Dark Mode";

  return (
    <header>
      <nav>
        <h1 className="branding">
          <Link to="/">
            <span className="logo">{"//"}</span>
          </Link>
          Project Showcase
        </h1>
        <div className="navigation">
          <NavLink className="button" exact to="/projects">
            All Projects
          </NavLink>
          <NavLink className="button" exact to="/projects/new">
            Add Project
          </NavLink>
          <button onClick={onToggleDarkMode}>{buttonTextContent}</button>
        </div>
      </nav>
    </header>
  );
};

export default Header;
