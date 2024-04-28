<script>
  import { onMount } from "svelte";
  import { currentView } from "../src/scripts/viewManager.js";
  import Template from "./components/Template.svelte";
  import LogIn from "./components/LogIn.svelte";
  import SignUp from "./components/SignUp.svelte";
  import LandingPage from "./components/LandingPage.svelte";
  import Feed from "./components/Feed.svelte";
  import Profile from "./components/Profile.svelte";

  onMount(() => {
    currentView.set("LogIn");
  });
</script>

<main>
  <Template>
    {#if $currentView === "LogIn"}
      <LogIn />
    {:else if $currentView === "SignUp"}
      <SignUp />
    {:else if $currentView === "LandingPage"}
      <LandingPage />
    {:else if $currentView === "Feed"}
      <Feed />
    {:else if $currentView === "Profile"}
      <Profile />
      <!-- {:else if $currentView === "Settings"}
      <Settings />
    {:else}
      <Dashboard /> -->
    {/if}
  </Template>
</main>

<style>
</style>
