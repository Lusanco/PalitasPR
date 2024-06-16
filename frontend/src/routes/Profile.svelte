<!-- Profile component -->
<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { link } from "svelte-routing";

  let response1 = writable(null);
  let response2 = writable(null);
  let response3 = writable([]);

  onMount(() => {
    console.log("Before axios");

    axios
      .get("/api/user/logout")
      .then((axiosResponse) => {
        console.log(".then() Logout Log: ", axiosResponse);
        return axios.get("/api/user/login?af1=jd123@gmail.com&af2=pwd1");
      })
      .then((axiosResponse) => {
        response.set(axiosResponse);
        response1.set(axiosResponse.data);
        console.log(".then() Login Log: ", $response1);
        return axios.get("/api/user/my-profile");
      })
      .then((axiosResponse2) => {
        response.set(axiosResponse2);
        response2.set(axiosResponse2.data);
        console.log(".then() Response 2 Log: ", $response2);
        return axios.get("/api/dashboard/promotion-request");
      })
      .then((axiosResponse3) => {
        response.set(axiosResponse3);
        response3.set(axiosResponse3.data.results[0] || []);
        console.log(".then() Response 3 Log: ", $response3);
      })
      .catch((axiosError) => {
        console.log(".catch() Error Log: ", axiosError);
      });
  });
</script>

<head>
  <title>PalitasPR | Profile</title>
</head>

{#if $response2}
  <!-- Profile Container -->
  <div class="flex flex-col items-center min-h-screen">
    <div class="flex w-screen max-w-6xl mx-auto bg-base-100">
      <!-- Upper Half -->
      <div class="w-screen">
        <!-- Profile Cover -->
        <div
          class="flex w-screen max-w-6xl mx-auto rounded-none h-60 max-h-96 skeleton"
        ></div>
        <!-- Profile Container -->
        <div class="flex flex-col items-center w-full pb-4 bg-base-100">
          <!-- Profile Picture -->
          <div
            class="w-40 h-40 -mt-20 border-4 rounded-full skeleton border-base-200"
          ></div>
          <h1 class="py-2 text-xl font-semibold text-stone-700">
            {`${$response2.results.first_name} ${$response2.results.last_name}`}
          </h1>
        </div>
        <!-- Profile Details -->
        <div
          class="flex flex-wrap p-4 mt-4 rounded-none md:-mt-24 bg-base-100 md:bg-transparent"
        >
          <div class="flex flex-wrap justify-between w-full px-4">
            <span class="w-full text-center md:text-left md:w-fit"
              >{$response2.results.job_title}</span
            >
            <span class="w-full text-center md:w-fit md:text-right">
              Placeholder, PR
            </span>
          </div>
          <div class="flex flex-wrap justify-between w-full px-4">
            <span class="w-full text-center md:text-left md:w-fit"
              >Completed: {$response2.results.tasks_completed}
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
        <div class="rounded-none card bg-base-100">
          <p
            class="h-full text-justify line-clamp-none overflow-ellipsis card-body"
          >
            {$response2.results.bio}
          </p>
        </div>
        <br />
      </div>
    </div>
    <!-- Bottom Half -->
    <div class="flex flex-wrap w-full h-full max-w-6xl bg-base-100">
      <!-- Leftmost -->
      <div class="w-full min-h-20 md:w-2/3">
        <!-- Services -->
        <div
          class="flex flex-col h-full gap-1 p-4 rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2"
        >
          <h1 class="self-center text-3xl text-stone-700 card-title">
            Services
          </h1>
          <br />

          <div
            class="flex flex-col gap-2 overflow-hidden overflow-y-scroll min-h-96 h-96 element"
          >
            {#each $response3 as service}
              <!-- New Card Start -->
              <a
                use:link
                href={service.promo_id
                  ? `/service-details/${service.promo_id}`
                  : `/request-details/${service.request_id}`}
                class="w-full h-40 transition-all duration-200 ease-in-out transform rounded-none md:rounded-2xl shadow-xl card card-side bg-white hover:bg-[#cc2936] hover:text-[#f1f1f1] active:scale-95 border-b-4 border-[#cc2936]"
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
          </div>
        </div>
      </div>
      <!-- Rightmost -->
      <div class="w-full min-h-20 md:w-1/3">
        <!-- Gallery -->
        <div
          class="flex flex-col h-full gap-1 p-4 rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2 bg-base-100"
        >
          <h1 class="self-center text-3xl text-stone-700 card-title">
            Gallery
          </h1>
          <br />

          <div
            class="flex flex-wrap justify-center gap-2 overflow-hidden overflow-y-scroll min-h-96 h-96 element"
          >
            {#each [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] as image}
              <div
                class="rounded-none min-w-72 min-h-36 max-w-72 max-h-36 skeleton"
              ></div>
            {/each}
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}
