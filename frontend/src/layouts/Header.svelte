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
<header class="navbar bg-base-100">
  <div class="navbar-start">
    <a
      use:link
      on:click={handlePalitasPRClick}
      href="/"
      rel="noopener noreferrer"
      class="text-xl btn btn-ghost">PalitasPR</a
    >
  </div>
  <div class="gap-2 navbar-end">
    <a use:link href="/login" rel="noopener noreferrer" class="btn">Login</a>
    <a use:link href="/signup" rel="noopener noreferrer" class="btn">Signup</a>
  </div>
</header>
<!-- Header End -->
