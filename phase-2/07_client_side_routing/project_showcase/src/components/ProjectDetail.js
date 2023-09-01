// Deliverable 4: Using the useParams hook, access the :id param from the URL
// to trigger appropriate GET requests

import { useState } from "react";

const ProjectDetail = ({ project }) => {
  const [claps, setClaps] = useState(0);

  // Reference isLoaded State. If False, Render Simple H1 "Loading..." Component
  if (!project) {
    return <h1>Loading...</h1>;
  }

  const { image, name, about, link, phase } = project;

  const handleClapClick = () => {
    setClaps((claps) => claps + 1);
  };

  return (
    <section>
      <div className="project-detail box">
        <div className="project-image">
          <img src={image} alt={name} />
          <button className="claps" onClick={handleClapClick}>
            👏{claps}
          </button>
        </div>
        <div className="details">
          <h2>{name}</h2>
          <p>{about}</p>
          {link ? (
            <p>
              <a target="_blank" rel="noreferrer" href={link}>
                Project Homepage
              </a>
            </p>
          ) : null}
          <div className="extra">
            <span className="badge blue">Phase {phase}</span>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProjectDetail;
