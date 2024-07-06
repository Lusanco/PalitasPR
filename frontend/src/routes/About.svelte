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

  let imagePath = "images/members/";
  let linkedInUrl = "https://www.linkedin.com/in/";
  let githubUrl = "https://github.com/";

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
          Sobre Nosotros
        </h1>
        <p class="text-2xl text-secondary">
          PalitasPR es un mercado para solicitar y promover servicios localmente
          en Puerto Rico. Somos un pequeño equipo de 5 desarrolladores que dio
          vida a esta aplicación como parte de un proyecto considerado como
          nuestra graduación.
        </p>
        <br />
        <br />

        <button
          on:click={scrollToTeam}
          aria-label="Scroll down"
          class="flex items-center justify-center w-10 h-10 mx-auto border-2 rounded-full shadow-lg md:hidden border-accent/90 text-accent/90 hover:border-accent hover:text-accent"
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
    <div class="mx-auto text-center lg:max-w-6xl">
      <br />
      <h1
        class="inline-block pb-8 text-3xl font-semibold tracking-wider uppercase rounded-full text-secondary"
      >
        Nuestro Equipo
      </h1>
      <!-- <Team /> -->
      <div
        class="flex flex-col items-center justify-center w-full gap-2 mt-12 md:flex-row"
      >
        <!--* Member 1 -->
        <div
          class="p-5 border-2 shadow-lg card bg-primnary text-secondary border-neutral/20"
        >
          <!--* Image -->
          <div class="flex items-center justify-center w-full">
            <img
              src="{imagePath}/Alfre.jpg"
              alt=""
              class="object-cover transition-transform duration-200 ease-in-out border-2 rounded-md w-52 h-52 border-neutral/30 hover:scale-105"
            />
          </div>
          <!--* Details -->
          <div class="mt-2 text-center">
            <h1 class="text-xl italic font-semibold text-accent">
              Luis Santiago
            </h1>
            <p class="font-semibold text-md">Lead Developer</p>
          </div>
          <!--* Action buttons -->
          <div class="flex w-full gap-2 mt-2">
            <a
              href="{linkedInUrl}lusanco/"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >LinkedIn</a
            >
            <a
              href="{githubUrl}lusanco"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >Github</a
            >
          </div>
        </div>
        <!--* Member 2 -->
        <div
          class="p-5 border-2 shadow-lg card bg-primnary text-secondary border-neutral/20"
        >
          <!--* Image -->
          <div class="flex items-center justify-center w-full">
            <img
              src="{imagePath}/Louis.jpg"
              alt=""
              class="object-cover transition-transform duration-200 ease-in-out border-2 rounded-md w-52 h-52 border-neutral/30 hover:scale-105"
            />
          </div>
          <!--* Details -->
          <div class="mt-2 text-center">
            <h1 class="text-xl italic font-semibold text-accent">Louis Toro</h1>
            <p class="font-semibold text-md">Backend Developer</p>
          </div>
          <!--* Action buttons -->
          <div class="flex w-full gap-2 mt-2">
            <a
              href="{linkedInUrl}ltoro9/"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >LinkedIn</a
            >
            <a
              href="{githubUrl}ltoro9"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >Github</a
            >
          </div>
        </div>
        <!--* Member 3 -->
        <div
          class="p-5 border-2 shadow-lg card bg-primnary text-secondary border-neutral/20"
        >
          <!--* Image -->
          <div class="flex items-center justify-center w-full">
            <img
              src="{imagePath}/Antonio.jpg"
              alt=""
              class="object-cover transition-transform duration-200 ease-in-out border-2 rounded-md w-52 h-52 border-neutral/30 hover:scale-105"
            />
          </div>
          <!--* Details -->
          <div class="mt-2 text-center">
            <h1 class="text-xl italic font-semibold text-accent">
              Antonio de Jesús
            </h1>
            <p class="font-semibold text-md">Database Developer</p>
          </div>
          <!--* Action buttons -->
          <div class="flex w-full gap-2 mt-2">
            <a
              href="{linkedInUrl}antoniofdjs/"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >LinkedIn</a
            >
            <a
              href="{githubUrl}antoniofdjs"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >Github</a
            >
          </div>
        </div>
      </div>
      <div
        class="flex flex-col items-center justify-center w-full gap-2 mt-4 -mb-12 md:flex-row"
      >
        <!--* Member 4 -->
        <div
          class="p-5 border-2 shadow-lg card bg-primnary text-secondary border-neutral/20"
        >
          <!--* Image -->
          <div class="flex items-center justify-center w-full">
            <img
              src="{imagePath}/Livan.jpg"
              alt=""
              class="object-cover transition-transform duration-200 ease-in-out border-2 rounded-md w-52 h-52 border-neutral/30 hover:scale-105"
            />
          </div>
          <!--* Details -->
          <div class="mt-2 text-center">
            <h1 class="text-xl italic font-semibold text-accent">
              Livan Hernandez
            </h1>
            <p class="font-semibold text-md">Frontend Developer</p>
          </div>
          <!--* Action buttons -->
          <div class="flex w-full gap-2 mt-2">
            <a
              href="{linkedInUrl}livan-hernandez-baba4a190/"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >LinkedIn</a
            >
            <a
              href="{githubUrl}livanhernandez"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >Github</a
            >
          </div>
        </div>
        <!--* Member 5 -->
        <div
          class="p-5 border-2 shadow-lg card bg-primnary text-secondary border-neutral/20"
        >
          <!--* Image -->
          <div class="flex items-center justify-center w-full">
            <img
              src="{imagePath}/Jonathan.jpg"
              alt=""
              class="object-cover transition-transform duration-200 ease-in-out border-2 rounded-md w-52 h-52 border-neutral/30 hover:scale-105"
            />
          </div>
          <!--* Details -->
          <div class="mt-2 text-center">
            <h1 class="text-xl italic font-semibold text-accent">
              Jonathan Pérez
            </h1>
            <p class="font-semibold text-md">Mobile Developer</p>
          </div>
          <!--* Action buttons -->
          <div class="flex w-full gap-2 mt-2">
            <a
              href="{linkedInUrl}prodjohnper/"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >LinkedIn</a
            >
            <a
              href="{githubUrl}prodjohnper"
              class="flex-1 transition-colors duration-200 ease-in-out border-2 btn border-accent hover:bg-accent hover:text-primary text-secondary"
              >Github</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
