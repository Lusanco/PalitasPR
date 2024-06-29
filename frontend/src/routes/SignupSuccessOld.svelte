<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import { link } from "svelte-routing";

  onMount(() => {
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
  });
</script>

<div
  class="flex flex-col items-center justify-center max-w-lg min-h-screen py-20 m-auto text-[#1f1f1f]"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-3xl font-bold text-wrap text-[#cc2936]">
      Account created succesfully
    </h1>
    <p class="px-6 mt-3 text-lg text-center">
      To continue, login to your account
    </p>
    <p class="px-6 pt-4 text-sm text-center text-stone-600">
      <button
        type="button"
        class="bg-[#cc2936] text-[#f1f1f1] hover:text-[#1f1f1f] hover:bg-white btn px-6"
      >
        <a use:link href="/login" rel="noopener noreferrer" role="button">
          Login
        </a>
      </button>
    </p>
  </div>
</div>
