<!-- Header Layout -->
<script>
  import { link } from "svelte-routing";
  import Menu from "../components/Menu.svelte";
  import Button from "../components/Button.svelte";
  import { userSession } from "../scripts/stores";
  import { writable } from "svelte/store";

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

  // Function to handle the "PalitasPR" link click
  function handlePalitasPRClick(event) {
    event.preventDefault();
    if (window.location.pathname === "/") {
      window.location.reload();
    } else {
      window.location.href = "/";
    }
  }
</script>

{#if !$userSession}
  <!-- Header Start -->
  <header
    class={$userSession
      ? `hidden`
      : `` +
        " p-2 md:p-4 bg-white shadow-2xl shadow-black navbar border-b-2 border-accent/40"}
  >
    <div class="navbar-start">
      <a
        use:link
        on:click={handlePalitasPRClick}
        href="/"
        rel="noopener noreferrer"
        class="text-xl bg-transparent border-none hover:from-[#1f1f1f] hover:scale-110 transition-transform ease-in-out duration-200 mx-4 rounded-full"
      >
        <img class="w-24 md:w-28" src="/logoDark.svg" alt="" />
      </a>
    </div>
    <div class="gap-2 mr-4 navbar-end">
      <a
        use:link
        href="/login"
        rel="noopener noreferrer"
        class="btn w-16 md:w-24 text-base font-semibold shadow-lg text-[#f1f1f1] bg-accent hover:bg-green-900"
        >Login</a
      >
      <a
        use:link
        href="/signup"
        rel="noopener noreferrer"
        class="w-16 text-base font-semibold border-2 shadow-lg md:w-24 text-accent border-accent btn bg-primary hover:opacity-80 hover:border-accent"
        >Signup</a
      >
    </div>
  </header>
  <!-- Header End -->
{/if}
{#if $userSession}
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
