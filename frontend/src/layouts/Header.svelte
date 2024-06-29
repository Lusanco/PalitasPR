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
<header
  class={$userSession
    ? `hidden`
    : `` + " p-2 md:p-4 shadow-lg md:shadow-xl navbar bg-primary "}
>
  <div class="navbar-start">
    <a
      use:link
      on:click={handlePalitasPRClick}
      href="/"
      rel="noopener noreferrer"
      class="text-xl bg-transparent border-none hover:from-[#1f1f1f] hover:scale-110 transition-transform ease-in-out duration-200 mx-4 rounded-full"
    >
      <img class="w-24 md:w-28" src="/logoDark.svg" alt="" />
    </a>
  </div>
  <div class="gap-2 mr-4 navbar-end">
    <a
      use:link
      href="/login"
      rel="noopener noreferrer"
      class="btn w-16 md:w-24 text-base font-semibold shadow-lg text-[#f1f1f1] bg-accent hover:bg-green-900"
      >Login</a
    >
    <a
      use:link
      href="/signup"
      rel="noopener noreferrer"
      class="w-16 text-base font-semibold border-2 shadow-lg md:w-24 text-accent border-accent btn bg-primary hover:opacity-80 hover:border-accent"
      >Signup</a
    >
  </div>
</header>
<!-- Header End -->
