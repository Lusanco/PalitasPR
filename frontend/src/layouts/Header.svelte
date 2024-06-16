<!-- Header Layout -->
<script>
  import { link } from "svelte-routing";

  // Function to handle the "PalitasPR" link click
  function handlePalitasPRClick(event) {
    event.preventDefault();
    if (window.location.pathname === "/") {
      window.location.reload();
    } else {
      window.location.href = "/";
    }
  }
</script>

<!-- Header Start -->
<header class="border-b-4 shadow-2xl border-[#cc2936] navbar bg-[#1f1f1f]">
  <div class="navbar-start">
    <a
      use:link
      on:click={handlePalitasPRClick}
      href="/"
      rel="noopener noreferrer"
      class="text-xl border-none btn"
    >
      <img class="w-24" src="/public/logoLight.svg" alt="" />
    </a>
  </div>
  <div class="gap-2 navbar-end">
    <a
      use:link
      href="/login"
      rel="noopener noreferrer"
      class="btn border-[#cc2936] border-b-2 border-t-0 border-x-0 text-[#f1f1f1]"
      >Login</a
    >
    <a
      use:link
      href="/signup"
      rel="noopener noreferrer"
      class="btn border-[#cc2936] border-b-2 border-t-0 border-x-0 text-[#f1f1f1]"
      >Signup</a
    >
  </div>
</header>
<!-- Header End -->
