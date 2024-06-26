<script>
  import { link } from "svelte-routing";
  import Loading from "../components/Loading.svelte";
  import Button from "../components/Button.svelte";
  import { state, data, response } from "../scripts/stores";
  import { get } from "svelte/store";
  import { onMount } from "svelte";

  // Button Prop Variables And Dependencies
  let image = null;
  let first_name;
  let last_name;
  let password;
  let confirmPassword;
  let email;
  let af1 = null;
  let af2 = null;
  let errorMessage;
  let button = {
    name: "Signup",
    method: "POST",
    url: "/api/user/signup",
    headers: "application/json",
    twcss: "border-2 shadow-md btn bg-base-100",
    misc: { "App Location": "Signup" },
  };
  // Button Prop Variables And Dependencies
  // Reactive block to update $data
  $: {
    $data = {
      first_name,
      last_name,
      email,
      password,
    };
  }

  data.set($data);
  // Define a reference for the Button component
  let buttonRef;

  // Function to handle the "Enter" key press
  function handleKeydown(event) {
    if (event.key === "Enter") {
      // Trigger the button logic from the child component
      if (password !== confirmPassword) {
        password = "";
        confirmPassword = "";
        errorMessage = "Passwords do not match!";
        return; // Exit early if passwords do not match
      }

      buttonRef.buttonLogic();
    }
  }

  // Reactive statement to update button store when misc store changes
  $: {
    button = {
      ...button,
    };

    // Update the data store with the current misc values
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
  class="flex flex-col items-center justify-center h-full min-h-screen py-20 m-auto"
>
  <div class="flex flex-col max-w-sm gap-4 px-1">
    <div class="text-center">
      <h1 class="text-4xl font-bold text-stone-800">Signup</h1>
      <p class="text-sm text-stone-600">Signup to create your account</p>
      <br />
    </div>
    <label class="flex items-center gap-2 input input-bordered">
      <p class="text-center w-14">First</p>
      <input
        bind:value={first_name}
        on:keydown={handleKeydown}
        type="text"
        class="border-none focus:ring-0 grow"
        placeholder="John"
      />
    </label>
    <label class="flex items-center gap-2 input input-bordered">
      <p class="text-center w-14">Last</p>
      <input
        bind:value={last_name}
        on:keydown={handleKeydown}
        type="text"
        class="border-none focus:ring-0 grow"
        placeholder="Doe"
      />
    </label>
    <label class="flex items-center gap-2 input input-bordered">
      <p class="text-center w-14">Email</p>
      <input
        bind:value={email}
        on:keydown={handleKeydown}
        type="email"
        class="border-none focus:ring-0 grow"
        placeholder="user@email.com"
      />
    </label>
    <label class="flex items-center gap-2 input input-bordered">
      <p class="text-center w-14">Password</p>
      <input
        bind:value={password}
        on:keydown={handleKeydown}
        type="password"
        class="border-none focus:ring-0 grow"
        placeholder="********"
      />
    </label>
    <label class="flex items-center gap-2 input input-bordered">
      <p class="text-center w-14">Confirm</p>
      <input
        bind:value={confirmPassword}
        on:keydown={handleKeydown}
        type="password"
        class="border-none focus:ring-0 grow"
        placeholder="********"
      />
    </label>

    <Button bind:this={buttonRef} {image} {button}></Button>
    <p class="pr-2 -mt-4 text-right">
      Have an account? <a
        use:link
        class="link link-hover"
        rel="noopener noreferrer"
        href="/login">Login</a
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
