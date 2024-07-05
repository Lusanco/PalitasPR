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
      Página no encontrada
    </h1>
    <p class="mt-3 text-xl leading-7 text-secondary">
      Lo sentimos, no pudimos encontrar la página que estás buscando.
    </p>
    <br />
    <div class="flex items-center justify-center">
      <a
        use:link
        href="/"
        class="px-6 shadow-md bg-accent/90 text-primary hover:bg-accent btn hover:shadow-md"
        >Inicio</a
      >
    </div>
  </div>
</div>
