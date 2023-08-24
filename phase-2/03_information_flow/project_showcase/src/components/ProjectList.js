import ProjectListItem from "./ProjectListItem";

const ProjectList = ({ projects }) => {
  const projectListItems = projects.map((project) => (
    <ProjectListItem key={project.id} {...project} />
  ));

  // Deliverable 3: Refactor the filter component out of
  // `ProjectList` and implement inverse data flow

  // - Refactor the `searchQuery` state and the filter
  // method inside of the `ProjectList` component to
  // the `App` component

  // - Using inverse data flow, get the value of the
  // input field UP to the App component

  // - Write a callback function inside the App
  // component:

  //   - the function should take in a new search value
  // and set state with that value

  //   - pass the callback function down as a prop to
  // `ProjectList`

  // - Call the callback function from the onChange
  // event listener

  return (
    <section>
      <h2>Projects</h2>
      <ul className="cards">{projectListItems}</ul>
    </section>
  );
};

export default ProjectList;
