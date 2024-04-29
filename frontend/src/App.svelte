<script>
  import { onMount } from "svelte";
  import { currentView } from "../src/scripts/viewManager.js";
  import Template from "./components/Template.svelte";
  import Feed from "./components/Feed.svelte";
  import Profile from "./components/Profile.svelte";
  import Login from "./components/Login.svelte";
  import SearchBarPage from "./components/SearchBarPage.svelte";
  import Signup from "./components/Signup.svelte";

  onMount(() => {
    currentView.set("SearchBarPage");
  });
</script>

<Template>
  {#if $currentView === "Login"}
    <Login />
  {:else if $currentView === "Signup"}
    <Signup />
  {:else if $currentView === "SearchBarPage"}
    <SearchBarPage />
  {:else if $currentView === "Feed"}
    <Feed />
  {:else if $currentView === "Profile"}
    <Profile />
  {/if}
</Template>

<style>
</style>
