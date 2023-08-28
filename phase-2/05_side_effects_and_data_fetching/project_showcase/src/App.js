import { useState, useEffect } from "react";
import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import Timer from "./components/Timer";
import ProjectList from "./components/ProjectList";
import ProjectListItem from "./components/ProjectListItem";

// Deliverable 1: Implement useEffect in App component
// to load projects

// Import the `useEffect` hook from the React library

// Invoke `useEffect` and make a `GET` request using
// the `fetch` method

// Update `projects` state upon successful response
// from the server

// Deliverable 2: Demonstrate the order of operations
// between rendering a component and running the side
// effect

// Place a console.log() inside the `App` component as
// well as the `useEffect` method

// Open up the devtools to observe when each phase of
// the component will occur

const App = () => {
  const [projects, setProjects] = useState([]);
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [isTimerShowing, setIsTimerShowing] = useState(true);
  const [project, setProject] = useState();
  const [projectId, setProjectId] = useState("");

  useEffect(() => {
    fetch(`http://localhost:4000/projects/`)
      .then((r) => r.json())
      .then((projects) => {
        setProjects(projects);
      });
  }, []);

  const fetchProject = (id) => {
    fetch(`http://localhost:4000/projects/${id}`)
      .then((r) => r.json())
      .then((project) => setProject(project));
  };

  const handleChange = (e) => {
    setProjectId(e.target.value);
    fetchProject(e.target.value);
  };

  const onAddProject = (newProject) => {
    const newProjectCollection = [...projects, newProject];
    setProjects(newProjectCollection);
  };

  const onToggleDarkMode = () => setIsDarkMode(!isDarkMode);

  // Update "projects" State With Filtered List When Error Occurs
  // With POST Request
  const onError = (filteredList) => {
    setProjects(filteredList);
  };

  return (
    <div className={isDarkMode ? "App" : "App light"}>
      <Header isDarkMode={isDarkMode} onToggleDarkMode={onToggleDarkMode} />
      <button onClick={() => setIsTimerShowing(!isTimerShowing)}>
        {isTimerShowing ? "Hide Timer" : "Show Timer"}
      </button>
      {isTimerShowing ? <Timer /> : null}
      <ProjectForm
        onAddProject={onAddProject}
        onError={onError}
        projects={projects}
      />
      <input value={projectId} onChange={handleChange} />
      {projectId ? <ProjectListItem {...project} /> : null}
      {/* <ProjectList projects={projects} /> */}
    </div>
  );
};

export default App;
