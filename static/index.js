function userToDict() {
  const firstNameInput = document.getElementById("first_name");
  const lastNameInput = document.getElementById("last_name");

  let user = {
    User: {
      first_name: firstNameInput.value,
      last_name: lastNameInput.value,
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
