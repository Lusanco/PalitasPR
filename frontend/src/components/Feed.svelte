<!-- Feed.svelte -->

<script>
  import PostCard from "./PostCard.svelte";
  import { changeView } from "../scripts/viewManager.js";
  import { onMount } from "svelte";

  onMount(() => {
    changeView("Feed");
  });

  // Sample data for posts
  let forYouPosts = [];
  let followingPosts = [];
  let activeTab = "forYou";

  onMount(() => {
    // Fetch data for both feeds when component mounts
    // Here you would fetch data from an API or somewhere else
    forYouPosts = [
      {
        id: 1,
        author: "User1",
        rating: "4.5",
        content:
          "I need someone to lawn my garden. I have a small garden and I need someone to lawn it. I will pay $50 for the job. Please contact me if you're interested!",
      },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
      { id: 2, author: "User2", content: "Another post for you!" },
    ];
    followingPosts = [
      {
        id: 3,
        author: "User3",
        content: "This is a post from someone you're following!",
      },
      { id: 4, author: "User4", content: "Another post from a followee!" },
    ];
  });

  function switchTab(tab) {
    activeTab = tab;
  }
</script>

<div class="w-full feed-container">
  <!-- Wrap buttons in a div -->
  <div class="button-container">
    <div class="flex justify-center gap-2 mt-4">
      <button
        class="btn border-none ml-4 px-2 py-2 rounded-md bg-[#00B59F] text-white font-semibold"
        class:selected={activeTab === "forYou"}
        on:click={() => switchTab("forYou")}
      >
        Posts
      </button>
      <button
        class="btn border-none mr-4 px-2 py-2 rounded-md bg-[#00B59F] text-white font-semibold"
        class:selected={activeTab === "following"}
        on:click={() => switchTab("following")}
      >
        Contracts
      </button>
    </div>
  </div>

  <!-- Post cards section -->
  <section class="grid w-full grid-cols-1 gap-2 p-4 feed-content">
    {#if activeTab === "forYou"}
      {#each forYouPosts as post}
        <PostCard {post} />
      {/each}
    {:else if activeTab === "following"}
      {#each followingPosts as post}
        <PostCard {post} />
      {/each}
    {/if}
  </section>
</div>

<style>
  .feed-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: calc(100vh - 3.9rem - 3.9rem);
  }

  .button-container {
    width: 100%;
    /* position: sticky;
    top: 0;
    z-index: 1; */
  }

  .btn {
    width: 48.3%;
  }
</style>
