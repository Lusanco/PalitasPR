<script>
  import { link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";
  import Button from "../components/Button.svelte";
  import { state, data, response, userSession } from "../scripts/stores";
  import { get } from "svelte/store";
  import { onMount } from "svelte";
  import axios from "axios";

  // Button Prop Variables And Dependencies
  let image = null;
  let af1 = null;
  let af2 = null;
  let errorMessage;
  let button = {
    name: "Iniciar Sesión",
    method: "GET",
    url: `/api/user/login?af1=${af1}&af2=${af2}`,
    headers: "application/json",
    twcss:
      "shadow-md text-[#f1f1f1] btn bg-accent hover:text-primary hover:bg-accent hover:scale-105 focus:outline-none",
    misc: { "App Location": "Login" },
  };
  // Button Prop Variables And Dependencies

  // Define a reference for the Button component
  let buttonRef;

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

  // Function to handle the "Enter" key press
  function handleKeydown(event) {
    if (event.key === "Enter") {
      // Trigger the button logic from the child component
      if (typeof af1 === "undefined" || typeof af2 === "undefined") {
        af1 = null;
        af2 = null;
      }

      buttonRef.buttonLogic();
    }
  }

  // Reactive statement to update button store when misc store changes
  $: {
    button = {
      ...button,
      url: `/api/user/login?af1=${af1}&af2=${af2}`,
    };

    // Update the data store with the current misc values
    data.set({ af1, af2 });
  }

  $response = get(response);

  // Function to handle the Axios response and redirect on successful login
  $: {
    if ($response && $response.status === 200) {
      window.location.href = "/";
    }
  }

  onMount(() => {
    errorMessage = ""; // Clear any previous error messages on component mount
  });
</script>

<div class="flex flex-col items-center justify-center h-full min-h-screen">
  <div class="flex flex-col gap-4">
    <div class="-mb-2 text-center">
      <h1 class="text-5xl font-bold text-accent">Iniciar Sesión</h1>
      <p class="text-md text-secondary">
        Inicia sesión para acceder a tu cuenta
      </p>
      <br />
    </div>
    <label
      class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg border-neutral"
    >
      <p class="w-12 text-center">Correo</p>
      <input
        bind:value={af1}
        on:keydown={handleKeydown}
        type="email"
        class="ml-4 border-none focus:ring-0 grow text-secondary"
        placeholder="user@email.com"
      />
    </label>
    <label
      class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg border-neutral"
    >
      <p class="w-12 text-center">Contraseña</p>
      <input
        bind:value={af2}
        on:keydown={handleKeydown}
        type="password"
        class="ml-4 border-none focus:ring-0 grow text-secondary"
        placeholder="********"
      />
    </label>
    <a
      use:link
      href="/forgot-password"
      rel="noopener noreferrer"
      class="self-end pr-2 -mt-4 text-sm link link-hover text-accent"
      >¿Olvidaste tu contraseña?</a
    >
    <Button bind:this={buttonRef} {image} {button}></Button>
    <p class="pr-2 -mt-3 text-sm text-right">
      ¿No tienes una cuenta aún? <a
        use:link
        class="link link-hover text-accent"
        rel="noopener noreferrer"
        href="/signup">Regístrate</a
      >.
    </p>
    {#if $state.hidden === true}
      <div class="hidden"></div>
    {:else if (!$state.hidden && !$state.loaded) || $state.reload}
      <Loading />
    {:else if $state.error}
      <div class="w-full mx-auto font-bold text-center text-error">
        Incorrect email or password, try again.
      </div>
    {/if}
  </div>
</div>
