<script>
  import { link } from "svelte-routing";
  import { userSession } from "../scripts/stores";
  import { onMount } from "svelte";
  import axios from "axios";
  import { writable } from "svelte/store";

  let detailsOpen = writable(false);
  let menuOpen = false;

  function toggleMenu() {
    menuOpen = !menuOpen;
  }

  function closeMenu(event) {
    if (
      menuOpen &&
      !event.target.closest("#navbar-cta") &&
      !event.target.closest('button[aria-controls="navbar-cta"]')
    ) {
      menuOpen = false;
    }
  }

  function closeDetails() {
    detailsOpen.set(false);
  }

  function handleLinkClick(event) {
    // Allow navigation to happen first
    setTimeout(() => {
      toggleMenu();
      closeDetails();
      handleHomeClick();
    }, 0);
  }

  let profileID = writable();

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

  function handleHomeClick(event) {
    event.preventDefault();
    if (window.location.pathname === "/") {
      window.location.reload();
    } else {
      window.location.href = "/";
    }
  }
</script>

<div class="flex justify-end w-full m-2 bg-tranparent">
  <button
    type="button"
    class="inline-flex items-center justify-center w-20 h-20 rounded-lg"
    aria-controls="navbar-cta"
    aria-expanded={menuOpen}
    on:click={toggleMenu}
  >
    <span class="sr-only">Open main menu</span>
    <i class="text-2xl fa-solid fa-bars text-accent"></i>
  </button>
</div>

<div
  class={`z-50 bg-white fixed top-20 rounded-2xl right-0 left-0 ${menuOpen ? "block" : "hidden"} md:left-auto md:w-80`}
  id="navbar-cta"
>
  <ul
    class="w-full p-4 text-xl font-semibold shadow-xl md:w-80 menu bg-whte rounded-box"
  >
    <li>
      <a
        use:link
        href="/"
        class="block gap-2 px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
        on:click={handleLinkClick}
        on:click={handleHomeClick}
        ><i class="mr-2 fa-solid fa-house text-accent group-hover:text-primary"
        ></i> Home</a
      >
    </li>
    <li>
      <a
        use:link
        href="/dashboard"
        class="block px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
        on:click={handleLinkClick}
        ><i
          class="mr-2 fa-solid fa-table-columns text-accent group-hover:text-primary"
        ></i> Dashboard</a
      >
    </li>
    <li>
      <a
        use:link
        href={`/profile/${$profileID}`}
        class="block px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
        on:click={handleLinkClick}
        ><i class="mr-2 fa-solid fa-user text-accent group-hover:text-primary"
        ></i> Profile</a
      >
    </li>
    <li>
      <details bind:open={$detailsOpen}>
        <summary
          class="px-5 py-3 rounded text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
          >More</summary
        >
        <ul>
          <li>
            <a
              use:link
              href={`/terms-of-use`}
              class="block px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
              on:click={handleLinkClick}
              ><i
                class="mr-2 fa-solid fa-book text-accent group-hover:text-primary"
              ></i> Terms of Use</a
            >
          </li>
          <li>
            <a
              use:link
              href={`/about`}
              class="block px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
              on:click={handleLinkClick}
              ><i
                class="mr-2 fa-solid fa-circle-info text-accent group-hover:text-primary"
              ></i> About us</a
            >
          </li>
          <li>
            <a
              use:link
              href={`/privacy`}
              class="block px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
              on:click={handleLinkClick}
              ><i
                class="mr-2 fa-solid fa-lock text-accent group-hover:text-primary"
              ></i> Privacy</a
            >
          </li>
          <li>
            <a
              use:link
              href={`/contact`}
              class="block px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
              on:click={handleLinkClick}
              ><i
                class="mr-2 fa-solid fa-envelope text-accent group-hover:text-primary"
              ></i> Contact</a
            >
          </li>
          <li>
            <a
              use:link
              href={`/faq`}
              class="block px-5 py-3 rounded group text-secondary hover:bg-accent hover:bg-opacity-90 hover:text-primary"
              on:click={handleLinkClick}
              ><i
                class="mr-2 fa-solid fa-circle-question text-accent group-hover:text-primary"
              ></i> FAQ</a
            >
          </li>
        </ul>
      </details>
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
        class="block px-4 py-3 mt-2 text-xl font-semibold text-center rounded-md text-primary bg-accent hover:bg-green-900"
        on:click={handleLinkClick}>Logout</a
      >
    </li>
  </ul>
</div>
