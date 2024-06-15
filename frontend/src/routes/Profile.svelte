<!-- Profile component -->
<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import { writable } from "svelte/store";

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
      <div class="w-full min-h-20 md:w-1/2">
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
              <div
                class="flex flex-col justify-between p-4 rounded-none shadow-md bg-stone-200 card"
              >
                <div class="flex justify-between gap-2">
                  <div>
                    {`${service.first_name} ${service.last_name}`}
                  </div>
                  <div>{`${service.rating}/5.0`}</div>
                </div>
                <br />
                <div
                  class="h-full py-6 text-justify line-clamp-none overflow-ellipsis"
                >
                  {service.description}
                </div>
                <div class="flex justify-between gap-2">
                  <div class="">{service.created_at}</div>
                  <button class="absolute btn right-4 bottom-4">Images</button>
                </div>
              </div>
            {/each}
          </div>
        </div>
      </div>
      <!-- Rightmost -->
      <div class="w-full bg-base-100 max-h-40 md:w-1/2">
        <!-- Gallery -->
        <div
          class="flex flex-col h-full gap-1 p-4 rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2 bg-base-100"
        >
          <h1 class="self-center text-3xl text-stone-700 card-title">
            Gallery
          </h1>
          <br />

          <div
            class="flex flex-col gap-2 overflow-hidden overflow-y-scroll min-h-96 h-96 element"
          >
            {#each [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] as review}
              <div
                class="flex flex-col justify-between p-4 rounded-none shadow-md bg-stone-200 min-h-40 max-h-96 card"
              >
                <div class="flex justify-between gap-2">
                  <div>Full Name</div>
                  <div>3.5/5.0</div>
                </div>
                <br />
                <div class="h-full text-justify line-clamp-6 overflow-ellipsis">
                  Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                  Dolorem cumque iste quia veritatis doloremque cum natus, vero
                  fugiat, vel odio quas placeat similique corrupti quo delectus
                  iure commodi maiores repellendus!
                </div>
                <br />
                <br />
                <div class="flex justify-between gap-2">
                  <div class="">Fecha</div>
                  <button class="absolute btn right-4 bottom-4">Images</button>
                </div>
              </div>
            {/each}
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}
