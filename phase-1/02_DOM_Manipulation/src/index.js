//BookStore has been moved to data.js
// console.log(bookStore);

const h1 = document.querySelector("header div h1");

h1.textContent = "Hello!";

function formatPrice(price) {
  return "$" + Number.parseFloat(price).toFixed(2);
}

const books = bookStore.inventory;

const renderBook = (book) => {
  // put a book on the page
  const ul = document.querySelector("ul#book-list");
  const li = document.createElement("li");
  li.className = "list-li";
  const title = document.createElement("h3");
  title.textContent = book.title;
  li.append(title);
  const author = document.createElement("p");
  const price = document.createElement("p");
  const image = document.createElement("img");
  const button = document.createElement("button");
  author.textContent = book.author;
  price.textContent = formatPrice(book.price);
  li.append(author, price, image, button);
  image.src = book.imageUrl;
  image.alt = `${book.title} cover`;
  button.textContent = "Delete";
  ul.append(li);
};

const showBooks = (books) => {
  books.forEach(renderBook);
};

showBooks(books);

const liToRemove = document.querySelectorAll("li")[1];
console.log(liToRemove);
liToRemove.remove();

// document.querySelector("#book-list").innerHTML = "";

document.getElementById("book-list");
document.getElementsByClassName("list-li");
document.querySelectorAll(".list-li");
// create a function called renderBook(book)
// it will take a book object as an argument
// and create the html struture for rendering
// that book and insert it into our webpage!

// function renderBook(book) {
// should create an li element that looks something like this:
// <li class="list-li">
//   <h3>Eloquent JavaScript : A Modern Introduction to Programming</h3>
//   <p>Marjin Haverbeke</p>
//   <p>$10.00</p>
//   <img src="https://images-na.ssl-images-amazon.com/images/I/51IKycqTPUL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg" alt="Eloquent JavaScript cover"/>
//   <button>Delete</button>
// </li>
