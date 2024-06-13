<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import About from "./About.svelte";

  let id;
  let currentUrl;
  let urlArr;

  let reviews = [
    { user_id: "User ID", title: "Excelente Servicio", review: "Reseña corta 1", rating: 4, date: "2024-06-13" },
    { user_id: "User ID", title: "Buen Servicio", review: "Reseña corta 2", rating: 5, date: "2024-06-12" },
    { user_id: "User ID", title: "Mal Servicio", review: "Reseña muy larga que debería mostrar un botón de 'ver más' para expandir y mostrar todo el contenido de la reseña. Esta es una reseña de ejemplo que es lo suficientemente larga como para necesitar truncamiento. Reseña muy larga que debería mostrar un botón de 'ver más' Reseña muy larga que debería mostrar un botón de 'ver más'", rating: 3, date: "2024-06-11" },
    { user_id: "User ID", title: "Excelente Servicio", review: "Reseña corta 4", rating: 4, date: "2024-06-10" },
    { user_id: "User ID", title: "Buen Servicio", review: "Reseña corta 5", rating: 5, date: "2024-06-09" },
    { user_id: "User ID", title: "Mal Servicio", review: "Reseña corta 6", rating: 2, date: "2024-06-08" },
    { user_id: "User ID", title: "Excelente Servicio", review: "Reseña corta 7", rating: 4, date: "2024-06-07" },
  ];

  let expandedReviews = [];

  function toggleReview(index) {
    if (expandedReviews.includes(index)) {
      expandedReviews = expandedReviews.filter(i => i !== index);
    } else {
      expandedReviews = [...expandedReviews, index];
    }
  }

  onMount(() => {
    console.log("ServiceDetails Component Has Mounted");
    currentUrl = window.location.href;
    console.log("Current URL: ", currentUrl);
    urlArr = currentUrl.split("/");
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
  <div class="flex flex-col items-center justify-center w-full h-full min-h-screen py-20 m-auto">
    <!-- ServiceDetails Flex Wrap -->
    <div class="flex flex-wrap items-center justify-center w-full m-auto md:max-w-6xl">
      <!-- ServiceDetails Left -->
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

      <!-- ServiceDetails Right -->
      <div class="flex flex-col h-full gap-1 p-4 rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2">
        <h1 class="self-center text-3xl card-title">Reviews</h1>
        <br />

        <div class="flex flex-col gap-2 overflow-y-scroll min-h-96 h-96">
          {#each reviews as review, index}
            <div class="relative p-4 transition-all shadow-md bg-stone-200" class:min-h-auto={expandedReviews.includes(index)} class:min-h-[150px]={!expandedReviews.includes(index)}>
              <div class="flex justify-between">
                <div class="text-lg font-bold">{review.title}</div>
                <div>{review.date}</div>
              </div>
              <div class="mb-12">
                {#if review.review.length > 250}
                  {#if expandedReviews.includes(index)}
                    {review.review}
                    <button class="mt-2 cursor-pointer text-stone-500" on:click={() => toggleReview(index)}> Show Less</button>
                  {:else}
                    {review.review.slice(0, 180)}...
                    <button class="mt-2 cursor-pointer text-stone-500" on:click={() => toggleReview(index)}> Show More</button>
                  {/if}
                {:else}
                  {review.review}
                {/if}
              </div>
              <div class="absolute text-sm bottom-2 left-2 text-stone-500">{review.user_id}</div>
              <div class="absolute text-sm bottom-2 right-2 text-stone-500">Rating: {review.rating}</div>
            </div>
          {/each}
        </div>
      </div>
      <!-- Right -->
    </div>
    <!-- Flex Wrap -->
    <div class="flex items-center justify-center w-10/12 gap-4 mx-4 md:w-11/12 md:max-w-6xl">
      <button class="w-1/2 btn bg-stone-200">Cancel</button>
      <button class="w-1/2 btn bg-stone-200">Accept</button>
    </div>
  </div>
  <!-- Container -->
{/if}
