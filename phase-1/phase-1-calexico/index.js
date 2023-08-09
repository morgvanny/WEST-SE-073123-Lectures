// Write your code here...
const menuItems = document.querySelector("#menu-items");
const cartSpan = document.querySelector("#number-in-cart");
let itemList;
let currentItem;

const updateTotal = () => {
  let t = 0;
  itemList.forEach((i) => {
    t += i.price * i.number_in_bag;
  });
  document.querySelector("#total").textContent = t.toFixed(2);
};

const makeSpan = (item) => {
  const span = document.createElement("span");
  span.addEventListener("click", () => renderDetails(item));
  span.textContent = item.name;
  menuItems.append(span);
};

const makeList = (items) => {
  items.forEach((item) => {
    makeSpan(item);
  });
};

fetch("http://localhost:3000/menu")
  .then((r) => r.json())
  .then((items) => {
    renderDetails(items[0]);
    itemList = items;
    updateTotal();
    makeList(items);
  });

const renderDetails = (item) => {
  currentItem = item;
  const image = document.querySelector("#dish-image");
  image.src = item.image;
  const name = document.querySelector("#dish-name");
  name.textContent = item.name;
  const desc = document.querySelector("#dish-description");
  desc.textContent = item.description;
  const price = document.querySelector("#dish-price");
  price.textContent = `$${item.price.toFixed(2)}`;
  cartSpan.textContent = item.number_in_bag;
};

const updateCurrentItem = () => {
  fetch(`http://localhost:3000/menu/${currentItem.id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(currentItem),
  })
    .then((r) => r.json())
    .then((updatedItem) => {
      updateTotal();
    });
};

const form = document.querySelector("#cart-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const inputValue = parseInt(form["cart-amount"].value);
  const currentValue = currentItem.number_in_bag;
  currentItem.number_in_bag = currentValue + inputValue;
  cartSpan.textContent = currentItem.number_in_bag;
  updateCurrentItem();
  form.reset();
});
