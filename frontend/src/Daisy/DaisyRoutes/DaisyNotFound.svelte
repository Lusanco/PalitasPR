<script>
  import { link } from "svelte-routing";
</script>

<div class="flex items-center justify-center min-h-screen px-6 py-24 bg-base-200 lg:px-8">
  <div class="text-center">
    <p class="font-semibold text-stone-300 text-8xl">404</p>
    <h1 class="mt-4 text-3xl font-bold tracking-tight text-stone-900 sm:text-5xl">
      Page not found
    </h1>
    <p class="mt-3 text-base leading-7 text-stone-600">
      Sorry, we couldn’t find the page you’re looking for.
    </p>
    <div class="flex items-center justify-center mt-8 gap-x-6">
      <a
        use:link
        href="/"
        class="p-4 text-sm font-semibold text-white rounded-md shadow-sm btn bg-stone-600 hover:bg-stone-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-stone-600"
        >Go back home</a
      >
    </div>
  </div>
</div>