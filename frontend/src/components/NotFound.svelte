<script>
  import { link } from "svelte-routing";
</script>

<div
  class="flex justify-center h-full px-6 py-24 bg-white place-items-center sm:py-32 lg:px-8"
>
  <div class="text-center">
    <p class="font-semibold text-gray-300 text-8xl">404</p>
    <h1
      class="mt-4 text-3xl font-bold tracking-tight text-gray-900 sm:text-5xl"
    >
      Page not found
    </h1>
    <p class="mt-3 text-base leading-7 text-gray-600">
      Sorry, we couldn’t find the page you’re looking for.
    </p>
    <div class="flex items-center justify-center mt-8 gap-x-6">
      <a
        use:link
        href="/"
        class="p-4 text-sm font-semibold text-white bg-teal-600 rounded-md shadow-sm hover:bg-teal-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >Go back home</a
      >
    </div>
  </div>
</div>
