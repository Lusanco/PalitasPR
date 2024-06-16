<script>
  import Slogan from "../components/Slogan.svelte";
  import townsID from "../scripts/townsID";
  import Loading from "../components/Loading.svelte";
  import Button from "../components/Button.svelte";
  import { state, data, response } from "../scripts/stores";
  import { get } from "svelte/store";
  import { link } from "svelte-routing";

  // Button Prop Variables And Dependencies
  let href = "";
  let image = null;
  let search = "";
  let model = "promotions";
  let town = "all";
  let button = {
    name: "",
    method: "GET",
    url: `/api/explore?search=${search.trim()}&model=${model}&town=${town}`,
    headers: "application/json",
    twcss:
      "btn btn-base border-none rounded-none focus:outline-none text-[#CC2936]",
    misc: { "App Location": "Index Search Component" },
  };
  // Button Prop Variables And Dependencies

  // Define a reference for the Button component
  let buttonRef;

  // Function to handle the "Enter" key press
  function handleKeydown(event) {
    if (event.key === "Enter") {
      // Trigger the button logic from the child component
      buttonRef.buttonLogic();
    }
  }

  // Reactive statement to update button store when misc store changes
  $: {
    button = {
      ...button,
      url: `/api/explore?search=${search.trim()}&model=${model}&town=${town}`,
    };

    // Update the data store with the current misc values
    data.set({ search, model, town });
  }
  $response = get(response);
</script>

<head>
  <title>PalitasPR | Index</title>
</head>

<!-- Index Start -->
<div
  class="flex flex-col items-center justify-center h-full min-h-screen gap-8 py-20"
>
  <Slogan />
  <!-- SearchBar Start -->
  <div
    class="items-center justify-center w-full max-w-md mx-2 border-2 shadow-lg md:mx-auto rounded-2xl border-b-2 border-x-0 border-t-0 border-[#cc2936] bg-white"
  >
    <div
      class="grid grid-cols-2 grid-rows-2 rounded-lg bg-base-100 overflow-clip join"
    >
      <div id="search-bar" class="col-span-2 row-span-1">
        <label for="Search" class="sr-only"> Search </label>
        <input
          type="text"
          id="search"
          bind:value={search}
          on:keydown={handleKeydown}
          placeholder="Search for..."
          class="w-full col-span-2 border-t-0 border-b-2 rounded-none border-x-0 border-[#cc2936] input input-bordered focus:outline-none text-[#cc2936]"
        />
      </div>
      <div id="filters" class="grid grid-cols-3 col-span-2 row-span-1">
        <!-- Model Filter Start -->
        <select
          bind:value={model}
          class="w-full border-none select select-bordered focus:outline-none text-[#cc2936]"
        >
          <option value="promotions">Promotions</option>
          <option value="requests">Requests</option>
        </select>
        <!-- Model Filter End -->
        <!-- Town Filter Start -->
        <select
          bind:value={town}
          class="w-full border-none select select-bordered focus:outline-none text-[#cc2936]"
        >
          <option value="all" disabled>Town</option>
          {#each Object.entries(townsID) as [town, id]}
            <option value={id}>{town}</option>
          {/each}
        </select>
        <!-- Town Filter End -->

        <!-- Bind the Button component to the reference variable -->
        <Button {button} {image} bind:this={buttonRef}>
          <!-- on:results={handleResults} -->
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
    <span class="font-bold text-[#cc2936]">No results found, try again.</span>
  {:else}
    <div
      class="flex py-2 flex-col gap-4 w-[95%] sm:w-[90%] md:w-[80%] overflow-y-scroll overflow-hidden h-96"
    >
      <!-- {#each services as service} -->
      {#each $response.data.results as service}
        <!-- New Card Start -->
        <a
          use:link
          href={service.promo_id
            ? `/service-details/${service.promo_id}`
            : `/request-details/${service.request_id}`}
          class="w-full h-40 transition-transform duration-200 ease-in-out transform rounded-none md:rounded-2xl shadow-xl card card-side bg-white hover:bg-[#cc2936] hover:text-[#f1f1f1] active:scale-95 border-b-4 border-[#cc2936]"
        >
          <div class="w-0 h-full rounded-none md:w-1/4 skeleton"></div>

          <div class="w-1/2 h-40 p-0 md:w-1/4 md:card-body">
            <div class="rounded-none h-1/2 md:w-0 skeleton"></div>
            <div class="p-2 md:mb-6 md:p-0 h-1/2 md:h-full">
              <h2
                class="md:card-title text-md overflow-ellipsis line-clamp-1 md:truncate"
              >
                {service.title}
              </h2>
              <p
                class="text-sm md:-mt-2 overflow-ellipsis line-clamp-1 md:truncate"
              >
                {service.first_name}
                {service.last_name}
              </p>
              <h3 class="hidden text-lg md:block">Published</h3>
              <p class="text-sm md:-mt-2">{service.created_at}</p>
            </div>
          </div>
          <div class="w-1/2 h-40 p-2 md:w-2/4 md:card-body">
            <p class="h-full line-clamp-4 overflow-ellipsis">
              {service.description}
            </p>
          </div>
        </a>
        <!-- New Card End -->
      {/each}
    </div>
  {/if}
</div>
<!-- Index End -->
