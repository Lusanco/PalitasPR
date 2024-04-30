<script>
  import axios from "axios";
  import LogoSlogan from "./LogoSlogan.svelte";
  import SearchBar from "./SearchBar.svelte";

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
        console.log(services);
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

<div class="flex flex-col items-center justify-center h-full gap-8">
  <LogoSlogan />
  <div class="items-center justify-center w-full max-w-md">
    <SearchBar input={searchInput} search={handleSearch} />
  </div>
  {#if switcher === false}
    <div class="hidden"></div>
  {:else}
    <div
      class="flex py-2 flex-col min-h-20 max-h-[50%] gap-4 rounded-md w-[95%] sm:w-[90%] md:w-[80%] overflow-y-scroll bg-teal-50"
    >
      {#each services as service}
        <!-- <div class="w-full p-2 border-teal-800 rounded-md border-1">
              {service.first_name}
              {service.last_name}
              {service.service}
              {#each service.towns as town, index}
                {town}{index < service.towns.length - 1 ? ", " : ""}
              {/each}
            </div> -->
        <!-- {service.name} -->
        <div
          class="relative block w-full p-4 border border-teal-100 rounded-lg shadow-lg sm:p-6 lg:p-8"
        >
          <span
            class="absolute inset-x-0 bottom-0 h-2 bg-gradient-to-r from-teal-200 via-teal-400 to-teal-600"
          ></span>

          <div class="sm:flex sm:justify-between sm:gap-4">
            <div>
              <h3 class="text-lg font-bold text-gray-900 sm:text-xl">
                {service.title}
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

          <div class="">
            <p class="text-sm text-gray-500 text-pretty">
              {service.description}
            </p>
          </div>

          <dl class="flex gap-4 sm:gap-6">
            <div class="flex flex-col-reverse">
              <dt class="text-sm font-medium text-gray-600">Published</dt>
              <dd class="text-xs text-gray-500">{service.created_at}</dd>
            </div>

            <div class="flex flex-col-reverse">
              <dt class="text-sm font-medium text-gray-600">Rated</dt>
              <dd class="text-xs text-gray-500">{service.rating}/5</dd>
            </div>
          </dl>
        </div>
      {/each}
    </div>
  {/if}
</div>
