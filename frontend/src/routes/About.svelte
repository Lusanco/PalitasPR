<script>
  import Team from "../components/Team.svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";
  import { onMount } from "svelte";

  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
      })
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log(userStatusErr);
        console.log($userSession);
      });
  });

  function scrollToTeam() {
    const teamSection = document.getElementById("team");
    teamSection.scrollIntoView({ behavior: "smooth" });
  }
</script>

<div class="w-full my-20 scroll-smooth">
  <div class="relative h-[32rem]">
    <div class="absolute inset-x-0 bottom-0">
      <svg
        viewBox="0 0 224 12"
        fill="currentColor"
        class="w-full -mb-1 bg-transparent shadow-2xl text-accent"
        preserveAspectRatio="none"
      >
        <path
          d="M0,0 C48.8902582,6.27314026 86.2235915,9.40971039 112,9.40971039 C137.776408,9.40971039 175.109742,6.27314026 224,0 L224,12.0441132 L0,12.0441132 L0,0 Z"
        ></path>
      </svg>
    </div>
    <div
      class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
    >
      <div
        class="relative max-w-2xl sm:mx-auto sm:max-w-xl md:max-w-2xl sm:text-center"
      >
        <h1
          class="mb-10 text-5xl font-bold tracking-tight text-center text-accent sm:text-4xl sm:leading-none"
        >
          About Us
        </h1>
        <p class="text-2xl text-secondary">
          PalitasPR is a marketplace for requesting and promoting services
          locally in PR. We are a small team of 5 developers that gave life to
          this app for an event considered our graduation project.
        </p>
        <br />
        <br />

        <button
          on:click={scrollToTeam}
          aria-label="Scroll down"
          class="flex items-center justify-center w-10 h-10 mx-auto border-2 rounded-full shadow-lg md:hidden border-accent text-accent"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="12"
            height="12"
            viewBox="0 0 12 12"
            fill="currentColor"
          >
            <path
              d="M10.293,3.293,6,7.586,1.707,3.293A1,1,0,0,0,.293,4.707l5,5a1,1,0,0,0,1.414,0l5-5a1,1,0,1,0-1.414-1.414Z"
            ></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
  <div
    id="team"
    class="px-4 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
  >
    <br />
    <div class="mx-auto text-center lg:max-w-xl">
      <br />
      <h1
        class="inline-block pb-8 text-3xl font-semibold tracking-wider uppercase rounded-full text-secondary"
      >
        Our Team
      </h1>
      <Team />
    </div>
  </div>
</div>
