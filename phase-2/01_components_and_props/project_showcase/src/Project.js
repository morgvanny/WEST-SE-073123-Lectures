function Project({ name, link, image, phase, about }) {
  return (
    <div className="card">
      <h4>
        <a href={link}>{name}</a>
      </h4>
      <img className="image" src={image} alt={name} />
      <p>Phase: {phase}</p>
      <p>{about}</p>
    </div>
  );
}

export default Project;
