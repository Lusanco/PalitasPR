<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { state, data, response, userSession } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { Link, link } from "svelte-routing";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";
  import { get } from "svelte/store";
  import Loading from "../components/Loading.svelte";

  let image = null;
  let button = {
    name: "Enviar contacto",
    method: "POST",
    url: "/api/initial-contact",
    headers: "application/json",
    twcss:
      "md:w-1/3 w-full btn px-8 py-3 font-semibold bg-accent text-primary rounded hover:bg-white hover:text-secondary hover:shadow-md shadow-md",
    misc: { "App Location": "Service Details" },
  };

  const response1 = writable(null);
  const response2 = writable(null);
  let profileID = writable("");

  let id;
  let currentUrl;
  let urlArr;
  let initialContact;

  let isLoading = writable(true);

  function showModal(event) {}
  onMount(() => {
    // Fetch user status
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
      })
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log(userStatusErr);
        console.log($userSession);
      });

    // Get current URL and split to find ID
    console.log("RequestDetails Component Has Mounted");
    currentUrl = window.location.href;
    console.log("Current URL: ", currentUrl);
    urlArr = currentUrl.split("/");
    id = urlArr[urlArr.length - 1];
    console.log("RequestDetails Component ID: ", id);

    // Fetch request details and reviews
    axios
      .get(`/api/request/${id}`)
      .then((axiosResponse1) => {
        response.set(axiosResponse1);
        response1.set(axiosResponse1.data);
        console.log(".then() Response Log: ", $response1);
        return axios.get(`/api/request/request_review/${id}`);
      })
      .then((axiosResponse2) => {
        response.set(axiosResponse2);
        response2.set(axiosResponse2.data);
        console.log(".then() Response 2 Log: ", $response2);
        initialContact = {
          receiver_id: $response1.results.user_id,
          request_id: $response1.results.id,
        };
        data.set(initialContact);
        profileID.set($response1.results.profile_id);

        isLoading.set(false);
      })
      .catch((axiosError) => {
        userSession.set(false);
        window.location.href = "/404";
        console.log(".catch() Error Log: ", axiosError);

        isLoading.set(false);
      });
  });
</script>

{#if $isLoading}
  <Loading />
{:else if $response1 && $response2}
  <div
    class="flex flex-col items-center justify-center w-full h-full min-h-screen py-20 m-auto bg-primary"
  >
    <div
      class="flex flex-wrap items-center justify-center w-full h-full m-auto bg-white md:max-w-3xl lg:max-w-4xl join min-h-96"
    >
      <div
        class="h-full gap-1 p-4 overflow-y-auto bg-white rounded-none element card min-h-96 basis-full md:w-1/2"
      >
        <br />
        <h1 class="self-center text-3xl card-title text-secondary">
          {$response1.results.title}
        </h1>
        <br />
        <div
          class="flex flex-col overflow-hidden overflow-y-scroll min-h-96 h-96 element text-secondary"
        >
          {#if !$response1.results.pictures || $response1.results.pictures.length === 0}
            <div
              class="self-center w-full h-40 rounded-none skeleton min-h-40"
            ></div>
          {:else}
            <div
              class="self-center object-cover w-full h-40 rounded-none max-h-40 min-h-40"
            >
              <img
                class="self-center object-cover w-full h-40 rounded-none max-h-40"
                src={$response1.results.pictures[0]}
                alt=""
              />
            </div>
          {/if}
          <br />
          <div class="flex flex-wrap justify-between text-xl">
            <span>
              {$response1.results.first_name}
              {$response1.results.last_name}
            </span>
            <span>{Object.keys(servicesID)[$response1.results.service_id]}</span
            >
          </div>
          <hr class="border-accent" />
          <div class="flex-grow mt-2">
            Pueblos Disponibles: {#each $response1.results.towns as town}
              <span class="mx-1">{town}</span>
            {/each}
          </div>
          <h3 class="mt-5 text-xl">Descripción</h3>
          <hr class="border-accent" />
          <p class="self-center w-full mt-2 text-justify min-h-40">
            {$response1.results.description}
          </p>
        </div>
        <br />
        <div
          class="flex items-center justify-center w-full bg-white h-fit md:max-w-6xl"
        >
          <div
            class="flex flex-col items-center justify-center w-10/12 gap-4 mx-4 bg-white md:flex-row md:w-11/12 md:max-w-6xl"
          >
            <Link
              class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded shadow-md md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
              to="/">Inicio</Link
            >
            {#if $userSession === false}
              <Link
                class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded shadow-md md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
                to="/login-to-continue">Ir a perfil</Link
              >
              <Link
                class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded shadow-md md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
                to="/login-to-continue">Enviar contacto</Link
              >
            {:else}
              <Link
                class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded shadow-md md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
                to={`/profile/${$profileID}`}>Ir a perfil</Link
              >
              <Button {image} {button} />
            {/if}
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}
