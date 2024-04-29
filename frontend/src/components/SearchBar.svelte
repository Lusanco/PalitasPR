<!-- <script></script>

<div class="flex flex-col px-4 mx-auto shadow-md md:px-0 md:join md:flex-row">
  <div>
    <div>
      <input
        class="w-full md:w-fit input input-bordered join-item"
        placeholder="Search"
      />
    </div>
  </div>
  <select class="select select-bordered join-item">
    <option disabled selected>Pueblo</option>
    <option>Ponce</option>
    <option>San Juan</option>
    <option>Aguadilla</option>
  </select>
  <div class="w-full indicator">
    <button class="w-full md:w-fit btn join-item">Search</button>
  </div>
</div> -->

<script>
  // @ts-ignore
  import { changeView } from "../scripts/viewManager";
  // @ts-ignore
  import { onMount } from "svelte";
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
          // let listDiv = document.getElementById("search-list");
          // let listCard = document.createElement("li");
          // // @ts-ignore
          // listCard.classList = "bg-teal-50 h-10 rounded-md w-full";
          // listDiv.append(listCard);

          console.log(
            `Service ID: ${serviceId}, Towns: ${towns}, Name: ${name}`
          ); // Example usage
        }
      })
      .catch((error) => {
        console.log(error);
        errorMessage = error;
      });
  }
</script>

<div
  class="flex flex-col px-4 mx-auto lg:shadow-md md:px-0 md:join md:flex-row"
>
  <div>
    <div>
      <input
        class="w-full md:w-fit input input-bordered join-item"
        placeholder="Search"
        bind:value={searchInput}
      />
    </div>
  </div>
  <select class="select select-bordered join-item">
    <option selected disabled>Town</option>
    <option>Ponce</option>
    <option>San Juan</option>
    <option>Aguadilla</option>
  </select>
  <div class="w-full indicator">
    <button
      class="w-full font-semibold text-teal-100 bg-teal-800 md:w-fit btn join-item"
      on:click={handleSearch}>Search</button
    >
  </div>
</div>

<!-- <ul id="search-list scroll-auto" class=""></ul> -->
