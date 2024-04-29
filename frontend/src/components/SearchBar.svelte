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
  let switcher = false;

  async function handleSearch() {
    const data = {
      Service: {
        name: searchInput,
        town: townInput,
      },
    };

    axios
      .post("/api/filter", data)
      // .get("https://jsonplaceholder.typicode.com/users")
      .then((response) => {
        services = response.data;
        // console.log(services);

        // Loop through each service in the response
        for (const serviceId in services) {
          const service = services[serviceId];

          switcher = true;
        }
      })
      .catch((error) => {
        console.log(error);
        errorMessage = error;
      });
  }
</script>

<!--
  Heads up! 👋

  Plugins:
    - @tailwindcss/forms
-->

<div class="relative">
  <label for="Search" class="sr-only"> Search </label>

  <input
    type="text"
    id="Search"
    bind:value={searchInput}
    placeholder="Search for..."
    class="w-full rounded-md border-gray-200 py-2.5 pe-10 shadow-sm sm:text-sm"
  />

  <span class="absolute inset-y-0 grid w-10 end-0 place-content-center">
    <button
      on:click={handleSearch}
      type="button"
      class="text-gray-600 hover:text-gray-700"
    >
      <span class="sr-only">Search</span>

      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-4 h-4"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
        />
      </svg>
    </button>
  </span>
</div>
<!-- <div class="max-w-xs mx-auto">
  <select
    id="example1"
    class="block w-full border-gray-300 rounded-md shadow-sm focus:border-primary-300 focus:ring focus:ring-primary-200 focus:ring-opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50"
  >
    <option value="">Option01</option>
    <option value="">Option02</option>
    <option value="">Option03</option>
  </select>
</div> -->

<div class="h-full overflow-auto">
  {#if switcher === false}
    <div class="hidden"></div>
  {:else}
    {#each services as service}
      <div
        class="relative block p-4 overflow-hidden border border-gray-100 rounded-lg sm:p-6 lg:p-8"
      >
        <span
          class="absolute inset-x-0 bottom-0 h-2 bg-gradient-to-r from-green-300 via-blue-500 to-purple-600"
        ></span>

        <div class="sm:flex sm:justify-between sm:gap-4">
          <div>
            <h3 class="text-lg font-bold text-gray-900 sm:text-xl">
              Descriptive Attention Grabbing Title
            </h3>

            <p class="mt-1 text-xs font-medium text-gray-600">
              By {service.first_name}
              {service.last_name}
            </p>
          </div>

          <div class="hidden sm:block sm:shrink-0">
            <img
              alt=""
              src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1180&q=80"
              class="object-cover rounded-lg shadow-sm size-16"
            />
          </div>
        </div>

        <div class="mt-4">
          <p class="text-sm text-gray-500 text-pretty">
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. At velit
            illum provident a, ipsa maiores deleniti consectetur nobis et eaque.
          </p>
        </div>

        <dl class="flex gap-4 mt-6 sm:gap-6">
          <div class="flex flex-col-reverse">
            <dt class="text-sm font-medium text-gray-600">Published</dt>
            <dd class="text-xs text-gray-500">31st June, 2021</dd>
          </div>

          <div class="flex flex-col-reverse">
            <dt class="text-sm font-medium text-gray-600">Reading time</dt>
            <dd class="text-xs text-gray-500">3 minute</dd>
          </div>
        </dl>
      </div>
    {/each}
  {/if}
</div>
