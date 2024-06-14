<!-- Profile component -->
<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import { writable } from "svelte/store";

  let response1 = writable(null);
  let response2 = writable(null);

  onMount(() => {
    axios
      .get("/api/user/login?af1=jd123@gmail.com&af2=pwd1")
      .then((axiosResponse) => {
        response.set(axiosResponse);
        response1.set(axiosResponse.data);
        console.log(".then() Response Log: ", $response1);
      })
      .catch((axiosError) => {
        console.log(".catch() Error Log: ", axiosError);
      });
    axios
      .get("/api/user/my-profile")
      .then((axiosResponse) => {
        response.set(axiosResponse);
        response2.set(axiosResponse.data);
        console.log(".then() Response Log 2: ", $response2);
      })
      .catch((axiosError) => {
        console.log(".catch() Error Log: ", axiosError);
      });
  });
</script>

{#if $response2}
  <!-- Profile Container -->
  <div class="flex flex-col items-center justify-center min-h-screen py-20">
    <!-- Upper Half -->
    <div class="flex flex-wrap">
      <!-- Profile Cover -->
      <div class="w-full h-96 skeleton">asdf</div>
      <!-- Profile Details -->
      <div></div>
    </div>
    <!-- Bottom Half -->
    <div>
      <!-- Leftmost -->
      <div></div>
      <!-- Rightmost -->
      <div></div>
    </div>
  </div>
{/if}
