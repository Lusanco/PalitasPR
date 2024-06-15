<!-- Profile component -->
<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import { writable } from "svelte/store";

  let response1 = writable(null);
  let response2 = writable(null);
  let temp = true;

  onMount(() => {
    console.log("Before axios");
    if (temp) {
      axios
        .get("/api/user/logout")
        .then((axiosResponse) => {
          console.log(".then() Logout Log: ", axiosResponse);
        })
        .catch((axiosError) => {
          console.log(".catch() Error Log: ", axiosError);
        });
    }
    if (temp) {
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
    }
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
  <div class="flex flex-col items-center min-h-screen">
    <div class="flex w-screen max-w-6xl mx-auto">
      <!-- Upper Half -->
      <div class="w-screen">
        <!-- Profile Cover -->
        <div
          class="flex w-screen max-w-6xl mx-auto rounded-none h-60 max-h-96 skeleton"
        ></div>
        <!-- Profile Picture -->
        <div class="flex flex-col items-center w-full">
          <div
            class="w-40 h-40 -mt-20 border-4 rounded-full skeleton border-base-200"
          ></div>
          <h1 class="text-lg font-semibold">Luis Petraco</h1>
        </div>
        <!-- Profile Details -->
        <div class="-mt-24">Luis Petraco</div>
      </div>
      <!-- Bottom Half -->
      <div>
        <!-- Leftmost -->
        <div></div>
        <!-- Rightmost -->
        <div></div>
      </div>
    </div>
  </div>
{/if}
