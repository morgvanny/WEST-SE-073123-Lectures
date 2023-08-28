// Deliverable 2: Click the delete button and make a 
// DELETE request

// - Attach an `onClick` event listener to the delete 
// button

// - Add a `DELETE` fetch request to the event handler 
// for the delete button

// - Update the `projects` state in the parent component
// `App` using the `.filter` function

  //  The goal is to return a new array with the deleted project excluded

// -----------------

  // Deliverable 3: Click the claps button and persist the updated number of claps

  // - Send a `PATCH` request when the `clapsCount` is updated through a click event
  
  // - Update the `projects` state in the parent component `App` using the `.map` function

  import { useState } from "react";
  import { FaPencilAlt, FaTrash } from "react-icons/fa";
  
  const ProjectListItem = ({ project, enterProjectEditModeFor }) => {
    const { id, image, about, name, link, phase } = project;
  
    const [clapCount, setClapCount] = useState(0);
  
    const handleClap = () => setClapCount(prevCount => prevCount + 1);
  
    const handleEditClick = () => {
      enterProjectEditModeFor(id);
    };
  
    const handleDeleteClick = () => {};
  
    return (
      <li className="card">
        <figure className="image">
          <img src={image} alt={name} />
          <button onClick={handleClap} className="claps">
            👏{clapCount}
          </button>
        </figure>
  
        <section className="details">
          <h4>{name}</h4>
          <p>{about}</p>
          {link ? (
            <p>
              <a href={link}>Link</a>
            </p>
          ) : null}
        </section>
  
        <footer className="extra">
          <span className="badge blue">Phase {phase}</span>
          <div className="manage">
            <button onClick={handleEditClick}>
              <FaPencilAlt />
            </button>
            <button onClick={handleDeleteClick}>
              <FaTrash />
            </button>
          </div>
        </footer>
      </li>
    );
  };
  
  export default ProjectListItem;
  