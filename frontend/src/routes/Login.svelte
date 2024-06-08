<script>
  import { link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";
  import Button from "../components/Button.svelte";
  import { state, data, response } from "../scripts/stores";
  import { get } from "svelte/store";
  import { onMount } from "svelte";

  // Button Prop Variables And Dependencies
  let image = null;
  let af1 = null;
  let af2 = null;
  let errorMessage;
  let button = {
    name: "Login",
    method: "GET",
    url: `/api/user/login?af1=${af1}&af2=${af2}`,
    headers: "application/json",
    twcss: "border-2 shadow-md btn bg-base-100",
    misc: { "App Location": "Login" },
  };
  // Button Prop Variables And Dependencies

  // Define a reference for the Button component
  let buttonRef;

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

<div
  class="flex flex-col items-center justify-center h-full min-h-screen m-auto"
>
  <div class="flex flex-col max-w-sm gap-4 px-1">
    <div class="text-center">
      <h1 class="text-4xl font-bold text-stone-800">Login</h1>
      <p class="text-sm text-stone-600">Login to access your account</p>
      <br />
    </div>
    <label class="flex items-center gap-2 input input-bordered">
      <p class="text-center w-14">Email</p>
      <input
        bind:value={af1}
        on:keydown={handleKeydown}
        type="text"
        class="border-none focus:ring-0 grow"
        placeholder="user@email.com"
      />
    </label>
    <label class="flex items-center gap-2 input input-bordered">
      <p class="text-center w-14">Password</p>
      <input
        bind:value={af2}
        on:keydown={handleKeydown}
        type="password"
        class="border-none focus:ring-0 grow"
        placeholder="********"
      />
    </label>
    <a
      use:link
      href="/forgot-password"
      class="self-end pr-2 -mt-4 link link-hover">Forgot password?</a
    >
    <Button bind:this={buttonRef} {image} {button}></Button>
    <p class="pr-2 -mt-4 text-right">
      Don't have an account yet? <a
        use:link
        class="link link-hover"
        href="/signup">Signup</a
      >
    </p>
    {#if $state.hidden === true}
      <div class="hidden"></div>
    {:else if (!$state.hidden && !$state.loaded) || $state.reload}
      <Loading />
    {:else if $state.error}
      <div class="w-full mx-auto font-bold text-center text-stone-600">
        Incorrect email or password, try again.
      </div>
    {/if}
  </div>
</div>
