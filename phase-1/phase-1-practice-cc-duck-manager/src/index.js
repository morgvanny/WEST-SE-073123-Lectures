// write your code here!
let selectedDuck;
const likeSpan = document.querySelector("#like-span");
const duckNav = document.querySelector("#duck-nav");
const nameDetail = document.querySelector("#duck-display-name");
const imageDetail = document.querySelector("#duck-display-image");
const likeButton = document.querySelector("#duck-display-likes");

const addNavImage = (duck) => {
  const navImage = document.createElement("img");
  navImage.addEventListener("click", () => {
    selectedDuck = duck;
    nameDetail.textContent = duck.name;
    imageDetail.src = duck.img_url;
    imageDetail.alt = duck.name;
    likeSpan.textContent = duck.likes;
    // likeButton.textContent = `${duck.likes} likes`;
  });
  navImage.src = duck.img_url;
  navImage.alt = duck.name;
  duckNav.append(navImage);
};

fetch("http://localhost:3000/ducks")
  .then((res) => res.json())
  .then((ducks) => {
    ducks.forEach(addNavImage);
  });

likeButton.addEventListener("click", () => {
  selectedDuck.likes += 1;
  likeSpan.textContent = selectedDuck.likes;
  // const currentLikes = parseInt(likeButton.textContent);
  // likeButton.textContent = `${selectedDuck.likes} likes`;
  // likeButton.textContent = `${currentLikes + 1} likes`;
});

// listen for form submit
// create duck object from form data (inputs)
// call addNavImage and pass duck in

const form = document.querySelector("#new-duck-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const duck = {
    name: form["duck-name-input"].value,
    img_url: form["duck-image-input"].value,
    likes: 0,
  };

  addNavImage(duck);
});
