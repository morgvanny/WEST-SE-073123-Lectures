import Header from "./Header";
import ProjectList from "./ProjectList";
import projects from "./projects";

function App() {
  return (
    <>
      <Header />
      <ProjectList projects={projects} />
    </>
  );
}

export default App;
