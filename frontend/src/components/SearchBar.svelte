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
  import { changeView } from "../scripts/viewManager";
  import { onMount } from "svelte";

  let searchTerm = "";
  let selectedTown = ""; // No default town selected
  let services = []; // Array to store fetched services
  let errorMessage = ""; // Added to store error messages

  async function fetchServices() {
    try {
      const response = await fetch("/api/filter", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          Service: {
            name: searchTerm,
            town: selectedTown === "" ? undefined : selectedTown, // Check for empty string
          },
        }),
      });

      const data = await response.json();

      if (data.error) {
        errorMessage = data.error;
        services = []; // Clear services on error
      } else {
        errorMessage = "";
        services = data;
      }
    } catch (error) {
      console.error("Network error:", error);
      errorMessage = "Network error occurred.";
      services = []; // Clear services on error
    }
  }

  async function handleSearch() {
    services = []; // Clear previous results before fetching new data
    await fetchServices();
    changeView("SearchResults");
  }

  // onMount(async () => {
  //   await fetchServices(); // Fetch initial data (optional, can be triggered on a separate action)
  // });
</script>

<div
  class="flex flex-col px-4 mx-auto lg:shadow-md md:px-0 md:join md:flex-row"
>
  <div>
    <div>
      <input
        class="w-full md:w-fit input input-bordered join-item"
        placeholder="Search"
        bind:value={searchTerm}
      />
    </div>
  </div>
  <select class="select select-bordered join-item" bind:value={selectedTown}>
    <option value="">All Pueblos</option>
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
