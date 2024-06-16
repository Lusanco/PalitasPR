<script>
  import axios, { AxiosError } from "axios";
  import { onMount } from "svelte";
  import { writable } from "svelte/store";

  let response = writable({});

  onMount(() => {
    axios
      .post("/api/initial-contact", {
        receiver_id: "b5de504c-1c5b-44d0-ba1e-e3d80d15408f",
        promo_id: "5411c66c-1fbe-4f7e-b1b2-182456edce31",
      })
      .then((axiosResponse) => {
        response.set(axiosResponse);
        console.log("Test Successful: ", $response);
      })
      .catch((axiosErr) => {
        console.log("Test Unsuccesful: ", axiosErr);
      });
  });
</script>

{#if $response}
  <div>
    {$response}
  </div>
{:else}
  <div>No correct response</div>
{/if}
