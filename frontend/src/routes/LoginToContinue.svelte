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
      });
  });

  function redirectToLogin() {
    window.location.href = "/login";
  }
</script>

<div
  class="flex flex-col items-center justify-center h-full max-w-xl min-h-screen p-6 m-auto sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="text-4xl font-bold text-accent">Para Accesar Este Contenido</h1>
    <p class="mt-1 text-lg text-secondary">Inicie sesión para continuar</p>
  </div>
  <div class="">
    <button
      on:click={redirectToLogin}
      type="button"
      class="px-6 bg-accent text-primary hover:text-text-secondary hover:bg-green-900 btn"
    >
      Iniciar Sesión
    </button>
  </div>
</div>
