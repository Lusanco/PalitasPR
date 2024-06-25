<!-- Alfre remember rename/move correctly this component -->
<script>
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";

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
    })
  })
  
  function redirectToLogin() {
    window.location.href = "/login";
  }
</script>

<head>
  <title>PalitasPR | Login To Continue</title>
</head>

<div
  class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto text-teal-800 rounded-md sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold text-[#cc2936]">
      Please Login to Continue
    </h1>
    <p class="text-lg text-[#1f1f1f]">You need to log in to access this page.</p>
  </div>
  <div class="space-y-2">
    <button
      on:click={redirectToLogin}
      type="button"
      class="bg-[#cc2936] text-[#f1f1f1] hover:text-[#1f1f1f] hover:bg-white btn px-6"
    >
      Login
    </button>
  </div>
</div>
