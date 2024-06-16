<script>
  import { link } from "svelte-routing";
</script>

<head>
  <title>PalitasPR | Not Found</title>
</head>

<div
  class="flex flex-col justify-center h-full min-h-screen px-6 py-20 place-items-center sm:py-32 lg:px-8"
>
  <div class="text-center">
    <p class="font-semibold text-[#cc2936] text-8xl">404</p>
    <h1
      class="mt-4 text-3xl font-bold tracking-tight text-[#1f1f1f] sm:text-5xl"
    >
      Page not found
    </h1>
    <p class="mt-3 text-xl leading-7 text-[#cc2936]">
      Sorry, we couldn’t find the page you’re looking for.
    </p>
    <br />
    <div class="flex items-center justify-center">
      <a
        use:link
        href="/"
        class="bg-[#cc2936] text-[#f1f1f1] hover:text-[#1f1f1f] hover:bg-white btn px-6"
        >Home</a
      >
    </div>
  </div>
</div>
