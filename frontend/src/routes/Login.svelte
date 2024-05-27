<script>
  import { link } from "svelte-routing";
  import { onMount } from "svelte";
  import axios from "axios";
  import LoadingSpinner from "../components/LoadingSpinner.svelte";

  let af2, errorMessage, af1;
  let hidden = true;
  let loaded = false;
  let reload = false;
  let error = false;

  function loginLogic() {
    if (typeof af1 === "undefined" || typeof af2 === "undefined") {
      af1 = null;
      af2 = null;
    }
    hidden = false;
    loaded = false;
    reload = true;
    error = false;

    // .post("/api/login", data)
    axios
      .get(`/api/login?af1=${af1}&af2=${af2}`)
      // .get(`/api/login?e=${af1}&p=${af2}`)
      .then((response) => {
        loaded = true;
        reload = false;
        error = false;
        console.log(response);
        if (response.status === 200) {
          // Write logic for real life cases
          // as in flask_login appropiate
          window.location.href = "/";
        }
      })
      .catch((err) => {
        hidden = false;
        loaded = true;
        reload = false;
        error = true;
        console.log(err);
        errorMessage = err;
      });
  }

  function handleKeydown(event) {
    if (event.key === "Enter") {
      af1 = af1;
      af2 = af2;
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
  class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto text-teal-800 rounded-md sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold">Login</h1>
    <p class="text-sm text-teal-600">Login to access your account</p>
  </div>
  <form action="" class="w-full space-y-12">
    <div class="space-y-4">
      <div>
        <label for="af1" class="block mb-2 text-sm">Email address</label>
        <input
          bind:value={af1}
          on:keydown={handleKeydown}
          type="email"
          name="email"
          id="af1"
          placeholder="user@email.com"
          class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
        />
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <label for="af2" class="text-sm">Password</label>
          <a
            rel="noopener noreferrer"
            href="/forgot-password"
            class="text-xs text-teal-600 hover:underline">Forgot password?</a
          >
        </div>
        <input
          bind:value={af2}
          on:keydown={handleKeydown}
          type="password"
          name="af2"
          id="af2"
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
    {#if hidden === true}
      <div class="hidden"></div>
    {:else if (hidden === false && loaded === false) || reload === true}
      <LoadingSpinner />
    {:else if error}
      <div class="w-full mx-auto font-bold text-center text-teal-600">
        Incorrect email or password, try again.
      </div>
    {/if}
  </form>
</div>
