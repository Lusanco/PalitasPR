<!-- Header Layout -->
<script>
  import { link } from "svelte-routing";
  import { userSession } from "../scripts/stores";

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
<header class={$userSession ? `hidden` : `` + " border-b-4 shadow-2xl border-[#cc2936] navbar bg-[#1f1f1f] "}>
  <div class="navbar-start">
    <a
      use:link
      on:click={handlePalitasPRClick}
      href="/"
      rel="noopener noreferrer"
      class="text-xl bg-transparent border-none hover:bg-gradient-to-t hover:from-[#1f1f1f] hover:via-[#cc2936] hover:to-[#1f1f1f] mx-4 rounded-full"
    >
      <img class="w-24" src="/logoLight.svg" alt="" />
    </a>
  </div>
  <div class="gap-2 navbar-end">
    <a
      use:link
      href="/login"
      rel="noopener noreferrer"
      class="btn border-[#cc2936] border-b-2 border-t-0 border-x-0 text-[#f1f1f1] bg-transparent hover:bg-transparent hover:border-[#f1f1f1]"
      >Login</a
    >
    <a
      use:link
      href="/signup"
      rel="noopener noreferrer"
      class="btn mr-4 border-[#cc2936] border-b-2 border-t-0 border-x-0 text-[#f1f1f1] bg-transparent hover:bg-transparent hover:border-[#f1f1f1]"
      >Signup</a
    >
  </div>
</header>
<!-- Header End -->