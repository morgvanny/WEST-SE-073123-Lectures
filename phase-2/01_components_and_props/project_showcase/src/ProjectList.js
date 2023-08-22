import Project from "./Project";

function ProjectList({ projects }) {
  const projectCards = projects.map((project) => {
    return (
      <Project
        image={project.image}
        name={project.name}
        link={project.link}
        about={project.about}
        phase={project.phase}
      />
    );
  });

  return (
    <>
      <h2>Projects</h2>
      <div className="cards">{projectCards}</div>
    </>
  );
}

export default ProjectList;
