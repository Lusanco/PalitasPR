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
  let first_name;
  let last_name;
  let password;
  let confirmPassword;
  let email;
  let phone;
  let af1 = null;
  let af2 = null;
  let errorMessage;
  let button = {
    name: "Crear cuenta",
    method: "POST",
    url: "/api/user/signup",
    headers: "application/json",
    twcss:
      "shadow-md text-white btn bg-accent hover:bg-white hover:text-secondary w-full max-w-96 flex justify-center items-center flex m-auto",
    misc: { "App Location": "Signup" },
  };

  // Reactive block to update $data
  $: {
    $data = {
      first_name,
      last_name,
      email,
      phone,
      password,
    };
  }

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

  // Function to validate the password fields
  function validatePasswords() {
    if (password !== confirmPassword) {
      errorMessage = "Las contraseñas no coinciden.";
      password = null;
      confirmPassword = null;
    } else {
      password = password;
      confirmPassword = confirmPassword;
    }
  }

  data.set($data);
  // Define a reference for the Button component
  let buttonRef;

  // Function to handle the "Enter" key press
  function handleKeydown(event) {
    if (event.key === "Enter") {
      validatePasswords();
      if (errorMessage) {
        return; // Exit early if passwords do not match
      }
      // Trigger the button logic from the child component
      buttonRef.buttonLogic();
    }
  }

  // Function to handle the phone number input
  function handlePhoneNum(event) {
    let input = event.target.value.replace(/[^0-9]/g, ""); // Remove non-numeric characters

    if (input.length > 10) {
      input = input.slice(0, 10); // Restrict length to 10 digits
    }

    let formattedValue = "";
    if (input.length > 0) {
      formattedValue += input.substring(0, 3);
    }
    if (input.length > 3) {
      formattedValue += "-" + input.substring(3, 6);
    }
    if (input.length > 6) {
      formattedValue += "-" + input.substring(6, 10);
    }

    phone = formattedValue;
  }

  // Reactive statement to update button store when misc store changes
  $: {
    button = {
      ...button,
    };
  }

  $response = get(response);

  // Function to handle the Axios response and redirect on successful login
  $: {
    if ($response && $response.status === 201) {
      window.location.href = "/signup-success";
    } else if ($response && $response.status >= 400) {
      errorMessage =
        $response.data.message || "Signup failed. Please try again.";
    }
  }

  onMount(() => {
    errorMessage = ""; // Clear any previous error messages on component mount
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full py-20 m-auto min-h-fit"
>
  <div class="flex flex-col max-w-3xl gap-4">
    <div class="-mb-2 text-center">
      <h1 class="text-5xl font-bold text-accent">Crear Cuenta</h1>
      <p class="text-md text-secondary">Crea tu cuenta para continuar</p>
      <br />
    </div>

    <div class="flex flex-col w-screen h-full max-w-3xl min-w-full gap-4">
      <div class="flex flex-wrap items-center justify-center gap-4">
        <label
          class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg basis-1/3 border-neutral"
        >
          <p class="w-16 text-center">Nombre</p>
          <input
            bind:value={first_name}
            on:keydown={handleKeydown}
            type="text"
            class="border-none focus:ring-0 grow text-secondary"
            placeholder="Juan"
          />
        </label>
        <label
          class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg basis-1/3 border-neutral"
        >
          <p class="w-16 text-center">Apellido</p>
          <input
            bind:value={last_name}
            on:keydown={handleKeydown}
            type="text"
            class="border-none focus:ring-0 grow text-secondary"
            placeholder="del Pueblo"
          />
        </label>
      </div>
      <div class="flex flex-wrap items-center justify-center gap-4">
        <label
          class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg border-neutral basis-1/3"
        >
          <p class="w-16">Correo</p>
          <input
            bind:value={email}
            on:keydown={handleKeydown}
            type="email"
            class="border-none focus:ring-0 grow text-secondary"
            placeholder="juandpueblo@email.com"
          />
        </label>
        <label
          class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg border-neutral basis-1/3"
        >
          <p class="w-16 text-center">Teléfono</p>
          <input
            bind:value={phone}
            on:input={handlePhoneNum}
            on:keydown={handleKeydown}
            type="tel"
            class="border-none focus:ring-0 grow text-secondary"
            placeholder="787-555-5555"
          />
        </label>
      </div>
      <div class="flex flex-wrap items-center justify-center gap-4">
        <label
          class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg border-neutral basis-1/3"
        >
          <p class="w-16 text-center">Contraseña</p>
          <input
            bind:value={password}
            on:keydown={handleKeydown}
            type="password"
            class="border-none focus:ring-0 grow text-secondary"
            placeholder="********"
          />
        </label>
        <label
          class="flex items-center gap-4 px-2 py-1 bg-white border-2 rounded-lg border-neutral basis-1/3"
        >
          <p class="w-16 text-center">Confirmar</p>
          <input
            bind:value={confirmPassword}
            on:keydown={handleKeydown}
            type="password"
            class="border-none focus:ring-0 grow text-secondary"
            placeholder="********"
          />
        </label>
      </div>
    </div>
    <div class="flex flex-col items-center justify-center mx-4">
      <Button
        on:click={validatePasswords}
        bind:this={buttonRef}
        {image}
        {button}
      ></Button>
    </div>
    <p class="flex items-center justify-center pr-2 -mt-3 text-sm text-right">
      ¿Ya tienes una cuenta? <a
        use:link
        class="pl-4 link link-hover text-accent"
        rel="noopener noreferrer"
        href="/login"
      >
        Iniciar sesión</a
      >.
    </p>
    {#if errorMessage}
      <div class="text-center text-red-500">{errorMessage}</div>
    {/if}
    {#if $state.hidden === true}
      <div class="hidden"></div>
    {:else if (!$state.hidden && !$state.loaded) || $state.reload}
      <Loading />
    {:else if $state.error}
      <div class="w-full mx-auto font-bold text-center text-stone-600">
        Correo o contraseña incorrectos. Por favor, intenta de nuevo.
      </div>
    {/if}
  </div>
</div>
