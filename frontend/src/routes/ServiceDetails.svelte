<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";

  let id;
  let currentUrl;
  let urlArr;

  onMount(() => {
    console.log("ServiceDetails Component Has Mounted");
    currentUrl = window.location.href;
    console.log("Current URL: ", currentUrl);
    urlArr = currentUrl.split("/");
    // console.log(urlArr);
    id = urlArr[urlArr.length - 1];
    console.log("ServiceDetails Component ID: ", id);

    axios
      .get(`/api/Promotion/${id}`)
      .then((axiosResponse) => {
        response.set(axiosResponse);
        console.log(".then() Response Log: ", $response);
      })
      .catch((axiosError) => {
        window.location.href = "/404";
        console.log(".catch() Error Log: ", axiosError);
      });
  });
</script>

{#if $response}
  <!-- ServiceDetails Container -->
  <div
    class="flex flex-col items-center justify-center w-full h-full min-h-screen py-20 m-auto"
  >
    <!-- ServiceDetails Flex Wrap -->
    <div
      class="flex flex-wrap items-center justify-center w-full m-auto md:max-w-6xl"
    >
      <!-- ServiceDetails Left -->
      <div
        class="h-full gap-1 p-4 rounded-none card md:border-r-2 min-h-96 md:border-stone-700 basis-full md:w-fit md:basis-1/2"
      >
        <h1 class="self-center text-3xl card-title">
          {$response.data.results.title}
        </h1>
        <br />
        <div
          class="flex flex-col overflow-hidden overflow-y-scroll min-h-96 h-96 element"
        >
          <div class="self-center w-full h-40 rounded-none skeleton"></div>
          <h2>User: {$response.data.results.user_id}</h2>
          <h3>Service: {$response.data.results.service_id}</h3>
          <hr class="text-stone-500" />
          <p class="self-center w-full text-justify min-h-40">
            {$response.data.results.description}
          </p>
        </div>
        <!-- 
        {
    "created_at": "Sat, 25 May 2024 21:28:42 GMT",
    "description": "Get the latest mix trends and hits. If you are looking to get your clients invested in your business, give them the entertainment they deserve.",
    "id": "2a39db46-59f4-42c2-9c1a-f14d63c4d7d9",
    "pictures": null,
    "price_max": 0,
    "price_min": 0,
    "service_id": 14,
    "title": "Urban DJ",
    "updated_at": "Sat, 25 May 2024 21:28:42 GMT",
    "user_id": "9e85c86b-f7aa-4ace-a538-84c53585f4fe"
}
        -->
      </div>
      <!-- Left -->

      <!-- ServiceDetails Right -->
      <div
        class="flex flex-col h-full gap-1 p-4 rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2"
      >
        <h1 class="self-center text-3xl card-title">Reviews</h1>
        <br />

        <div
          class="flex flex-col gap-2 overflow-hidden overflow-y-scroll min-h-96 h-96"
        >
          {#each [1, 2, 3, 4, 5, 6, 7] as item}
            <div class="p-4 shadow-md bg-stone-200 min-h-40 max-h-96">
              Review Card
            </div>
          {/each}
        </div>
        <!-- 
      {
  "created_at": "Sat, 25 May 2024 21:28:42 GMT",
  "description": "Get the latest mix trends and hits. If you are looking to get your clients invested in your business, give them the entertainment they deserve.",
  "id": "2a39db46-59f4-42c2-9c1a-f14d63c4d7d9",
  "pictures": null,
  "price_max": 0,
  "price_min": 0,
  "service_id": 14,
  "title": "Urban DJ",
  "updated_at": "Sat, 25 May 2024 21:28:42 GMT",
  "user_id": "9e85c86b-f7aa-4ace-a538-84c53585f4fe"
}
      -->
      </div>
      <!-- Right -->
    </div>
    <!-- Flex Wrap -->
  </div>
  <!-- Container -->
{/if}
