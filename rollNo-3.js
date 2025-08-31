function greetUser(name) {
  if (!name) {
    console.log("No name provided");
    return;
  }
  console.log("Hello, " + name + "!");
}

document.getElementById("btn").addEventListener("click", function () {
  greetUser("Alice");
});
