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
    class="flex flex-col items-center justify-center w-full m-auto bg-red-500"
  >
    <!-- ServiceDetails Flex Wrap -->
    <div
      class="flex flex-wrap items-center justify-center w-full m-auto md:max-w-7xl"
    >
      <!-- ServiceDetails Left -->
      <div class="bg-blue-500 basis-full md:w-fit md:basis-1/2">I am blue</div>
      <!-- Left -->

      <!-- ServiceDetails Right -->
      <div class="bg-yellow-500 basis-full md:w-fit md:basis-1/2">
        I am yellow
      </div>
      <!-- Right -->
    </div>
    <!-- Flex Wrap -->
  </div>
  <!-- Container -->
{/if}
