<!-- Revised: Livan - Instrucctions in Trello -->
<script>
  import { link } from "svelte-routing";
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
  }
</script>

<div class="flex justify-end bg-transparent md:hidden">
  <button
    type="button"
    class="inline-flex items-center justify-center w-16 h-16 p-2 text-sm text-teal-600 rounded-lg hover:text-teal-400 focus:outline-none focus:ring-0"
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
  class={`absolute left-0 right-0 ${menuOpen ? "block" : "hidden"} md:hidden bg-transparent`}
  id="navbar-cta"
>
  <ul
    class="flex flex-col p-2 mt-1 space-y-2 font-medium rounded-lg rtl:space-x-reverse"
  >
    <li>
      <a
        use:link
        href="/"
        class="block px-3 py-2 text-teal-600 rounded hover:bg-teal-800 hover:text-gray-200 dark:text-teal-100 dark:hover:bg-teal-700 dark:hover:text-teal-100"
        >Home</a
      >
    </li>
    <li>
      <a
        use:link
        href="/aboutus"
        class="block px-3 py-2 text-teal-600 rounded hover:bg-teal-800 hover:text-gray-200 dark:text-teal-100 dark:hover:bg-teal-700 dark:hover:text-teal-100"
        >About Us</a
      >
    </li>
    <li>
      <a
        use:link
        href="/services"
        class="block px-3 py-2 text-teal-600 rounded hover:bg-teal-800 hover:text-gray-200 dark:text-teal-100 dark:hover:bg-teal-700 dark:hover:text-teal-100"
        >Services</a
      >
    </li>
    <li>
      <a
        use:link
        href="/contact"
        class="block px-3 py-2 text-teal-600 rounded hover:bg-teal-800 hover:text-gray-200 dark:text-teal-100 dark:hover:bg-teal-700 dark:hover:text-teal-100"
        >Contact</a
      >
    </li>
    <!-- Hide these items on medium and larger screens -->
    <li class="md:hidden">
      <a
        use:link
        href="/login"
        class="block px-4 py-2 text-sm font-medium text-center text-white bg-teal-400 rounded-lg hover:bg-teal-500 focus:ring-4 focus:outline-none focus:ring-teal-300"
        >Sign In</a
      >
    </li>
    <li class="md:hidden">
      <a
        use:link
        href="/signup"
        class="block px-4 py-2 text-sm font-medium text-center text-white bg-teal-400 rounded-lg hover:bg-teal-500 focus:ring-4 focus:outline-none focus:ring-teal-300"
        >Sign Up</a
      >
    </li>
  </ul>
</div>
