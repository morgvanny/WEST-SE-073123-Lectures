import { useState } from "react";

import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import ProjectList from "./components/ProjectList";
import Search from "./components/Search";

const App = () => {
  const [projects, setProjects] = useState([]);
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");
  const [phase, setPhase] = useState("All");

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };
  // # Deliverable 1: Configure a <button> in our App
  // that will use json-server to fetch projects
  // and store them in state

  // - Add an onClick event listener to the "Load Projects"
  // button

  // - When the button is clicked, make a fetch
  // request to "http://localhost:4000/projects"
  // and set the `projects` state to the value
  // returned by the response
  const loadProjects = () => {
    fetch("http://localhost:3000/projects")
      .then((r) => r.json())
      .then((projects) => {
        setProjects(projects);
      });
  };

  const searchResults = projects.filter((project) => {
    return project.name.toLowerCase().includes(searchQuery.toLowerCase());
  });

  const phaseResults =
    phase === "All"
      ? searchResults
      : searchResults.filter((project) => {
          return project.phase === parseInt(phase);
        });

  return (
    <div className={isDarkMode ? "App" : "App light"}>
      <Header handleClick={toggleDarkMode} isDarkMode={isDarkMode} />
      <ProjectForm />
      <Search
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
        setPhase={setPhase}
      />
      <button onClick={loadProjects}>Load Projects</button>
      <ProjectList projects={phaseResults} />
    </div>
  );
};

export default App;
