<script>
  import { link } from "svelte-routing";
</script>

<div
  class="flex flex-col items-center justify-center max-w-lg min-h-screen p-6 m-auto text-teal-800 rounded-md sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-3xl font-bold text-wrap">
      Account created succesfully
    </h1>
    <p class="px-6 mt-3 text-sm text-center">
      To continue, login to your account
    </p>
    <p class="px-6 pt-4 text-sm text-center text-teal-600">
      <button
        type="button"
        class="px-8 py-3 font-semibold text-white bg-teal-600 rounded-md hover:bg-teal-800"
        ><a use:link href="/login" rel="noopener noreferrer" role="button"
          >Login</a
        ></button
      >
    </p>
  </div>
</div>
