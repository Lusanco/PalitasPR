<!-- Main Layout -->
<script>
  import Menu from "../components/Menu.svelte";
  import Button from "../components/Button.svelte";
  import { userSession } from "../../scripts/stores";

  // Button Prop Variables And Dependencies
  let image = null;
  let button = {
    name: "",
    method: "",
    url: "",
    headers: "",
    twcss:
      "flex flex-col absolute items-center justify-center shadow-none w-16 h-16 btn btn-sm border-none text-secondary rounded-lg hover:bg-accent hover:text-primary focus:outline-none focus:ring-0 m-2 z-50",
    misc: { "App Location": "Back Button Component" },
  };
  // Button Prop Variables And Dependencies
</script>

<!-- Main Start -->
<main class="min-h-full overflow-y-scroll element">
  <div class={`${$userSession ? "" : "hidden"}`}>
    <Button {image} {button}>
      <span class="sr-only">Go back</span>
      <i class="text-md fa-solid fa-chevron-left"></i>
    </Button>
  </div>
  <div class={`${$userSession ? "" : "hidden"}`}>
    <Menu></Menu>
  </div>
  <slot />
</main>
<!-- Main End -->
