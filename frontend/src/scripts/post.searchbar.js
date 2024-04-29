import axios from "axios";

let searchInput = document.getElementById("search-input");
let townInput = "All"; // No default town selected
let services = []; // Array to store fetched services
let errorMessage = ""; // Added to store error messages

async function handleSearch() {
  const data = {
    Service: {
      name: searchInput,
      town: townInput,
    },
  };

  axios
    .post("/api/filter", data)
    .then((response) => {
      services = response.data;
      console.log(services);

      // Loop through each service in the response
      for (const serviceId in services) {
        const service = services[serviceId];
        const name = service.first_name + " " + service.last_name; // Access the towns array
        const towns = service.towns;
        let listDiv = document.getElementById("search-list");
        let listCard = document.createElement("li");
        // @ts-ignore
        listCard.classList = "bg-black h-10 rounded-md w-full";
        listDiv.append(listCard);

        console.log(`Service ID: ${serviceId}, Towns: ${towns}, Name: ${name}`); // Example usage
      }
    })
    .catch((error) => {
      console.log(error);
      errorMessage = error;
    });
}

export default handleSearch;
