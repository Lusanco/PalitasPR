<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import About from "./About.svelte";

  let id;
  let currentUrl;
  let urlArr;

  let offers = [
    { first_name: "Juan", last_name: "Pérez", phone: "123-456-7890", email: "juan.perez@example.com" },
    { first_name: "María", last_name: "González", phone: "987-654-3210", email: "maria.gonzalez@example.com" },
    { first_name: "Carlos", last_name: "Ramírez", phone: "555-555-5555", email: "carlos.ramirez@example.com" },
    { first_name: "Ana", last_name: "Fernández", phone: "444-444-4444", email: "ana.fernandez@example.com" },
  ];

  onMount(() => {
    console.log("OffersDetails Component Has Mounted");
    currentUrl = window.location.href;
    console.log("Current URL: ", currentUrl);
    urlArr = currentUrl.split("/");
    id = urlArr[urlArr.length - 1];
    console.log("OffersDetails Component ID: ", id);

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
  <!-- OffersDetails Container -->
  <div class="flex flex-col items-center justify-center w-full h-full min-h-screen py-20 m-auto">
    <!-- OffersDetails Flex Wrap -->
    <div class="flex flex-wrap items-center justify-center w-full m-auto md:max-w-6xl">
      <!-- OffersDetails Left -->
      <div class="h-full gap-1 p-4 rounded-none card md:border-r-2 min-h-96 md:border-stone-700 basis-full md:w-fit md:basis-1/2">
        <h1 class="self-center text-3xl card-title">
          {$response.data.results.title}
        </h1>
        <br />
        <div class="flex flex-col overflow-hidden overflow-y-scroll min-h-96 h-96 element">
          <div class="self-center w-full h-40 rounded-none skeleton"></div>
          <h2>User: {$response.data.results.user_id}</h2>
          <h3>Service: {$response.data.results.service_id}</h3>
          <hr class="text-stone-500" />
          <p class="self-center w-full text-justify min-h-40">
            {$response.data.results.description}
          </p>
        </div>
      </div>
      <!-- Left -->

      <!-- OffersDetails Right -->
      <div class="flex flex-col h-full gap-1 p-4 rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2">
        <h1 class="self-center text-3xl card-title">Offers</h1>
        <br />

        <div class="flex flex-col gap-2 overflow-y-scroll min-h-96 h-96">
          {#each offers as offer, index}
            <div class="relative p-4 transition-all shadow-md bg-stone-200 min-h-[150px]">
              <div class="flex justify-between">
                <div class="text-lg font-bold">{offer.first_name} {offer.last_name}</div>
                <button class="text-white btn bg-stone-500">Continue</button>
              </div>
              <div class="mb-12">
                <p>Phone: {offer.phone}</p>
                <p>Email: {offer.email}</p>
              </div>
            </div>
          {/each}
        </div>
      </div>
      <!-- Right -->
    </div>
    <!-- Flex Wrap -->
    <div class="flex items-center justify-center w-10/12 gap-4 mx-4 md:w-11/12 md:max-w-6xl">
      <button class="w-1/2 btn bg-stone-200">Edit</button>
      <button class="w-1/2 btn bg-stone-200">Delete</button>
    </div>
  </div>
  <!-- Container -->
{/if}