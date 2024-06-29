<!-- Profile component -->
<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response, userSession } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";

  let axStatus = writable(null);
  let response2 = writable(null);
  let response3 = writable([]);
  let images = writable([]);
  let profilePic = writable("");
  let coverPic = writable("");

  let promotions = writable([]);

  let isLoading = writable(true);

  let id;
  let currentUrl;
  let urlArr;

  onMount(() => {
    console.log("Profile Component Has Mounted");

    const currentUrl = window.location.href;
    console.log("Current URL: ", currentUrl);

    const urlArr = currentUrl.split("/");
    const id = urlArr[urlArr.length - 1];
    console.log("Profile ID: ", id);

    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
        console.log(userStatusRes.status);
        return axios.get(`/api/user/profile/${id}`);
      })
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log("userStatusErr: ", userStatusErr.response.status);
        if (userStatusErr.response.status === 401) {
          window.location.href = "/login-to-continue";
        }
        if (userStatusErr.response.status === 404) {
          window.location.href = "/404";
        }
        return axios.get(`/api/user/profile/${id}`);
      })
      .then((profileRes) => {
        response2.set(profileRes.data);
        console.log(".then() Response 2 Log: ", profileRes);

        let galleryImages = profileRes.data.results.gallery || [];
        if (typeof galleryImages === "string") {
          galleryImages = [galleryImages];
        }
        images.set(galleryImages);

        profilePic.set(profileRes.data.results.profile_pic || "");
        coverPic.set(profileRes.data.results.cover_pic || "");

        return axios.get(`/api/dashboard/profile-promotions/${id}`);
      })
      .then((axiosResponse3) => {
        promotions.set(axiosResponse3.data.results);
        console.log(".then() Response 3 Log: ", axiosResponse3);
        console.log("Promotions: ", $promotions);

        isLoading.set(false);
      })
      .catch((axiosError) => {
        console.log(".catch() Error Log: ", axiosError);

        isLoading.set(false);
      });
  });

  // Function to format the rating
  function formatRating(rating) {
    // Convert rating to number if it's a string
    rating = parseFloat(rating);
    // Check if the rating ends with ".0"
    if (rating % 1 === 0) {
      return Math.floor(rating); // Return the integer part
    } else {
      return rating.toFixed(1); // Return the rating formatted to 1 decimal place
    }
  }

  // Function to format date
  function formatDate(dateString) {
    const date = new Date(dateString); // Assuming dateString is in ISO 8601 format
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  }
</script>

