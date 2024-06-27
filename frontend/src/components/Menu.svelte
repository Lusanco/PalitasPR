<script>
  import { link } from "svelte-routing";
  import { userSession } from "../scripts/stores";
  import { onMount } from "svelte";
  import axios from "axios";
  import { writable } from "svelte/store";
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
  }

  function closeMenu(event) {
    // Verifica si el clic fue fuera del menú y del botón
    if (
      menuOpen &&
      !event.target.closest("#navbar-cta") &&
      !event.target.closest('button[aria-controls="navbar-cta"]')
    ) {
      menuOpen = false;
    }
  }
  let profileID = writable();

  // Agrega el evento de clic al documento
  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        profileID.set(userStatusRes.data.profile_id);
      })
      .catch((userStatusErr) => {
        console.log("User Status Err: ", userStatusErr);
      });
    document.addEventListener("click", closeMenu);

    return () => {
      document.removeEventListener("click", closeMenu);
    };
  });
</script>

<div class="flex justify-end m-2 bg-transparent">
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
  class={`z-50 bg-[#f1f1f1] fixed top-20 right-0 left-0 ${menuOpen ? "block" : "hidden"} bg-transparent md:left-auto md:w-80`}
  id="navbar-cta"
>
  <ul class="w-full p-4 shadow-lg md:w-80 menu bg-[#f1f1f1] rounded-box">
    <li>
      <a
        use:link
        href="/"
        class="block px-5 py-4 text-[#1f1f1f] rounded hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        on:click|preventDefault={toggleMenu}>Home</a
      >
    </li>
    <li>
      <a
        use:link
        href="/dashboard"
        class="block px-5 py-4 text-[#1f1f1f] rounded hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        on:click|preventDefault={toggleMenu}>Dashboard</a
      >
    </li>
    <li>
      <a
        use:link
        href={`/profile/${$profileID}`}
        class="block px-5 py-4 text-[#1f1f1f] rounded hover:bg-[#cc2936] hover:text-[#f1f1f1]"
        on:click|preventDefault={toggleMenu}>Profile</a
      >
    </li>
    <li class="">
      <a
        use:link
        on:click={() => {
          axios
            .get("/api/user/logout")
            .then((logoutRes) => {
              if (window.location.pathname === "/") {
                window.location.reload();
              } else {
                window.location.href = "/";
              }
              console.log(logoutRes);
            })
            .catch((logoutErr) => {
              console.log(logoutErr);
            });
        }}
        href="/"
        class="mt-2 block px-4 py-3 text-sm font-medium text-center text-white bg-[#cc2936] hover:text-gray-800 rounded-lg"
        on:click|preventDefault={toggleMenu}>Logout</a
      >
    </li>
  </ul>
</div>
