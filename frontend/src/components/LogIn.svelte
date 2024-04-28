<script>
  import { changeView } from "../scripts/viewManager";
  import { onMount } from "svelte";

  onMount(() => {
    changeView("LogIn");
  });

  let email = "";
  let password = "";

  function handleSubmit(event) {
    event.preventDefault();
    // Add your login logic here
    console.log("Email:", email);
    console.log("Password:", password);
  }
</script>

<div class="flex flex-col items-center justify-center h-full bg-slate-100">
  <div
    class="p-6 mx-auto bg-white md:p-6 lg:p-6 LoginBox sm:w-3/4 md:w-2/3 lg:w-1/2 xl:w-1/3 sm:mx-6 md:mx-8 lg:mx-12"
  >
    <div class="mb-8 text-center">
      <h1 class="my-3 text-4xl font-bold">Login</h1>
      <p class="text-sm text-gray-600">Login to access your account</p>
    </div>
    <form on:submit={handleSubmit} class="space-y-12">
      <div class="space-y-4">
        <div>
          <label for="email" class="block mb-2 text-sm">Email address</label>
          <input
            type="email"
            bind:value={email}
            id="email"
            placeholder="leroy@jenkins.com"
            class="w-full px-3 py-2 border rounded-md dark:border-gray-300 dark:bg-gray-50 dark:text-gray-800"
          />
        </div>
        <div>
          <div class="flex justify-between mb-2">
            <label for="password" class="text-sm">Password</label>
            <a href="/" class="text-xs hover:underline dark:text-gray-600"
              >Forgot password?</a
            >
          </div>
          <input
            type="password"
            bind:value={password}
            id="password"
            placeholder="************"
            class="w-full px-3 py-2 border rounded-md dark:border-gray-300 dark:bg-gray-50 dark:text-gray-800"
          />
        </div>
      </div>
      <div class="space-y-2">
        <div>
          <button
            on:click={() => changeView("LandingPage")}
            type="submit"
            class="w-full px-8 py-3 font-semibold text-white bg-teal-400 rounded-md dark:bg-violet-600 dark:text-gray-50 button-hover hover:bg-teal-500"
            >Login</button
          >
        </div>
        <p class="px-6 text-sm text-center dark:text-gray-600">
          Don't have an account yet?
          <a
            href="/"
            role="button"
            on:click|preventDefault={() => changeView("SignUp")}
            class="text-teal-400 hover:text-teal-500 hover:underline">Sign up</a
          >.
        </p>
      </div>
    </form>
  </div>
</div>

<style></style>
