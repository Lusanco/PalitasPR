<script>
  import { changeView } from "../scripts/viewManager";
  import { onMount } from "svelte";

  onMount(() => {
    changeView("SignUp");
  });

  let name = "";
  let username = "";
  let email = "";
  let password = "";
  let confirmPassword = "";

  // Current step in the signup process
  let currentStep = 1;

  function handleSubmit(event) {
    event.preventDefault();
    // Add your signup logic here
    console.log("Name:", name);
    console.log("Username:", username);
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Confirm Password:", confirmPassword);
  }
</script>

<div class="flex flex-col items-center justify-center h-full bg-[#F4F5F6]">
  <div
    class="p-6 mx-auto bg-[#F4F5F6] shadow-lg shadow-slate-300/90 md:p-6 lg:p-6 LoginBox sm:w-3/4 md:w-2/3 lg:w-1/2 xl:w-1/3 sm:mx-6 md:mx-8 lg:mx-12 rounded-md"
  >
    <div class="mb-4 text-center">
      <h1 class="my-2 text-4xl font-bold text-gray-800">
        Sign <span class="text-[#006E5A]">Up</span>
      </h1>
      <p class="text-sm text-gray-600">Create an account to get started</p>
    </div>
    <form on:submit={handleSubmit} class="">
      <!-- Step 1 -->
      {#if currentStep === 1}
        <div>
          <label for="name" class="block mb-2 text-sm">Name</label>
          <input
            type="text"
            bind:value={name}
            id="name"
            placeholder="Enter your name"
            class="w-full px-3 py-2 border rounded-md dark:border-gray-300 dark:bg-gray-50 dark:text-gray-800"
          />
          <button
            on:click={() => (currentStep = 2)}
            class="w-full px-8 py-3 my-2 mt-6 font-semibold text-[#F4F5F6] bg-[#006E5A] rounded-md button-hover hover:bg-[#008F75]"
            >Next</button
          >
        </div>
      {/if}

      <!-- Step 2 -->
      {#if currentStep === 2}
        <div>
          <label for="username" class="block mb-2 text-sm">Username</label>
          <input
            type="text"
            bind:value={username}
            id="username"
            placeholder="Enter your username"
            class="w-full px-3 py-2 border rounded-md dark:border-gray-300 dark:bg-gray-50 dark:text-gray-800"
          />
          <button
            on:click={() => (currentStep = 3)}
            class="w-full px-8 py-3 my-2 mt-6 font-semibold text-[#F4F5F6] bg-[#006E5A] rounded-md button-hover hover:bg-[#008F75]"
            >Next</button
          >
        </div>
      {/if}

      <!-- Step 3 -->
      {#if currentStep === 3}
        <div>
          <label for="email" class="block mb-2 text-sm">Email address</label>
          <input
            type="email"
            bind:value={email}
            id="email"
            placeholder="Enter your email address"
            class="w-full px-3 py-2 border rounded-md dark:border-gray-300 dark:bg-gray-50 dark:text-gray-800"
          />
          <button
            on:click={() => (currentStep = 4)}
            class="w-full px-8 py-3 my-2 mt-6 font-semibold text-[#F4F5F6] bg-[#006E5A] rounded-md button-hover hover:bg-[#008F75]"
            >Next</button
          >
        </div>
      {/if}

      <!-- Step 4 -->
      {#if currentStep === 4}
        <div>
          <label for="password" class="block mb-2 text-sm">Password</label>
          <input
            type="password"
            bind:value={password}
            id="password"
            placeholder="Enter your password"
            class="w-full px-3 py-2 border rounded-md dark:border-gray-300 dark:bg-gray-50 dark:text-gray-800"
          />
          <button
            on:click={() => (currentStep = 5)}
            class="w-full px-8 py-3 my-2 mt-6 font-semibold text-[#F4F5F6] bg-[#006E5A] rounded-md button-hover hover:bg-[#008F75]"
            >Next</button
          >
        </div>
      {/if}

      <!-- Step 5 -->
      {#if currentStep === 5}
        <div>
          <label for="confirmPassword" class="block mb-2 text-sm"
            >Confirm Password</label
          >
          <input
            type="password"
            bind:value={confirmPassword}
            id="confirmPassword"
            placeholder="Confirm your password"
            class="w-full px-3 py-2 border rounded-md dark:border-gray-300 dark:bg-gray-50 dark:text-gray-800"
          />
          <button
            on:click={() => changeView("LandingPage")}
            type="submit"
            class="w-full px-8 py-3 my-2 mt-6 font-semibold text-[#F4F5F6] bg-[#006E5A] rounded-md button-hover hover:bg-[#008F75]"
            >Sign Up</button
          >
        </div>
      {/if}
    </form>
  </div>
</div>

<style></style>
