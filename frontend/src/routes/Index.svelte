<script>
  import Slogan from "../components/Slogan.svelte";
  import townsID from "../scripts/townsID";
  import Loading from "../components/Loading.svelte";
  import Button from "../components/Button.svelte";
  import { state, data, response, userSession } from "../scripts/stores";
  import { get } from "svelte/store";
  import { Link, link } from "svelte-routing";
  import { onMount } from "svelte";
  import axios from "axios";

  // Button Prop Variables And Dependencies
  let href = "";
  let image = null;
  let search = "";
  let model = "promotions";
  let town = "all";
  let page = 1;
  let totalPages = 1;
  let button = {
    name: "",
    method: "GET",
    url: `/api/explore?search=${search.trim()}&model=${model}&town=${town}&page=${page}`,
    headers: "application/json",
    twcss:
      "border-none rounded-t-none rounded-l-none rounded-r-lg h-full rounded-b-lg focus:outline-none text-accent bg-white hover:text-white hover:bg-accent w-full overflow-hidden",
    misc: { "App Location": "Index Search Component" },
  };
  // Button Prop Variables And Dependencies

  // Define a reference for the Button component
  let buttonRef;

  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
        return axios.get(button.url);
      })
      .catch((userStatusErr) => {
        console.log(userStatusErr);
        return axios.get(button.url);
      })
      .then((res) => {
        response.set(res.data);
        console.log(response);
        totalPages = res.data.total_pages;
      })
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log(userStatusErr);
        console.log($userSession);
      });
  });

  // Function to handle the "Enter" key press
  function handleKeydown(event) {
    if (event.key === "Enter") {
      page = 1;
      button.url = `/api/explore?search=${search.trim()}&model=${model}&town=${town}&page=1`;
      buttonRef.buttonLogic();
    }
  }

  function nextPage() {
    if ($response.data.page < $response.data.total_pages) {
      page += 1;
      button.url = `/api/explore?search=${search.trim()}&model=${model}&town=${town}&page=${page}`;
      buttonRef.buttonLogic();
    }
  }

  function previousPage() {
    if ($response.data.page > 1) {
      page -= 1;
      button.url = `/api/explore?search=${search.trim()}&model=${model}&town=${town}&page=${page}`;
      buttonRef.buttonLogic();
    }
  }
  // Reactive statement to update button store when misc store changes
  $: {
    button = {
      ...button,
      url: `/api/explore?search=${search.trim()}&model=${model}&town=${town}&page=${page}`,
    };

    // Update the data store with the current misc values
    data.set({ search, model, town });
  }
  $response = get(response);
  // totalPages = $response.total_pages || 1;
</script>

<!-- Index Start -->
<div
  class="flex flex-col items-center justify-center h-full max-w-6xl gap-8 px-4 my-20 min-h-fit md:p-0"
>
  <Slogan />
  <!-- SearchBar Start -->
  <div
    class="w-full max-w-md bg-white border-0 border-b-2 rounded-lg shadow-lg border-accent"
  >
    <div class="grid grid-cols-2 grid-rows-2 rounded-lg overflow-clip join">
      <div id="search-bar" class="col-span-2 row-span-1">
        <label for="Search" class="sr-only"> Buscar </label>
        <input
          type="text"
          id="search"
          bind:value={search}
          on:keydown={handleKeydown}
          placeholder="Buscar..."
          class="w-full col-span-2 bg-white border-none rounded-none placeholder:text-secondary placeholder:opacity-60 input input-bordered focus:outline-none text-secondary"
        />
        <div
          class="border-[1px] mx-2 flex justify-center items-center border-neutral"
        ></div>
      </div>
      <div
        id="filters"
        class="grid w-full grid-cols-3 col-span-2 row-span-1 overflow-hidden"
      >
        <!-- Model Filter Start -->
        <select
          bind:value={model}
          class="w-full bg-white border-none select select-bordered focus:outline-none text-secondary"
        >
          <option value="promotions">Promociones</option>
          <option value="requests">Solicitudes</option>
        </select>
        <!-- Model Filter End -->
        <!-- Town Filter Start -->
        <select
          bind:value={town}
          class="w-full bg-white border-none select select-bordered focus:outline-none text-secondary"
        >
          <option value="all" disabled>Pueblos</option>
          {#each Object.entries(townsID) as [town, id]}
            <option value={id}>{town}</option>
          {/each}
        </select>
        <!-- Town Filter End -->

        <!-- Bind the Button component to the reference variable -->
        <Button {button} {image} bind:this={buttonRef}>
          <!-- on:results={handleResults} -->
          <span class="sr-only">Buscar</span>

          <i
            class="flex items-center justify-center w-full h-full m-auto transition-all duration-300 fa-solid fa-magnifying-glass text-accent hover:text-white"
          ></i>
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
    <span class="font-bold text-error"
      >No se encontraron resultados, intenta de nuevo.</span
    >
  {:else}
    <div
      class="flex flex-col w-full gap-4 py-2 overflow-hidden overflow-y-scroll element md:px-12 h-96"
    >
      <!-- {#each services as service} -->
      {#each $response.data.results as service}
        <!-- New Card Start -->
        <Link
          to={service.promo_id
            ? `/service-details/${service.promo_id}`
            : `/request-details/${service.request_id}`}
          class="w-full overflow-hidden transition-all duration-200 ease-in-out transform border-b-2 md:border-b-[3px] rounded-md shadow-md min-h-40 md:rounded-2xl card card-side bg-white hover:bg-accent hover:bg-opacity-10 active:scale-95 border-accent"
        >
          {#if !service.pictures}
            <div
              class="hidden object-cover h-full rounded-none max-h-40 min-w-60 max-w-60 md:block md:w-1/4 skeleton"
            ></div>
          {:else}
            <div
              class="hidden object-cover h-full rounded-none min-w-60 max-w-60 md:block md:w-1/4"
            >
              <img
                class="hidden object-cover h-full rounded-none max-h-40 min-w-60 max-w-60 md:block"
                src={service.pictures}
                alt=""
              />
            </div>
          {/if}

          <div class="w-1/2 h-40 p-0 md:w-1/4 md:card-body">
            {#if !service.pictures}
              <div
                class="object-center rounded-none h-1/2 md:w-0 skeleton"
              ></div>
            {:else}
              <div
                class="object-cover object-center w-full rounded-none h-1/2 md:w-0"
              >
                <img
                  class="object-cover w-full h-full rounded-none md:w-0"
                  src={service.pictures}
                  alt=""
                />
              </div>
            {/if}
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
              <h3 class="hidden text-lg md:block">Publicado</h3>
              <p class="text-sm md:-mt-2">{service.created_at}</p>
            </div>
          </div>
          <div class="w-1/2 h-40 p-2 md:w-2/4 md:card-body">
            <p class="h-full line-clamp-4 overflow-ellipsis">
              {service.description}
            </p>
          </div>
        </Link>
        <!-- New Card End -->
      {/each}
    </div>
    <div class="flex justify-between w-full max-w-md mx-auto">
      <button
        on:click={previousPage}
        class={`btn ${$response.data.page > 1 ? "" : "cursor-not-allowed bg-black/20"}`}
        >Anterior</button
      >
      <button
        on:click={nextPage}
        class={`btn ${$response.data.page < $response.data.total_pages ? "" : "cursor-not-allowed bg-black/20"}`}
        >Siguiente</button
      >
    </div>
  {/if}
</div>
<!-- Index End -->
