<script>
  import Footer from "./Footer.svelte";
  import Header from "./Header.svelte";
</script>

<div class="flex flex-col w-screen h-screen bg-slate-100">
  <!-- <Navbar /> -->
  <Header></Header>
  <div class="w-screen h-full">
    <slot />
  </div>
  <Footer />
</div>
