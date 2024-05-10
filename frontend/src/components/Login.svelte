<script>
  import { link } from "svelte-routing";
  import { onMount } from "svelte";
  import axios from "axios";
  import LoadingSpinnerFull from "./LoadingSpinnerFull.svelte";

  let password, errorMessage, email;
  let hidden = true;
  let loaded = false;
  let reload = false;

  function loginLogic() {
    hidden = false;
    reload = true;
    const data = {
      email: email,
      password: password,
    };

    axios
      .post("/api/login", data)
      .then((response) => {
        loaded = true;
        reload = false;
        if (response.data.response === "success") {
          window.location.href = "/";
        }
      })
      .catch((error) => {
        console.log(error);
        errorMessage = error;
      });
  }

  function handleKeydown(event) {
    if (event.key === "Enter") {
      email = email;
      password = password;
      loginLogic();
    }
  }

  async function handleLogin() {
    loginLogic();
  }

  onMount(() => {
    errorMessage = ""; // Clear any previous error messages on component mount
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full max-w-md p-6 m-auto text-teal-800 rounded-md sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold">Login</h1>
    <p class="text-sm text-teal-600">Login to access your account</p>
  </div>
  <form action="" class="w-full space-y-12">
    <div class="space-y-4">
      <div>
        <label for="email" class="block mb-2 text-sm">Email address</label>
        <input
          bind:value={email}
          on:keydown={handleKeydown}
          type="email"
          name="email"
          id="email"
          placeholder="user@email.com"
          class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
        />
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <label for="password" class="text-sm">Password</label>
          <a
            rel="noopener noreferrer"
            href="/forgot-password"
            class="text-xs text-teal-600 hover:underline">Forgot password?</a
          >
        </div>
        <input
          bind:value={password}
          on:keydown={handleKeydown}
          type="password"
          name="password"
          id="password"
          placeholder="************"
          class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
        />
      </div>
    </div>
    <div class="space-y-2">
      <button
        on:click={handleLogin}
        type="button"
        class="w-full px-8 py-3 font-semibold bg-teal-600 rounded-md text-teal-50"
        >Login</button
      >
      <p class="px-6 text-sm text-center text-teal-600">
        Don't have an account yet?
        <a
          use:link
          href="/signup"
          rel="noopener noreferrer"
          role="button"
          class="font-semibold text-teal-600 hover:underline">Sign up</a
        >
      </p>
    </div>
  </form>
</div>

{#if hidden === true}
  <div class="hidden"></div>
{:else if (hidden === false && loaded === false) || reload === true}
  <LoadingSpinnerFull />
{/if}
