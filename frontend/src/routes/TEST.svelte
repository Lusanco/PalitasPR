<!-- <script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { response } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { link } from "svelte-routing";

  let response1 = writable(null);
  let response2 = writable(null);
  let received = writable(null);
  let sent = writable(null);

  onMount(() => {
    axios
      .get("/api/user/login?af1=jd123@gmail.com&af2=pwd1")
      .then((axiosResponse1) => {
        response.set(axiosResponse1);
        response1.set(axiosResponse1.data);
        console.log(".then() Login Log: ", $response1);
        return axios.get("/api/user/contacts");
      })
      .then((axiosResponse2) => {
        response.set(axiosResponse2);
        response2.set(axiosResponse2.data);
        received.set($response2.results.received);
        sent.set($response2.results.sent);
        console.log("RECEIVED => ", $received);
        console.log("");
        console.log("SENT => ", $sent);
        console.log(".then() Contacts Log: ", $response2);
      })
      .catch((axiosError) => {
        console.log(".catch() Error Log: ", axiosError);
      });
  });

  // let openIndex = null;

  // function toggleItem(index) {
  //   openIndex = openIndex === index ? null : index;
  // }

  
</script> -->

<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { data, response } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";

  // Combined store for received and sent data
  let contactData = writable({ received: [], sent: [] });

  onMount(() => {
    axios
      .get("/api/user/login?af1=jd123@gmail.com&af2=pwd1")
      .then((axiosResponse1) => {
        response.set(axiosResponse1);
        console.log(".then() Login Log: ", axiosResponse1.data);
        return axios.get("/api/user/contacts");
      })
      .then((axiosResponse2) => {
        response.set(axiosResponse2);

        // Update the contactData store
        contactData.update((currentData) => ({
          ...currentData,
          received: axiosResponse2.data.results.received,
          sent: axiosResponse2.data.results.sent,
        }));

        console.log("RECEIVED => ", $contactData.received);
        console.log("");
        console.log("SENT => ", $contactData.sent);
      })
      .catch((axiosError) => {
        console.log(".catch() Error Log: ", axiosError);
      });
  });
</script>

{#if $contactData.received.length}
  {#each $contactData.received as received}
    <p>{received.created_at}</p>
    <br />
  {/each}
{:else}
  <div
    class="flex flex-col items-center justify-center w-full min-h-screen py-20 m-auto skeleton"
  >
    <Loading />
  </div>
{/if}
