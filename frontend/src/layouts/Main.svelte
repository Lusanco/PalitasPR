<!-- Main Layout -->
<script>
  import Menu from "../components/Menu.svelte";
  import Button from "../components/Button.svelte";

  // Button Prop Variables And Dependencies
  let image = null;
  let button = {
    name: "",
    method: "",
    url: "",
    headers: "",
    twcss:
      "flex flex-col absolute items-center justify-center w-16 h-16 p-2 text-sm text-teal-600 rounded-lg hover:bg-teal-700 hover:text-teal-200 focus:outline-none focus:ring-0 m-2 z-50",
    misc: { "App Location": "Back Button Component" },
  };
  // Button Prop Variables And Dependencies
</script>

<!-- Main Start -->
<main class="min-h-full overflow-y-scroll element">
  <!-- <Button {image} {button}>
    <span class="sr-only">Go back</span>
    <svg
      class="w-5 h-5"
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
  </Button> -->
  <Menu></Menu>
  <slot />
</main>
<!-- Main End -->
