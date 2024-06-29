<script>
  import { link } from "svelte-routing";
  import { onMount } from "svelte";
  import { userSession } from "../../scripts/stores";
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
  class="flex flex-col items-center justify-center max-w-lg min-h-screen py-20 m-auto text-secondary"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-3xl font-bold text-wrap text-accent">
      Contact Sent Successfully
    </h1>
    <!-- <p class="px-6 mt-3 text-lg text-center">
      To continue, login to your account
    </p> -->
    <p class="px-6 pt-4 text-sm text-center text-secondary">
      <a
        use:link
        href="/"
        rel="noopener noreferrer"
        class="w-full px-6 bg-accent max-w-32 text-primary hover:text-secondary hover:bg-white btn"
        >Search
      </a>
      <a
        use:link
        href="/dashboard"
        rel="noopener noreferrer"
        class="px-6 bg-accent max-w-32 text-primary hover:text-secondary hover:bg-white btn"
      >
        Dashboard
      </a>
    </p>
  </div>
</div>
