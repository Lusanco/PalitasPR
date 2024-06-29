<script>
  import { link } from "svelte-routing";
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
      });
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto text-[#1f1f1f] rounded-md sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold">Request Created Successfully</h1>
    <p class="text-sm text-[#1f1f1f]">
      Your request has been successfully submitted.
    </p>
  </div>
  <div class="space-y-2">
    <a
      use:link
      href="/dashboard"
      type="button"
      class="w-full px-8 py-3 font-semibold bg-[#cc2936] rounded-md text-[#f1f1f1]"
    >
      Back to Dashboard
    </a>
  </div>
</div>
