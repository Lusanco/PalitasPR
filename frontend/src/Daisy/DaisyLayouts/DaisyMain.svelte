<!-- Main Layout -->
<script>
  import Menu from "../components/Menu.svelte";
  import Button from "../components/Button.svelte";
  import { onMount } from "svelte";

  let axiosDATA = {};
  let miscDATA = { "Back Button": true };
  let buttonDATA = {
    name: "",
    method: "",
    url: "",
    headers: {},
    twcss:
      "absolute btn btn-square btn-ghost bg-transparent m-2 z-50",
  };

  let isMobile = false;

  function updateIsMobile() {
    isMobile = window.innerWidth <= 768;
  }

  onMount(() => {
    updateIsMobile();
    window.addEventListener("resize", updateIsMobile);
    return () => {
      window.removeEventListener("resize", updateIsMobile);
    };
  });
</script>

<!-- Main Start -->
<main class="min-h-full overflow-y-scroll element">
  <Button {axiosDATA} {buttonDATA} {miscDATA}>
    <span class="sr-only">Go back</span>
    <svg
      class="w-6 h-6 $isMobile ? 'text-primary' : 'text-neutral'"
      aria-hidden="true"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M15 19l-7-7 7-7"
      />
    </svg>
  </Button>
  <Menu></Menu>
  <slot />
</main>
<!-- Main End -->