{#if $isLoading}
  <Loading />
{:else if $response2}
  <!-- Profile Container -->
  <div class="flex flex-col items-center min-h-screen">
    <div class="flex w-screen max-w-6xl mx-auto bg-primary">
      <!-- Upper Half -->
      <div class="w-screen p-0 md:p-2">
        <!-- Profile Cover -->
        <div class="flex w-full h-60 max-h-96 skeleton">
          <img
            src={$coverPic}
            alt="Banner"
            class="object-cover w-full h-full"
          />
        </div>
        <!-- Profile Container -->
        <div class="bg-white border-b-2 shadow-md rounded-b-md border-accent">
          <div class="flex flex-col items-center w-full pb-4 bg-white">
            <!-- Profile Picture -->
            <div
              class="w-40 h-40 -mt-20 border-4 border-white rounded-full skeleton"
            >
              <img
                src={$profilePic}
                alt="Profile Pic"
                class="w-full h-full bg-cover rounded-full"
              />
            </div>
            <h1 class="py-2 text-xl font-semibold text-[#1f1f1f]">
              {`${$response2.results.first_name} ${$response2.results.last_name}`}
            </h1>
          </div>
          <!-- Profile Details -->
          <div
            class="flex flex-wrap p-4 -mt-8 rounded-none bg-primary md:bg-transparent"
          >
            <div class="flex flex-wrap justify-between w-full px-4">
              <span class="w-full text-lg text-left md:w-fit"
                >{$response2.results.job_title}</span
              >
              <!-- <span class="w-full text-center md:w-fit md:text-right">
                Placeholder, PR
              </span> -->
            </div>
            <div class="flex flex-wrap justify-between w-full px-4">
              <span class="w-full text-left md:w-fit"
                >Completado: {$response2.results.tasks_completed}
                {$response2.results.tasks_completed === 1
                  ? "Palita"
                  : "Palitas"}</span
              >
              <span class="w-full text-right -mt-11 md:-mt-4 md:w-fit"
                ><i class="fa-solid fa-trowel text-accent"></i>
                {formatRating($response2.results.rating)}/5</span
              >
            </div>
          </div>

          <!-- Description -->
          <div class="-mt-8 card">
            <p class="h-full line-clamp-none overflow-ellipsis card-body">
              {$response2.results.bio}
            </p>
          </div>
        </div>
        <br />
      </div>
      <br />
    </div>
    <!-- Bottom Half -->
    <div
      class="flex flex-wrap w-full h-full max-w-6xl -mt-2 rounded-lg bg-primary"
    >
      <!-- Leftmost -->
      <div
        class="w-full border-r-2 border-opacity-25 min-h-20 md:w-2/3 border-neutral"
      >
        <!-- Services -->
        <div
          class="flex flex-col w-full h-full p-5 rounded-none card min-h-96 basis-full"
        >
          <h1 class="text-3xl font-semibold text-secondary card-title">
            Servicios
          </h1>

          <div
            class="flex flex-col w-full gap-2 mt-4 overflow-hidden overflow-y-scroll min-h-96 h-96 element"
          >
            {#if $promotions.length === 0}
              <div
                class="flex flex-col items-center justify-center w-full h-full text-xl font-bold text-center text-error"
              >
                Aún no ha publicado servicios.
              </div>
            {:else}
              {#each $promotions as service}
                <!-- New Card Start -->
                <a
                  use:link
                  href={service.promo_id
                    ? `/service-details/${service.promo_id}`
                    : `/request-details/${service.request_id}`}
                  class="w-full h-40 transition-all duration-75 ease-in-out bg-white border-b-0 shadow-md hover:border-b-2 rounded-xl card card-side active:scale-95 hover:border-accent"
                >
                  <div class="w-1/2 h-40 p-0 px-2 md:w-1/4 md:card-body">
                    <div
                      class="flex flex-col justify-center h-full p-0 my-auto text-left border-r-0 border-opacity-40 md:border-r-2 border-neutral"
                    >
                      <h2
                        class="text-lg font-normal truncate md:font-semibold text-accent overflow-ellipsis line-clamp-1"
                      >
                        {service.first_name}
                        {service.last_name}
                      </h2>
                      <p
                        class="-mt-2 text-sm truncate overflow-ellipsis line-clamp-1"
                      >
                        {service.title}
                      </p>
                      <h2
                        class="text-lg font-normal truncate md:font-semibold text-accent overflow-ellipsis line-clamp-1"
                      >
                        Publicado
                      </h2>
                      <p
                        class="-mt-2 text-sm truncate overflow-ellipsis line-clamp-1"
                      >
                        {formatDate(service.created_at)}
                      </p>
                    </div>
                  </div>
                  <div class="w-1/2 h-40 p-2 md:w-2/4 md:card-body">
                    <p
                      class="h-full text-sm text-balance md:text-base line-clamp-4 overflow-ellipsis"
                    >
                      {service.description}
                    </p>
                  </div>
                </a>
                <!-- New Card End -->
              {/each}
            {/if}
          </div>
        </div>
      </div>
      <!-- Rightmost -->
      <div class="w-full min-h-20 md:w-1/3">
        <!-- Gallery -->
        <div
          class="flex flex-col h-full gap-1 p-4 rounded-none bg-primary card min-h-96 basis-full md:w-fit md:basis-1/2"
        >
          <h1 class="self-center mb-2 text-3xl text-secondary card-title">
            Galería
          </h1>

          <div
            class="flex flex-wrap justify-center overflow-hidden overflow-y-scroll min-h-96 h-96 element"
          >
            {#each $images as image}
              <div class="mt-2 min-w-72 min-h-36 max-w-72 max-h-36 skeleton">
                <img
                  src={image}
                  alt="Gallery Pic"
                  class="object-cover transition-transform duration-100 ease-out rounded-md hover:scale-105 min-w-72 min-h-36 max-w-72 max-h-36"
                />
              </div>
            {/each}
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}
