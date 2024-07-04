<script>
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

  import { link } from "svelte-routing";
</script>

<div
  class="flex flex-col justify-center h-full min-h-screen px-6 py-20 place-items-center sm:py-32 lg:px-8"
>
  <div class="text-center">
    <p class="font-semibold text-accent text-8xl">404</p>
    <h1
      class="mt-4 text-3xl font-bold tracking-tight text-secondary sm:text-5xl"
    >
      Page not found
    </h1>
    <p class="mt-3 text-xl leading-7 text-accent">
      Sorry, we couldn’t find the page you’re looking for.
    </p>
    <br />
    <div class="flex items-center justify-center">
      <a
        use:link
        href="/"
        class="px-6 bg-accent text-primary hover:text-secondary hover:bg-white btn"
        >Home</a
      >
    </div>
  </div>
</div>
