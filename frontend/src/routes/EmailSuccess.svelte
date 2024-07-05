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
  class="flex flex-col items-center justify-center max-w-lg min-h-screen py-20 m-auto bg-primary"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-3xl font-bold text-wrap text-accent">
      Cuenta confirmada con éxito
    </h1>
    <p class="px-6 mt-3 text-lg text-center text-secondary">
      Para continuar, inicie sesión en su cuenta
    </p>
    <p class="px-6 pt-4 text-sm text-center text-secondary">
      <button
        type="button"
        class="px-6 bg-accent/90 text-primary hover:bg-accent btn"
      >
        <a use:link href="/login" rel="noopener noreferrer" role="button">
          Login
        </a>
      </button>
    </p>
  </div>
</div>
