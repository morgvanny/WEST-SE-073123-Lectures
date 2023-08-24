import { useState } from "react";

const ProjectForm = ({ addProject }) => {
  const [newProject, setNewProject] = useState({
    name: "",
    about: "",
    phase: "",
    link: "",
    image: "",
  });

  const { name, about, phase, link, image } = newProject;

  const handleSubmit = (e) => {
    e.preventDefault();
    const newProject = { name, about, phase, link, image };
    fetch("http://localhost:4000/projects", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newProject),
    })
      .then((r) => r.json())
      .then((createdProject) => {
        // update state so created project shows up
        setNewProject({
          name: "",
          about: "",
          phase: "",
          link: "",
          image: "",
        });
        addProject(createdProject);
      });
  };

  const handleOnChange = (e) => {
    const key = e.target.name;
    const value = e.target.value;
    setNewProject({ ...newProject, [key]: value });
  };

  return (
    <section>
      <form onSubmit={handleSubmit} className="form" autoComplete="off">
        <h3>Add New Project</h3>

        <label htmlFor="name">Name</label>
        <input
          value={name}
          onChange={handleOnChange}
          type="text"
          id="name"
          name="name"
        />

        <label htmlFor="about">About</label>
        <textarea
          value={about}
          onChange={handleOnChange}
          id="about"
          name="about"
        />

        <label htmlFor="phase">Phase</label>
        <select value={phase} onChange={handleOnChange} name="phase" id="phase">
          <option>Select One</option>
          <option value="1">Phase 1</option>
          <option value="2">Phase 2</option>
          <option value="3">Phase 3</option>
          <option value="4">Phase 4</option>
          <option value="5">Phase 5</option>
        </select>

        <label htmlFor="link">Project Homepage</label>
        <input
          value={link}
          onChange={handleOnChange}
          type="text"
          id="link"
          name="link"
        />

        <label htmlFor="image">Screenshot</label>
        <input
          value={image}
          onChange={handleOnChange}
          type="text"
          id="image"
          name="image"
        />

        <button type="submit">Add Project</button>
      </form>
    </section>
  );
};

export default ProjectForm;

// Deliverable 1: Make the `ProjectForm` component a controlled component

// - Initialize state for all the form fields found in the component

// - Add an `onChange` event to each field that will update state associated
// with the field that is interacted with

// - Provide a `value` attribute to each form field that will return the
// associated piece of state

// - Add an `onSubmit` event handler to the form

// const ProjectForm = ({ addProject }) => {
//   const [name, setName] = useState("");
//   const [about, setAbout] = useState("");
//   const [phase, setPhase] = useState("");
//   const [link, setLink] = useState("");
//   const [image, setImage] = useState("");

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     const newProject = { name, about, phase, link, image };
//     fetch("http://localhost:4000/projects", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(newProject),
//     })
//       .then((r) => r.json())
//       .then((createdProject) => {
//         // update state so created project shows up
//         setName("");
//         setImage("");
//         setLink("");
//         setPhase("");
//         setAbout("");
//         addProject(createdProject);
//       });
//   };

//   return (
//     <section>
//       <form onSubmit={handleSubmit} className="form" autoComplete="off">
//         <h3>Add New Project</h3>

//         <label htmlFor="name">Name</label>
//         <input
//           value={name}
//           onChange={(e) => {
//             setName(e.target.value);
//           }}
//           type="text"
//           id="name"
//           name="name"
//         />

//         <label htmlFor="about">About</label>
//         <textarea
//           value={about}
//           onChange={(e) => setAbout(e.target.value)}
//           id="about"
//           name="about"
//         />

//         <label htmlFor="phase">Phase</label>
//         <select
//           value={phase}
//           onChange={(e) => setPhase(e.target.value)}
//           name="phase"
//           id="phase"
//         >
//           <option>Select One</option>
//           <option value="1">Phase 1</option>
//           <option value="2">Phase 2</option>
//           <option value="3">Phase 3</option>
//           <option value="4">Phase 4</option>
//           <option value="5">Phase 5</option>
//         </select>

//         <label htmlFor="link">Project Homepage</label>
//         <input
//           value={link}
//           onChange={(e) => setLink(e.target.value)}
//           type="text"
//           id="link"
//           name="link"
//         />

//         <label htmlFor="image">Screenshot</label>
//         <input
//           value={image}
//           onChange={(e) => setImage(e.target.value)}
//           type="text"
//           id="image"
//           name="image"
//         />

//         <button type="submit">Add Project</button>
//       </form>
//     </section>
//   );
// };

// export default ProjectForm;
