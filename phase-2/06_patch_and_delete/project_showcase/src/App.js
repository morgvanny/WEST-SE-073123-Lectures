import { useEffect, useState } from "react";

import Header from "./components/Header";
import ProjectForm from "./components/ProjectForm";
import ProjectList from "./components/ProjectList";
import ProjectEditForm from "./components/ProjectEditForm";

const App = () => {
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [projects, setProjects] = useState([]);
  const [projectId, setProjectId] = useState(null);

  useEffect(() => {
    fetch("http://localhost:4000/projects")
      .then((resp) => resp.json())
      .then((projects) => setProjects(projects));
  }, []);

  const onToggleDarkMode = () => {
    setIsDarkMode((isDarkMode) => !isDarkMode);
  };

  const onAddProject = (newProj) => {
    setProjects((projects) => [...projects, newProj]);
  };

  const onEditedProject = (updatedProject) => {
    setProjects((projects) =>
      projects.map((p) => {
        if (p.id === updatedProject.id) {
          return updatedProject;
        } else {
          return p;
        }
      })
    );
    setProjectId(null);
  };

  const removeProject = (id) => {
    setProjects((projects) => projects.filter((p) => p.id !== id));
  };

  const enterProjectEditModeFor = (projectId) => {
    setProjectId(projectId);
  };

  const renderForm = projectId ? (
    <ProjectEditForm projectId={projectId} onEditedProject={onEditedProject} />
  ) : (
    <ProjectForm onAddProject={onAddProject} />
  );

  return (
    <div className={isDarkMode ? "App" : "App light"}>
      <Header isDarkMode={isDarkMode} onToggleDarkMode={onToggleDarkMode} />
      {renderForm}
      <ProjectList
        projects={projects}
        enterProjectEditModeFor={enterProjectEditModeFor}
        removeProject={removeProject}
        onEditedProject={onEditedProject}
      />
    </div>
  );
};

export default App;
