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
        console.log(".catch() Error Log: ", axiosError);
      });
  });
</script>

{#if $response.data.results.id}
  <h1 class="text-red-500 bg-black text-7xl">PLACEHOLDER</h1>
{:else}
  ID NOT PASSED
{/if}
