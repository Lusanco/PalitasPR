<script>
  import { link } from "svelte-routing";
  import { userSession } from "../scripts/stores";
</script>

<footer
  class={$userSession
    ? `hidden`
    : `` +
      " flex flex-wrap  text-primary justify-between p-5 md:p-8 footer font-semibold bg-accent"}
>
  <nav
    class="flex flex-wrap items-center justify-center gap-2 mx-auto -mb-5 md:gap-4 md:mx-0"
  >
    <a
      use:link
      href="/terms-of-use"
      rel="noopener noreferrer"
      class="link link-hover">Terms of Use</a
    >

    <a
      use:link
      href="/privacy"
      rel="noopener noreferrer"
      class="link link-hover">Privacy</a
    >
    <a use:link href="/about" rel="noopener noreferrer" class="link link-hover"
      >About us</a
    >
    <a
      use:link
      href="/contact"
      rel="noopener noreferrer"
      class="link link-hover">Contact</a
    >
    <a use:link href="/faq" rel="noopener noreferrer" class="link link-hover"
      >FAQ</a
    >
  </nav>
  <p class="mx-auto text-center md:mx-0 md:text-end">
    Copyright © 2024 - All right reserved by PalitasPR
  </p>
</footer>
