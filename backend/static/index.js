let classnames = {
  body: "",
  header: "",
  footer: "",
  app: "",
};

// Function to fetch user data from Flask backend
function fetchUsers() {
  fetch("/users") // MAKE A CALL TO FLASK, GETS BACKEND
    .then((response) => response.json()) // Parse the JSON response
    .then((users) => {
      const userList = document.getElementById("user-list");
      userList.classList = "gap-4 flex flex-col";
      users.forEach((user) => {
        const listContainer = document.createElement("div");
        listContainer.classList = "bg-slate-300 p-4 rounded-lg shadow-lg";
        const listItem = document.createElement("li");
        listItem.textContent = `${user.first_name} ${user.last_name}: ${user.email}`;
        listItem.classList = "font-bold text-slate-800 text-center list-none";
        listContainer.appendChild(listItem);
        // BELOW, THE USERS NAME AND LAST NAME ARE FETCHED
        userList.appendChild(listContainer);
      });
    });
}

// Function to fetch service data from Flask backend
function fetchServices() {
  fetch("/services") // MAKE A CALL TO FLASK, GETS BACKEND
    .then((response) => response.json()) // Parse the JSON response
    .then((services) => {
      const serviceList = document.getElementById("service-list");
      serviceList.innerHTML = "";
      services.forEach((service) => {
        const listItem = document.createElement("li");
        // ALL SERVICES
        listItem.textContent = service.name;
        serviceList.appendChild(listItem);
      });
    });
}

// Fetch data when the page loads
fetchUsers();
fetchServices();

function userToDict() {
  const firstNameInput = document.getElementById("first_name");
  const lastNameInput = document.getElementById("last_name");
  const emailInput = document.getElementById("email");

  let user = {
    User: {
      first_name: firstNameInput.value,
      last_name: lastNameInput.value,
      email: emailInput.value,
      // email: "email@email.test",
    },
  };

  let userDict = JSON.stringify(user);

  const fetchURL = "http://localhost:5000/create_object";
  const fetchOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: userDict,
  };

  console.log(userDict);

  fetch(fetchURL, fetchOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log("POST request successful: ", data);
    })
    .catch((error) => {
      console.error("There was a problem with the POST request: ", error);
    });
}