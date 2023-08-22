import { useState } from "react";

const ProjectListItem = ({ id, about, image, link, name, phase }) => {
  // const stateArray = useState(0);
  // // returns an array with 2 elements
  // // first element is the state variable
  // // second element is the setter function
  // const claps = stateArray[0];
  // const setClaps = stateArray[1];
  const [claps, setClaps] = useState(0);

  console.log(`project #${id} is rendering`);

  return (
    <li className="card">
      <figure className="image">
        <img src={image} alt={name} />
        <button
          onClick={() => {
            setClaps(claps + 1);
          }}
          className="claps"
        >
          👏{claps}
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
      </footer>
    </li>
  );
};

export default ProjectListItem;
