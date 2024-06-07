<script>
    import Slogan from "../components/Slogan.svelte";
    import townsID from "../scripts/townsID";
    import Loading from "../components/Loading.svelte";
    import Button from "../components/Button.svelte";
    import { state } from "../scripts/stateStores";
  
    let services = [];
    let errorMessage = "";
  
    let axiosDATA;
    let miscDATA = {
      search: "",
      model: "promotions",
      town: "all",
    };
    let buttonDATA = {
      name: "",
      method: "GET",
      url: `/api/explore?search=${miscDATA.search.trim()}&model=${miscDATA.model}&town=${miscDATA.town}`,
      headers: { "Content-Type": "application/json" },
      twcss:
        "w-full h-full font-bold text-teal-100 bg-teal-800 hover:bg-teal-700 hover:text-teal-300",
    };
  
    // Define a reference for the Button component
    let buttonRef;
  
    // Function to handle the "Enter" key press
    function handleKeydown(event) {
      if (event.key === "Enter") {
        // Trigger the button logic from the child component
        buttonRef.buttonLogic();
      }
    }
  
    function handleResults(event) {
      const { success, data, error, state: newState } = event.detail;
      services = data;
      state.set(newState);
  
      if (!success) {
        errorMessage = error?.message || "An error occurred";
      }
    }
  
    // Update buttonDATA when miscDATA changes
    $: buttonDATA = {
      ...buttonDATA,
      url: `/api/explore?search=${miscDATA.search.trim()}&model=${miscDATA.model}&town=${miscDATA.town}`,
    };
  </script>
  
  <!-- Index Start -->
  <div
    class="flex flex-col items-center justify-center h-full min-h-screen gap-8"
  >
    <Slogan />
    <!-- SearchBar Start -->
    <div class="items-center justify-center w-full max-w-md mx-2 md:mx-auto">
      <div class="grid grid-cols-2 grid-rows-2 rounded-lg bg-base-100 overflow-clip">
        <div id="search-bar" class="col-span-2 row-span-1">
          <label for="Search" class="sr-only"> Search </label>
          <input
            type="text"
            id="search"
            bind:value={miscDATA.search}
            on:keydown={handleKeydown}
            placeholder="Search for..."
            class="w-full col-span-2 input input-bordered"
          />
          <!-- on:keydown={handleKeydown} -->
        </div>
        <div id="filters" class="grid grid-cols-3 col-span-2 row-span-1">
          <!-- Model Filter Start -->
          <select
            bind:value={miscDATA.model}
            class="w-full select select-bordered"
          >
            <option value="promotions">Promotions</option>
            <option value="requests">Requests</option>
          </select>
          <!-- Model Filter End -->
          <!-- Town Filter Start -->
          <select
            bind:value={miscDATA.town}
            class="w-full select select-bordered"
          >
            <option value="all" disabled>Town</option>
            {#each Object.entries(townsID) as [town, id]}
              <option value={id}>{town}</option>
            {/each}
          </select>
          <!-- Town Filter End -->
  
          <!-- Bind the Button component to the reference variable -->
          <Button
            bind:this={buttonRef}
            {axiosDATA}
            {buttonDATA}
            {miscDATA}
            on:results={handleResults}
          >
            <span class="sr-only">Search</span>
  
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-5 h-5 m-auto"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
              />
            </svg>
          </Button>
        </div>
      </div>
      <!-- SearchBar End -->
    </div>
    {#if $state.hidden}
      <div class="hidden"></div>
    {:else if (!$state.hidden && !$state.loaded) || $state.reload}
      <Loading />
    {:else if $state.error}
      <span class="font-bold text-error">No results found, try again.</span>
    {:else}
      <div
        class="flex py-2 flex-col gap-4 rounded-md w-[95%] sm:w-[90%] md:w-[80%] overflow-y-scroll overflow-hidden h-96 bg-base-200"
      >
        {#each services as service}
          <a href="##">
            <div
              class="relative block w-full p-4 border rounded-lg shadow-lg border-base-300 sm:p-6 lg:p-8"
            >
              <span
                class="absolute inset-x-0 bottom-0 h-2 bg-gradient-to-r from-teal-200 via-teal-400 to-teal-600"
              ></span>
  
              <div class="sm:flex sm:justify-between sm:gap-4">
                <div>
                  <h3 class="text-lg font-bold text-primary sm:text-xl">
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
                <p class="text-sm text-neutral text-pretty">
                  {service.description}
                </p>
              </div>
  
              <dl class="flex gap-4 sm:gap-6">
                <div class="flex flex-col-reverse">
                  <dt class="text-sm font-medium text-neutral-content">Published</dt>
                  <dd class="text-xs text-neutral-content">{service.created_at}</dd>
                </div>
  
                <div class="flex flex-col-reverse">
                  <dt class="text-sm font-medium text-neutral-content">Rated</dt>
                  <dd class="text-xs text-neutral-content">{service.rating}/5</dd>
                </div>
              </dl>
            </div>
          </a>
        {/each}
      </div>
    {/if}
  </div>
  <!-- Index End -->
  