// write your code here
const menuDiv = document.querySelector("#ramen-menu");
let selectedRamen;

const addMenuItem = (ramen) => {
  const item = document.createElement("div");
  const image = document.createElement("img");
  image.src = ramen.image;

  const button = document.createElement("button");
  button.textContent = "delete";
  button.addEventListener("click", () => {
    fetch(`http://localhost:3000/ramens/${ramen.id}`, { method: "DELETE" })
      .then((r) => r.json())
      .then(() => {
        item.remove();
      });
  });
  item.append(image, button);
  menuDiv.append(item);
  image.addEventListener("click", () => displayDetails(ramen));
};

fetch("http://localhost:3000/ramens")
  .then((r) => r.json())
  .then((ramens) => {
    ramens.forEach((r) => addMenuItem(r));
    displayDetails(ramens[0]);
  });

const displayDetails = (ramen) => {
  selectedRamen = ramen;
  const { name, image, restaurant, rating, comment } = ramen;
  const img = document.querySelector(".detail-image");
  img.src = image;
  img.alt = name;
  document.querySelector(".name").textContent = name;
  document.querySelector(".restaurant").textContent = restaurant;
  document.querySelector("#rating-display").textContent = rating;
  document.querySelector("#comment-display").textContent = comment;
};

const form = document.querySelector("#new-ramen");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const ramen = {
    image: form.image.value,
    name: form.name.value,
    restaurant: form.restaurant.value,
    rating: parseInt(form.rating.value),
    comment: form["new-comment"].value,
  };

  fetch("http://localhost:3000/ramens", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(ramen),
  })
    .then((res) => res.json())
    .then((ramen) => {
      addMenuItem(ramen);
      form.reset();
    });
});

const editForm = document.querySelector("#edit-ramen");

editForm.addEventListener("submit", (e) => {
  e.preventDefault();
  selectedRamen.rating = parseInt(editForm.rating.value);
  selectedRamen.comment = editForm["new-comment"].value;
  fetch(`http://localhost:3000/ramens/${selectedRamen.id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(selectedRamen),
  })
    .then((r) => r.json())
    .then((updatedRamen) => {
      displayDetails(updatedRamen);
      editForm.reset();
    });
});
