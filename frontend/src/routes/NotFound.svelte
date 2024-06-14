<script>
  import { link } from "svelte-routing";
</script>

<div
  class="flex flex-col justify-center h-full px-6 py-20 place-items-center sm:py-32 lg:px-8"
>
  <div class="text-center">
    <p class="font-semibold text-stone-300 text-8xl">404</p>
    <h1
      class="mt-4 text-3xl font-bold tracking-tight text-stone-700 sm:text-5xl"
    >
      Page not found
    </h1>
    <p class="mt-3 text-base leading-7 text-stone-600">
      Sorry, we couldn’t find the page you’re looking for.
    </p>
    <div class="flex items-center justify-center mt-8 gap-x-6">
      <a use:link href="/" class="bg-stone-200 btn">Go back home</a>
    </div>
  </div>
</div>
