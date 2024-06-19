<!-- Revised: Livan - Instrucctions in Trello -->
<script>
  import { link } from "svelte-routing";
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
  }
</script>

<div class="flex justify-end m-2 bg-transparent md:hidden">
  <button
    type="button"
    class="inline-flex items-center justify-center w-16 h-16 p-2 text-sm text-[#cc2936] rounded-lg hover:opacity-90 focus:outline-none focus:ring-0"
    aria-controls="navbar-cta"
    aria-expanded={menuOpen}
    on:click={toggleMenu}
  >
    <span class="sr-only">Open main menu</span>
    <svg
      class="w-5 h-5"
      aria-hidden="true"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 17 14"
    >
      <path
        stroke="currentColor"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M1 1h15M1 7h15M1 13h15"
      />
    </svg>
  </button>
</div>

<div
  class={`z-50 bg-teal-50 absolute left-0 right-0 ${menuOpen ? "block" : "hidden"} md:hidden bg-transparent`}
  id="navbar-cta"
>
  <ul
    class="z-50 flex flex-col p-2 mt-1 space-y-2 font-medium rounded-b-lg bg-slate-200 rtl:space-x-reverse"
  >
    <li>
      <a
        use:link
        href="/"
        class="block px-3 py-2 text-[#1f1f1f] rounded hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        >Home</a
      >
    </li>
    <li>
      <a
        use:link
        href="/aboutus"
        class="block px-3 py-2 text-[#1f1f1f] rounded hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        >About Us</a
      >
    </li>
    <li>
      <a
        use:link
        href="/services"
        class="block px-3 py-2 text-[#1f1f1f] rounded hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        >Services</a
      >
    </li>
    <li>
      <a
        use:link
        href="/contact"
        class="block px-3 py-2 text-[#1f1f1f] rounded hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        >Contact</a
      >
    </li>
    <!-- Hide these items on medium and larger screens -->
    <li class="md:hidden">
      <a
        use:link
        href="/login"
        class="block px-4 py-2 text-sm font-medium text-center text-white bg-[#cc2936] rounded-lg"
        >Sign In</a
      >
    </li>
    <li class="md:hidden">
      <a
        use:link
        href="/signup"
        class="block px-4 py-2 text-sm font-medium text-center text-white bg-[#cc2936] rounded-lg"
        >Sign Up</a
      >
    </li>
  </ul>
</div>
