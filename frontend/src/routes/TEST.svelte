<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import { data, response } from "../scripts/stores";
  import { writable } from "svelte/store";
  import { link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";

  // Combined store for received and sent data
  let contactData = writable({ received: [], sent: [] });
  let response3 = writable(null);
  let tasks = writable([]);

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

        // Now, set 'tasks' within this 'then' block
        tasks.set(
          $contactData.received.map((item) => Object.entries(item.task)).flat()
        );

        // *************** Finding the Specific Task Key **************
        const targetKey = "promo_id";
        const foundTask = $contactData.received.find((item) =>
          item.task.hasOwnProperty(targetKey)
        );
        const promo_id = foundTask.task[targetKey];

        console.log("RECEIVED =>");
        console.table($contactData.received);
        console.log("RECEIVED.TASK =>");
        $contactData.received.forEach((item) => {
          console.table(item.task);
        });
        console.log("SENT =>");
        console.table($contactData.sent);
        console.log("SENT.TASK =>");
        $contactData.sent.forEach((item) => {
          console.table(item.task);
        });
        return axios.get(`/api/promotion/${promo_id}`);
      })
      .then((axiosResponse3) => {
        response3.set(axiosResponse3.data);
        console.log(axiosResponse3);
      })
      .catch((axiosError) => {
        console.error(".catch() Error Log: ", axiosError);
      });
  });

  let openIndex = null;

  function toggleItem(index) {
    openIndex = openIndex === index ? null : index;
  }
</script>

<div class="flex flex-col items-center w-full min-h-screen px-4 py-20 mx-auto">
  <h1 class="text-3xl font-semibold">Tasks</h1>
  <div class="flex flex-col w-full h-full py-4 mx-auto">
    {#if $contactData && $response3}
      {#each $contactData.received as received, index}
        <div
          class="max-w-6xl px-4 mx-auto w-full bg-white border-b-2 rounded-lg border-[#cc2936] text-[#1f1f1f] flex flex-col transition-all duration-100 hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        >
          <button
            class="flex flex-col w-full gap-1 px-2 py-4 text-lg font-medium text-left rounded-lg md:text-xl focus:outline-none"
            on:click={() => toggleItem(index)}
          >
            <div class="flex flex-wrap justify-between w-full">
              {#if received.task.status === "closed"}
                <span class="bg-[#f1f1f1] p-2 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {:else if received.task.status === "active"}
                <span class="p-2 bg-green-500 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {:else if received.task.status === "pending"}
                <span class="p-2 bg-yellow-500 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {:else if received.task.status === "rejected"}
                <span class="p-2 bg-red-500 rounded-badge text-[#1f1f1f]"
                  >{received.task.status}</span
                >
              {/if}
              {#if received.read === false}
                <span class="w-10 h-10 bg-[#cc2936] rounded-badge animate-ping">
                </span>
              {:else}
                <span class="w-10 h-10 bg-[#f1f1f1] rounded-badge"> </span>
              {/if}
            </div>
            <br />
            <div
              class="flex flex-wrap justify-center w-full md:justify-between"
            >
              <span>
                Name: {received.sender_first_name}
                {received.sender_last_name}
              </span>
              <span>
                {received.updated_at}
              </span>
            </div>
            <div
              class="flex flex-wrap justify-center w-full md:justify-between"
            >
              <span> Add Number to response object </span>
              <span> {received.sender_email} </span>
            </div>
          </button>
          <div
            class={`overflow-hidden transition-all duration-300 ${openIndex === index ? "max-h-screen" : "max-h-0"}`}
          >
            <div class="w-full text-center">Agreement Service</div>

            <div class="w-full text-justify">
              <span>
                {$response3.results.title}:
              </span>
              <span>
                {$response3.results.description}
              </span>
            </div>
            <br />
            <div class="w-full text-center">Agreement Terms</div>
            <div class="px-4 py-2">
              <p>{received.sender_first_name}</p>
            </div>
          </div>
        </div>
      {/each}
    {:else}
      <div
        class="flex flex-col items-center justify-center w-full min-h-screen py-20 m-auto skeleton"
      >
        <Loading />
      </div>
    {/if}
  </div>
</div>
