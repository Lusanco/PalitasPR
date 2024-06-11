<script>
  import { onMount, afterUpdate } from "svelte";
  import { link } from "svelte-routing";
  import axios from "axios";
  import Loading from "../components/Loading.svelte";

  let first_name,
    last_name,
    password,
    confirmPassword,
    errorMessage,
    email = "";

  let hidden = true;
  let loaded = false;
  let reload = false;
  let error = false;

  function signupLogic() {
    hidden = false;
    loaded = false;
    reload = true;
    error = false;
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
      .post("/api/user/signup", data)
      .then((response) => {
        loaded = true;
        reload = false;
        error = false;
        console.log(response);
        if (response.status === 201) {
          window.location.href = "/success";
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
      email = email;
      password = password;
      signupLogic();
    }
  }

  async function handleSignup() {
    signupLogic();
  }

  onMount(() => {
    errorMessage = ""; // Clear any previous error messages on component mount
  });
  afterUpdate(() => {
    if (error) {
      const errorElement = document.getElementById("err-msg");
      errorElement.scrollIntoView({ behavior: "smooth" });
    }
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full max-w-lg p-6 m-auto rounded-md text-primary sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold text-primary">Sign up</h1>
    <p class="text-sm text-primary">Sign up to create your account</p>
  </div>
  <form action="" class="w-full space-y-12">
    <div class="space-y-4">
      <div class="grid grid-cols-1 gap-2 md:grid-cols-2">
        <div class="">
          <label for="first_name" class="block mb-2 text-sm">First Name</label>
          <input
            bind:value={first_name}
            on:keydown={handleKeydown}
            type="text"
            name="first_name"
            id="first_name"
            placeholder="John"
            class="w-full input input-bordered text-primary"
          />
        </div>
        <div class="">
          <label for="last_name" class="block mb-2 text-sm">Last Name</label>
          <input
            bind:value={last_name}
            on:keydown={handleKeydown}
            type="text"
            name="last_name"
            id="last_name"
            placeholder="Doe"
            class="w-full input input-bordered text-primary"
          />
        </div>
      </div>
      <div>
        <label for="email" class="block mb-2 text-sm">Email address</label>
        <input
          bind:value={email}
          on:keydown={handleKeydown}
          type="email"
          name="email"
          id="email"
          placeholder="johndoe@email.com"
          class="w-full input input-bordered text-primary"
        />
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <label for="password" class="text-sm">Password</label>
        </div>
        <input
          bind:value={password}
          on:keydown={handleKeydown}
          type="password"
          name="password"
          id="password"
          placeholder="************"
          class="w-full input input-bordered text-primary"
        />
      </div>
      <div>
        <div class="flex justify-between mb-2">
          <label for="password" class="text-sm">Confirm Password</label>
        </div>
        <input
          bind:value={confirmPassword}
          on:keydown={handleKeydown}
          type="password"
          name="confirm"
          id="confirm"
          placeholder="************"
          class="w-full input input-bordered text-primary"
        />
      </div>
    </div>
    <div class="space-y-2">
      <div>
        <button
          on:click={handleSignup}
          type="button"
          class="w-full btn btn-primary"
          >Sign up</button
        >
      </div>
      <p class="px-6 text-sm text-center text-primary">
        Have an account?
        <a
          use:link
          href="/login"
          rel="noopener noreferrer"
          role="button"
          class="font-semibold text-primary hover:underline">Sign In</a
        >
      </p>
    </div>
    {#if hidden === true}
      <div class="hidden"></div>
    {:else if (hidden === false && loaded === false) || reload === true}
      <Loading />
    {:else if error}
      <div
        id="err-msg"
        class="w-full mx-auto font-bold text-center text-primary"
      >
        Unsuccessful atempt to create account, try again.
      </div>
    {/if}
  </form>
</div>
