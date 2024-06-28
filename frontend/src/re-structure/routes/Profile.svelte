<!-- Profile component -->
<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response, userSession } from "../../scripts/stores";
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
</script>

{#if $isLoading}
  <Loading />
{:else if $response2}
  <!-- Profile Container -->
  <div class="flex flex-col items-center min-h-screen">
    <div class="flex w-screen max-w-6xl mx-auto bg-white">
      <!-- Upper Half -->
      <div class="w-screen border-x-0 border-t-0 border-b-2 border-[#cc2936]">
        <!-- Profile Cover -->
        <div
          class="flex border-[#cc2936] border-b-2 border-x-0 border-t-0 w-screen max-w-6xl mx-auto rounded-none h-60 max-h-96 skeleton"
        >
          <img
            src={$coverPic}
            alt="Banner"
            class="object-cover w-full h-full"
          />
        </div>
        <!-- Profile Container -->
        <div class="flex flex-col items-center w-full pb-4 bg-white">
          <!-- Profile Picture -->
          <div
            class="w-40 border-[#cc2936] border-2 h-40 -mt-20 rounded-full skeleton"
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
          class="flex flex-wrap p-4 mt-4 bg-white rounded-none md:-mt-24 md:bg-transparent"
        >
          <div class="flex flex-wrap justify-between w-full px-4">
            <span class="w-full text-center md:text-left md:w-fit"
              >{$response2.results.job_title}</span
            >
            <!-- <span class="w-full text-center md:w-fit md:text-right">
                Placeholder, PR
              </span> -->
          </div>
          <div class="flex flex-wrap justify-between w-full px-4">
            <span class="w-full text-center md:text-left md:w-fit"
              >Completado: {$response2.results.tasks_completed}
              {$response2.results.tasks_completed === 1
                ? "Palita"
                : "Palitas"}</span
            >
            <span class="w-full text-center md:text-right md:w-fit"
              >{$response2.results.rating}/5.0</span
            >
          </div>
        </div>

        <!-- Description -->
        <div class="bg-white rounded-none card">
          <p
            class="h-full text-justify line-clamp-none overflow-ellipsis card-body"
          >
            {$response2.results.bio}
          </p>
        </div>
        <br />
      </div>
      <br />
    </div>
    <br />
    <!-- Bottom Half -->
    <div class="flex flex-wrap w-full h-full max-w-6xl bg-white rounded-md">
      <!-- Leftmost -->
      <div class="w-full min-h-20 md:w-2/3">
        <!-- Services -->
        <div
          class="flex flex-col w-full h-full gap-1 p-4 rounded-none card min-h-96 basis-full md:basis-1/2"
        >
          <h1 class="font-semibold text-3xl text-[#1f1f1f] card-title">
            Servicios
          </h1>
          <br />

          <div
            class="flex flex-col w-full gap-2 overflow-hidden overflow-y-scroll min-h-96 h-96 element"
          >
            {#if $promotions.length === 0}
              <div
                class="font-bold text-xl flex flex-col justify-center items-center text-[#cc2936] text-center h-full w-full"
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
                  class="w-full h-40 transition-all duration-200 ease-in-out transform rounded-none md:rounded-2xl shadow-xl card card-side bg-white hover:bg-[#cc2936] hover:text-white active:scale-95 border-b-4 border-[#cc2936]"
                >
                  <div class="w-1/2 h-40 p-0 px-2 md:w-1/4 md:card-body">
                    <div
                      class="flex flex-col justify-center h-full my-auto text-left"
                    >
                      <h2
                        class="md:text-lg overflow-ellipsis line-clamp-1 md:truncate"
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
                    <p
                      class="h-full text-sm text-justify md:text-base line-clamp-4 overflow-ellipsis"
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
          class="flex flex-col h-full gap-1 p-4 bg-white rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2"
        >
          <h1 class="self-center text-3xl text-[#1f1f1f] card-title">
            Galería
          </h1>
          <br />

          <div
            class="flex flex-wrap justify-center gap-2 overflow-hidden overflow-y-scroll min-h-96 h-96 element"
          >
            {#each $images as image}
              <div
                class="rounded-none min-w-72 min-h-36 max-w-72 max-h-36 skeleton"
              >
                <img src={image} alt="Gallery Pic" />
              </div>
            {/each}
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}
