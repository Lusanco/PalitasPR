<script>
  import { onMount } from "svelte";
  import { link } from "svelte-routing";
  import axios from "axios";

  let first_name,
    last_name,
    password,
    confirmPassword,
    errorMessage,
    email = "";

  async function handleSignup() {
    if (password !== confirmPassword) {
      errorMessage = "Passwords do not match!";
      return; // Prevent unnecessary API call
    }

    const data = {
      first_name: first_name,
      last_name: last_name,
      email: email,
      password: password,
    };

    // let user = JSON.stringify(data);

    axios
      .post("/api/create_object", data)
      //   .get("https://jsonplaceholder.typicode.com/users")
      .then((response) => {
        console.log(response);
        window.location.href = "/login";
      })
      .catch((error) => {
        console.log(error);
        errorMessage = error;
      });
  }

  onMount(() => {
    errorMessage = ""; // Clear any previous error messages on component mount
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full max-w-lg p-6 m-auto text-teal-800 rounded-md sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold">Sign up</h1>
    <p class="text-sm text-teal-600">Sign up to create your account</p>
  </div>
  <form action="" class="w-full space-y-12">
    <div class="space-y-4">
      <div class="grid grid-cols-1 gap-2 md:grid-cols-2">
        <div class="">
          <label for="first_name" class="block mb-2 text-sm">First Name</label>
          <input
            bind:value={first_name}
            type="text"
            name="first_name"
            id="first_name"
            placeholder="John"
            class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
          />
        </div>
        <div class="">
          <label for="last_name" class="block mb-2 text-sm">Last Name</label>
          <input
            bind:value={last_name}
            type="text"
            name="last_name"
            id="last_name"
            placeholder="Doe"
            class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
          />
        </div>
      </div>
      <div>
        <label for="email" class="block mb-2 text-sm">Email address</label>
        <input
          bind:value={email}
          type="email"
          name="email"
          id="email"
          placeholder="johndoe@email.com"
          class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
        />
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <label for="password" class="text-sm">Password</label>
        </div>
        <input
          bind:value={password}
          type="password"
          name="password"
          id="password"
          placeholder="************"
          class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
        />
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <label for="password" class="text-sm">Confirm Password</label>
        </div>
        <input
          bind:value={confirmPassword}
          type="password"
          name="confirm"
          id="confirm"
          placeholder="************"
          class="w-full px-3 py-2 text-teal-800 border border-teal-300 rounded-md bg-teal-50"
        />
      </div>
    </div>
    <div class="space-y-2">
      <div>
        <button
          on:click={handleSignup}
          type="button"
          class="w-full px-8 py-3 font-semibold bg-teal-600 rounded-md text-teal-50"
          >Sign up</button
        >
      </div>
      <p class="px-6 text-sm text-center text-teal-600">
        Have an account?
        <a
          use:link
          href="/login"
          rel="noopener noreferrer"
          role="button"
          class="font-semibold text-teal-600 hover:underline">Login</a
        >
      </p>
    </div>
  </form>
</div>
