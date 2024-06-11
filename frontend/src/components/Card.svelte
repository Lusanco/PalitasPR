<script>
  import axios from "axios";
  import { state, data, response } from "../scripts/stores";
  import { get } from "svelte/store";
  import { link } from "svelte-routing";

  export let card = {
    url: "Card URL", //{service.promo_id ? `/Promotion/${service.promo_id}` : `/Request/${service.request_id}`}
    id: "Card ID",
    model: "Card Model",
    title: "Card Title",
    first_name: "Card First Name",
    last_name: "Card Last Name",
    created_at: "Card Created At",
    description: "Card Description",
  };

  let url = `/${card.model}/${card.id}`;
  // Function to handle Axios logic
  function axiosLogic() {
    // Update state for loading/error handling
    state.update((s) => ({
      ...s,
      hidden: false,
      loaded: false,
      reload: true,
      error: false,
    }));

    const $data = get(data);
    let axiosData;

    // Make the Axios request
    axios({
      method: "GET",
      url: url,
      //   data: axiosData,
      headers: { "Content-Type": "application/json" },
    })
      .then((axiosResponse) => {
        state.update((s) => ({
          ...s,
          hidden: false,
          loaded: true,
          reload: false,
          error: false,
        }));

        response.set(axiosResponse);

        console.log(".then() Response Log: ", $response);
        // console.log(".then() Data Log: ", axiosData);
        console.log(".then() Card Log: ", card);
        console.log(".then() State Log: ", $state);
      })
      .catch((axiosError) => {
        state.update((s) => ({
          ...s,
          hidden: false,
          loaded: true,
          reload: false,
          error: true,
        }));

        console.log(".catch() Error Log: ", axiosError);
        console.log(".catch() Data Log: ", axiosData);
        console.log(".catch() Card Log: ", card);
        console.log(".catch() State Log: ", $state);
      });
  }

  // Function to handle button click
  export function cardLogic() {
    axiosLogic();
  }
</script>

<div
  class="flex py-2 flex-col gap-4 w-[95%] sm:w-[90%] md:w-[80%] overflow-y-scroll overflow-hidden h-96"
>
  <!-- {#each services as service} -->
  {#each $response.data.results as service}
    <!-- New Card Start -->
    <a
      use:link
      on:click={cardLogic}
      href={`/Promotion/${service.promo_id}`}
      class="w-full h-40 transition-transform duration-200 ease-in-out transform rounded-none shadow-xl card card-side bg-base-100 hover:bg-base-300 active:scale-95"
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
