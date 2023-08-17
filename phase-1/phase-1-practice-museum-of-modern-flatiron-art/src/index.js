let currentExhibit;

const commentSectionDiv = document.querySelector("#comments-section");
const ticketsSpan = document.querySelector("#tickets");

const displayComment = (comment) => {
  const commentP = document.createElement("p");
  commentP.textContent = comment;
  commentSectionDiv.append(commentP);
};

const displayExhibit = (exhibit) => {
  currentExhibit = exhibit;
  const h2Title = document.querySelector("#exhibit-title");
  h2Title.textContent = exhibit.title;
  const img = document.querySelector("#exhibit-image");
  img.src = exhibit.image;
  img.alt = exhibit.title;

  ticketsSpan.textContent = exhibit.tickets_bought;
  const descP = document.querySelector("#exhibit-description");
  descP.textContent = exhibit.description;

  exhibit.comments.forEach(displayComment);
};

fetch("http://localhost:3000/current-exhibits/1")
  .then((resp) => resp.json())
  .then((ex) => {
    displayExhibit(ex);
  });

const form = document.querySelector("#comment-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const comment = form["comment-input"].value;
  displayComment(comment);
  form.reset();
});

document.querySelector("#buy-tickets-button").addEventListener("click", () => {
  currentExhibit.tickets_bought += 1;
  ticketsSpan.textContent = currentExhibit.tickets_bought;
  // const current = parseInt(ticketsSpan.textContent);
  // ticketsSpan.textContent = current + 1;
});
