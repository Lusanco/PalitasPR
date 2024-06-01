<script>
    import { link } from "svelte-routing";
  
    function redirectToLogin() {
      window.location.href = "/login";
    }
  </script>
  
  <div class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto text-teal-800 rounded-md sm:p-10">
    <div class="mb-8 text-center">
      <h1 class="my-3 text-4xl font-bold">Please Login to Continue</h1>
      <p class="text-sm text-teal-600">You need to log in to access this page.</p>
    </div>
    <div class="space-y-2">
      <button
        on:click={redirectToLogin}
        type="button"
        class="w-full px-8 py-3 font-semibold bg-teal-600 rounded-md text-teal-50"
      >
        Login
      </button>
    </div>
  </div>