<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { link } from "svelte-routing";

  const response1 = writable(null);
  const response2 = writable(null);

  let id;
  let currentUrl;
  let urlArr;

  function showModal(event) {}
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
        response1.set(axiosResponse.data);
        console.log(".then() Response Log: ", $response1);
      })
      .catch((axiosError) => {
        window.location.href = "/404";
        console.log(".catch() Error Log: ", axiosError);
      });
    axios
      .get(`/api/promotion/promo_review/${id}`)
      .then((axiosResponse) => {
        response.set(axiosResponse);
        response2.set(axiosResponse.data);
        console.log(".then() Response 2 Log: ", $response2);
      })
      .catch((axiosError) => {
        console.log(".catch() Error Log: ", axiosError);
      });
  });
</script>

<head>
  <title>PalitasPR | Service Details</title>
</head>

{#if $response1 && $response2}
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
          {$response1.results.title}
        </h1>
        <br />
        <div
          class="flex flex-col overflow-hidden overflow-y-scroll min-h-96 h-96 element"
        >
          <div class="self-center w-full h-40 rounded-none skeleton"></div>
          <h2>User: {$response1.results.user_id}</h2>
          <h3>Service: {$response1.results.service_id}</h3>
          <hr class="text-stone-500" />
          <br />
          <p class="self-center w-full text-justify min-h-40">
            {$response1.results.description}
          </p>
        </div>
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
          {#each $response2.results as review}
            <div
              class="flex flex-col justify-between p-4 shadow-md bg-stone-200 card"
            >
              <div class="flex justify-between gap-2">
                <div>
                  {`${review.first_name} ${review.last_name}`}
                </div>
                <div>{`${review.rating}/5.0`}</div>
              </div>
              <br />
              <div
                class="h-full py-6 text-justify line-clamp-none overflow-ellipsis"
              >
                {review.description}
              </div>
              <!-- <br />
              <br /> -->
              <div class="flex justify-between gap-2">
                <div class="">{review.created_at}</div>
                <button class="absolute btn right-4 bottom-4">Images</button>
              </div>
            </div>
          {/each}
        </div>
      </div>
      <!-- Right -->
    </div>
    <!-- Flex Wrap -->
    <div
      class="flex items-center justify-center w-10/12 gap-4 mx-4 md:w-11/12 md:max-w-6xl"
    >
      <a use:link href="/" class="w-1/2 btn bg-stone-200">Cancel</a>
      <button class="w-1/2 btn bg-stone-200">Accept</button>
    </div>
  </div>
  <!-- Container -->
{/if}
