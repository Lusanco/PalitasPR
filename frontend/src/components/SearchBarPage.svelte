<script>
  import SearchBar from "./SearchBar.svelte";
  import Card from "./Card.svelte";
</script>

<div class="flex flex-col items-center justify-center h-full gap-8">
  <div class="text-center text-teal-500">
    <h1 class="text-6xl font-bold">
      Palitas<span class="text-teal-700">PR</span>
    </h1>
    <p class="-mt-2 text-2xl italic">Servicios Locales y Accesibles</p>
  </div>
  <div class="items-center justify-center w-full max-w-md">
    <SearchBar />
    <!-- <Card /> -->
  </div>
</div>
