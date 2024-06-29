<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { state, data, response, userSession } from "../../scripts/stores";
  import { writable } from "svelte/store";
  import { Link, link } from "svelte-routing";
  import servicesID from "../../scripts/servicesID";
  import Button from "../components/Button.svelte";
  import { get } from "svelte/store";
  import Profile from "./Profile.svelte";
  import Loading from "../components/Loading.svelte";

  let image = null;
  let button = {
    name: "Send Contact",
    method: "POST",
    url: "/api/initial-contact",
    headers: "application/json",
    twcss:
      "md:w-1/3 w-full btn px-8 py-3 font-semibold bg-accent text-primary rounded hover:bg-white hover:text-secondary hover:shadow-md flex flex-col justify-center items-center",
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

  onMount(() => {
    console.log("ServiceDetails Component Has Mounted");
    currentUrl = window.location.href;
    console.log("Current URL: ", currentUrl);
    urlArr = currentUrl.split("/");
    id = urlArr[urlArr.length - 1];
    console.log("ServiceDetails Component ID: ", id);

    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
        return axios.get(`/api/promotion/${id}`);
      })
      .catch((userStatusErr) => {
        if (userStatusErr.status === 401) {
          window.location.href = "/404";
        }
        return axios.get(`/api/promotion/${id}`);
      })
      .then((promoIDRes) => {
        response1.set(promoIDRes.data);
        profileID.set(promoIDRes.data.results.profile_id);
        console.log(".then() promoIDRes Log: ", promoIDRes.data);
        return axios.get(`/api/promotion/promo_review/${id}`);
      })
      .then((promoReviewRes) => {
        response2.set(promoReviewRes.data);
        console.log(".then() promoReviewRes Log: ", promoReviewRes.data);
        initialContact = {
          receiver_id: get(response1).results.user_id,
          promo_id: get(response1).results.id,
        };
        data.set(initialContact);
        isLoading.set(false);
      })
      .catch((axiosError) => {
        userSession.set(false);
        console.log(".catch() Error Log: ", axiosError);
        isLoading.set(false);
      });
  });
</script>

{#if $isLoading}
  <Loading />
{:else if $response1 && $response2 && $profileID}
  <!-- ServiceDetails Container -->
  <div
    class="flex flex-col items-center justify-center w-full h-full min-h-screen py-20 m-auto bg-primary"
  >
    <!-- ServiceDetails Flex Wrap -->
    <div
      class="flex flex-wrap items-center justify-center w-full h-full m-auto bg-white md:max-w-6xl join min-h-96"
    >
      <!-- ServiceDetails Left -->
      <div
        class="h-full gap-1 p-4 overflow-y-auto bg-white rounded-none element card md:border-r-2 min-h-96 md:border-accent basis-full md:w-fit md:basis-1/2"
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
          <!-- <br> -->
          <hr class="border-accent" />
          <div class="mt-2">
            Pueblos Disponibles: {#each $response1.results.towns as town}
              <span class="mx-1">{town},</span>
            {/each}
          </div>
          <!-- <hr class="border-[#cc2936]" /> -->
          <h3 class="mt-5 text-xl">Descripción</h3>
          <hr class="border-accent" />
          <p class="self-center w-full mt-2 text-justify min-h-40">
            {$response1.results.description}
          </p>
        </div>
        <br />
      </div>
      <!-- Left -->

      <!-- ServiceDetails Right -->
      <div
        class="flex flex-col h-full gap-1 p-4 bg-white rounded-none card min-h-96 basis-full md:w-fit md:basis-1/2"
      >
        <br />
        <h1 class="self-center text-3xl card-title text-secondary">Reviews</h1>
        <br />

        <div
          class="flex flex-col gap-2 overflow-hidden overflow-y-scroll element min-h-96 h-96"
        >
          {#if !$response2.results || $response2.results.length === 0}
            <div
              class="flex flex-col items-center justify-center w-full h-full text-xl font-bold text-center text-accent/60"
            >
              No Reviews Yet
            </div>
          {:else}
            {#each $response2.results as review}
              <div
                class="flex flex-col justify-between p-4 rounded-lg shadow-md bg-primary card"
              >
                <div class="flex justify-between gap-2 text-secondary">
                  <div>
                    {`${review.first_name} ${review.last_name}`}
                  </div>
                  <div>{`${review.rating}/5.0`}</div>
                </div>
                <br />
                <div
                  class="h-full py-6 text-justify line-clamp-none overflow-ellipsis text-[#1f1f1f]"
                >
                  {review.description}
                </div>
                <div class="flex justify-between gap-2 mt-8 text-secondary">
                  <div>{review.created_at}</div>
                  <!-- <button
                      class="absolute btn right-4 bottom-4 bg-[#cc2936] text-white hover:bg-white hover:text-[#1f1f1f] hover:shadow-md"
                      >Images</button
                    > -->
                </div>
              </div>
            {/each}
          {/if}
        </div>
        <br />
        <!-- Flex Wrap -->
        <div
          class="flex items-center justify-center w-full bg-white h-fit md:max-w-6xl"
        >
          <div
            class="flex flex-col items-center justify-center w-10/12 gap-4 mx-4 bg-white md:flex-row md:w-11/12 md:max-w-6xl"
          >
            <Link
              class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
              to="/">Back To Search</Link
            >
            {#if $userSession === false}
              <Link
                class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
                to="/login-to-continue">Go To Profile</Link
              >
              <Link
                class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
                to="/login-to-continue">Send Contact</Link
              >
            {:else}
              <Link
                class="flex flex-col items-center justify-center w-full px-8 py-3 font-semibold rounded md:w-1/3 btn bg-accent text-primary hover:bg-white hover:text-secondary hover:shadow-md"
                to={`/profile/${$profileID}`}>Go To Profile</Link
              >
              <Button {image} {button} />
            {/if}
          </div>
        </div>
      </div>
      <!-- Right -->
    </div>
  </div>
  <!-- Container -->
{/if}
