<!-- Revised: Livan - Instrucctions in Trello -->
<script>
  import {onMount, onDestroy} from "svelte";
  import { link } from "svelte-routing";
  let menuOpen = false;
  let menuRef;

  function toggleMenu() {
    event.stopPropagation();
    menuOpen = !menuOpen;
  }

  function handleClickOutside(event) {
    if (menuOpen && menuRef && !menuRef.contains(event.target)) {
      menuOpen = false;
    }
  }

  function handleLinkClick() {
    menuOpen = false;
  }

  onMount(() => {
    document.addEventListener("click", handleClickOutside);
  });

  onDestroy(() => {
    document.addEventListener("click", handleClickOutside);
  });
</script>

<div class="flex justify-end m-2 bg-transparent md:hidden">
  <button
    type="button"
    class="btn btn-square btn-ghost focus:outline-none"
    aria-controls="navbar-cta"
    aria-expanded={menuOpen}
    on:click={toggleMenu}
  >
    <span class="sr-only">Open main menu</span>
    <svg
      class="w-6 h-6 text-primary"
      aria-hidden="true"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 17 14"
      stroke="CurrentColor"
      
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M1 1h15M1 7h15M1 13h15"
      />
    </svg>
  </button>
</div>

<div
bind:this={menuRef}
  class={`z-50 absolute left-0 right-0 ${menuOpen ? "block" : "hidden"} md:hidden bg-transparent`}
  id="navbar-cta"
>
  <ul
    class="w-full p-4 mt-2 shadow-lg menu bg-slate-200 text-primary rounded-box"
  >
    <li>
      <a
        use:link
        href="/"
        class="hover:bg-primary hover:text-base-100"
        on:click={handleLinkClick}
        >Home</a
      >
    </li>
    <li>
      <a
        use:link
        href="/aboutus"
        class="hover:bg-primary hover:text-base-100"
        on:click={handleLinkClick}
        >About Us</a
      >
    </li>
    <li>
      <a
        use:link
        href="/services"
        class="hover:bg-primary hover:text-base-100"
        on:click={handleLinkClick}
        >Services</a
      >
    </li>
    <li>
      <a
        use:link
        href="/contact"
        class="mb-1 hover:bg-primary hover:text-base-100"
        on:click={handleLinkClick}
        >Contact</a
      >
    </li>
    <!-- Hide these items on medium and larger screens -->
    <li class="md:hidden">
      <a
        use:link
        href="/login"
        class="w-full mb-1 btn btn-primary"
        on:click={handleLinkClick}
        >Sign In</a
      >
    </li>
    <li class="md:hidden">
      <a
        use:link
        href="/signup"
        class="w-full btn btn-primary"
        on:click={handleLinkClick}
        >Sign Up</a
      >
    </li>
  </ul>
</div>
