import { useState } from "react";

const ProjectForm = ({ onAddProject, onError, projects }) => {

  const initialFormValues = {
    name: "",
    about: "",
    phase: "",
    link: "",
    image: ""
  }

  const [formData, setFormData] = useState(initialFormValues);

  const { name, about, phase, link, image } = formData;

  const handleFormData = (e) => {
    const { name, value } = e.target;
    
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors
    setFormData({ ...formData, [name]: value});
  }

  const handleFormSubmit = (e) => {      
    e.preventDefault();

    // Optimistic Rendering
    // Update "projects" State with Newest Project Before POST 
    // onAddProject(formData);

    const requestObj = {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    }


    fetch("http://localhost:4000/projects", requestObj)
      .then(res => res.json())
      .then(newProject => {
        
        // Merge Newest Project Into "projects" State
        // Pessimistic Rendering
        onAddProject(newProject);

        // Clear Out Form Values
        setFormData(initialFormValues);
      })
      .catch(() => {
          // Undo Optimistic Rendering
          // Add Additional Code to Undo State Change (projects)

          // Filter Through Existing List of Projects in "projects" State
          // Return New List of Projects With Newest (formData) Project Filtered Out
          const revertedProjectList = projects.filter(project => {

            // Return All Projects Whose Names Do NOT Match formData.name (name)
            return project.name !== name;
          });

          // Invoke onError Function from App Component, Updating
          // "projects" State With revertedProjectList Array / Undoing
          // Optimistic Change
          onError(revertedProjectList);
      });
  }
  
  return (
    <section>
      <form className="form" autoComplete="off" onSubmit={handleFormSubmit}>
        <h3>Add New Project</h3>

        <label htmlFor="name">Name</label>
        <input 
          type="text" 
          id="name" 
          name="name"
          value={name}
          onChange={handleFormData}
        />

        <label htmlFor="about">About</label>
        <textarea 
          id="about" 
          name="about"
          value={about}
          onChange={handleFormData}
        />

        <label htmlFor="phase">Phase</label>
        <select 
          name="phase" 
          id="phase"
          value={phase}
          onChange={handleFormData}
        >
          <option>Select One</option>
          <option value="1">Phase 1</option>
          <option value="2">Phase 2</option>
          <option value="3">Phase 3</option>
          <option value="4">Phase 4</option>
          <option value="5">Phase 5</option>
        </select>

        <label htmlFor="link">Project Homepage</label>
        <input 
          type="text" 
          id="link" 
          name="link" 
          value={link}
          onChange={handleFormData}
        />

        <label htmlFor="image">Screenshot</label>
        <input 
          type="text" 
          id="image" 
          name="image" 
          value={image}
          onChange={handleFormData}
        />

        <button type="submit">Add Project</button>
      </form>
    </section>
  );
};

export default ProjectForm;
