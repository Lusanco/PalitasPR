<!-- Header Layout -->
<script>
  import { link } from "svelte-routing";
  import { userSession } from "../../scripts/stores";

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
      class="mx-4 text-xl transition-transform duration-300 ease-in-out bg-transparent border-none rounded-full hover:scale-110"
    >
      <img class="w-24 md:w-28" src="/logoDark.svg" alt="" />
    </a>
  </div>
  <div class="gap-2 mr-4 navbar-end">
    <a
      use:link
      href="/login"
      rel="noopener noreferrer"
      class="w-16 shadow-lg btn md:w-24 text-primary bg-accent hover:bg-green-900"
      >Login</a
    >
    <a
      use:link
      href="/signup"
      rel="noopener noreferrer"
      class="w-16 font-semibold border-2 shadow-lg md:w-24 text-accent border-accent btn bg-primary hover:opacity-80 hover:border-accent"
      >Signup</a
    >
  </div>
</header>
<!-- Header End -->
