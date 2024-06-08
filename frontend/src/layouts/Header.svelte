<!-- Header Layout -->
<script>
  import { link } from "svelte-routing";
</script>

<!-- Header Start -->
<header class="navbar bg-base-100">
  <div class="navbar-start">
    <a use:link href="/" class="text-xl btn btn-ghost">PalitasPR</a>
  </div>
  <div class="gap-2 navbar-end">
    <a use:link href="/login" class="btn">Login</a>
    <a use:link href="/signup" class="btn">Signup</a>
  </div>
</header>
<!-- Header End -->
