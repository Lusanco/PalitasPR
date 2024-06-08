<script>
  import { link } from "svelte-routing";
</script>

<footer
  class="flex flex-wrap justify-between p-10 rounded footer bg-base-100 text-base-content"
>
  <nav class="flex flex-wrap items-center justify-center gap-4 mx-auto">
    <a use:link href="/terms-of-use" class="link link-hover">Terms of Use</a>
    <a use:link href="/privacy" class="link link-hover">Privacy</a>
    <a use:link href="/about" class="link link-hover">About us</a>
    <a use:link href="/contact" class="link link-hover">Contact</a>
    <a use:link href="/faq" class="link link-hover">FAQ</a>
  </nav>
  <p class="mx-auto text-center md:text-end">
    Copyright © 2024 - All right reserved by PalitasPR
  </p>
</footer>
