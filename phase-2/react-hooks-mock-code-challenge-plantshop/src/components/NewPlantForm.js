import React, { useState } from "react";

function NewPlantForm({ addPlant }) {
  const initialFormState = {
    name: "",
    image: "",
    price: "",
  };

  const [formData, setFormData] = useState(initialFormState);

  const handleChange = (e) => {
    const value =
      e.target.name === "price" ? parseFloat(e.target.value) : e.target.value;

    setFormData((formData) => {
      return { ...formData, [e.target.name]: value };
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    addPlant(formData);
    setFormData(initialFormState);
  };

  return (
    <div className="new-plant-form">
      <h2>New Plant</h2>
      <form onSubmit={handleSubmit}>
        <input
          value={formData.name}
          onChange={handleChange}
          type="text"
          name="name"
          placeholder="Plant name"
        />
        <input
          value={formData.image}
          onChange={handleChange}
          type="text"
          name="image"
          placeholder="Image URL"
        />
        <input
          value={formData.price}
          onChange={handleChange}
          type="number"
          name="price"
          step="0.01"
          placeholder="Price"
        />
        <button type="submit">Add Plant</button>
      </form>
    </div>
  );
}

export default NewPlantForm;
