const resultsDiv = document.querySelector("#results");
document.addEventListener("DOMContentLoaded", () => {
  const apiSearchForm = document.querySelector("#api-Search");

  apiSearchForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const query = encodeURI(e.target.search.value);
    // console.log(query);
    fetch(`https://api.tvmaze.com/singlesearch/shows?q=${query}&embed=episodes`)
      .then((r) => r.json())
      .then((data) => {
        const resultsDiv = document.querySelector("#tvApiResults");
        resultsDiv.innerHTML = "";
        console.log(data);
        if (data) {
          const name = document.createElement("h1");
          name.textContent = data.name;
          const img = document.createElement("img");
          img.src = data.image.medium;
          img.alt = data.name;
          const episodesH2 = document.createElement("h2");
          episodesH2.textContent = "Episodes";
          const episodeList = document.createElement("div");
          data._embedded.episodes.forEach((ep) => {
            const epDiv = document.createElement("div");
            const epHeader = document.createElement("h3");
            epHeader.textContent = `Episode ${ep.number}: ${ep.name}`;
            epDiv.append(epHeader);
            if (ep.image) {
              const img = document.createElement("img");
              img.src = ep.image.medium;
              epDiv.append(img);
            }
            episodeList.append(epDiv);
          });
          resultsDiv.append(name, img);
          const summary = document.createElement("p");
          summary.textContent = data.summary.replace(/<\/?[^>]+(>|$)/g, "");
          resultsDiv.append(summary, episodesH2, episodeList);
        } else {
          const error = document.createElement("p");
          error.textContent = "No results found.";
          resultsDiv.append(error);
        }
      });
  });
});

const query = "dune";
fetch(`https://www.googleapis.com/books/v1/volumes?q=${query}`, {
  headers: {
    authorization: apiKey,
  },
});
