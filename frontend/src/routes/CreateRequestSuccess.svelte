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
  class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto rounded-md text-accent sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold">Solicitud creada correctamente</h1>
    <p class="text-sm text-secondary">Tu solicitud a sido sometida exito.</p>
  </div>
  <div class="flex justify-center px-4">
    <a
      use:link
      href="/"
      rel="noopener noreferrer"
      class="w-full px-6 mx-1 bg-accent max-w-32 text-primary hover:text-secondary hover:bg-white btn"
      >Buscar
    </a>
    <a
      use:link
      href="/dashboard"
      rel="noopener noreferrer"
      class="w-full px-6 mx-1 bg-accent max-w-32 text-primary hover:text-secondary hover:bg-white btn"
    >
      Tablero
    </a>
  </div>
</div>
