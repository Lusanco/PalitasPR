<!-- Main Layout -->
<script>
  import Menu from "../components/Menu.svelte";
  import Button from "../components/Button.svelte";
  import { userSession } from "../scripts/stores";

  // Button Prop Variables And Dependencies
  let image = null;
  let button = {
    name: "",
    method: "",
    url: "",
    headers: "",
    twcss:
      "flex flex-col text-xl font-semibold absolute items-center justify-center shadow-none w-20 h-20 btn btn-sm border-none text-secondary rounded-2xl hover:bg-accent/50 hover:text-primary focus:outline-none focus:ring-0 m-2 z-50",
    misc: { "App Location": "Back Button Component" },
  };
  // Button Prop Variables And Dependencies
</script>

<!-- Main Start -->
<main
  class="flex flex-col items-center justify-center flex-grow w-screen min-h-full overflow-y-scroll bg-primary element"
>
  {#if $userSession || !$userSession}
    <div
      class={`${$userSession ? "flex flex-row justify-between items-stretch w-full bg-transparent px-2" : "hidden"}`}
    >
      <Button {image} {button}>
        <span class="sr-only">Go back</span>
        <i class="text-md fa-solid fa-chevron-left"></i>
      </Button>

      <Menu></Menu>
    </div>
  {/if}
  <slot />
</main>
<!-- Main End -->
