let currentGame;
const detailHighScore = document.querySelector("#detail-high-score");

const addGame = (game) => {
  const gameH5 = document.createElement("h5");
  gameH5.addEventListener("click", () => {
    showDetails(game);
  });
  gameH5.textContent = `${game.name} (${game.manufacturer_name})`;
  const nav = document.querySelector("#game-list");
  nav.append(gameH5);
};

fetch("http://localhost:3000/games")
  .then((r) => r.json())
  .then((games) => {
    showDetails(games[0]);
    games.forEach((game) => addGame(game));
  });

const showDetails = (game) => {
  currentGame = game;
  const img = document.querySelector("#detail-image");
  img.src = game.image;
  img.alt = game.name;
  const detailName = document.querySelector("#detail-title");
  detailName.textContent = game.name;
  detailHighScore.textContent = game.high_score;
};

const form = document.querySelector("#high-score-form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const scoreInputValue = parseInt(form["score-input"].value);
  currentGame.high_score = scoreInputValue;
  detailHighScore.textContent = currentGame.high_score;
  form.reset();
});
