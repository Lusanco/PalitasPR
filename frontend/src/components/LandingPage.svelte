<script>
  import { changeView } from "../scripts/viewManager.js";
  import { onMount } from "svelte";

  onMount(() => {
    changeView("LandingPage");
  });
</script>

<div class="flex items-center justify-center">
  <div class="card-container">
    <div class="card w-96 text-neutral-content bg-base-200">
      <div class="items-center text-center card-body">
        <h1 class="text-2xl text-gray-200 card-title">
          What are you searching for?
        </h1>
        <div class="flex justify-center gap-2 pt-2">
          <input
            type="text"
            class="rounded-xl bg-[#E9ECEC] placeholder:text-gray-400 text-center focus:outline-none text-gray-700"
            placeholder="Search"
          />
          <button class="btn bg-[#00B59F]"
            ><i class="fas fa-search text-[#E9ECEC]"></i></button
          >
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .card-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: calc(100vh - 3.9rem - 3.9rem);
  }
</style>
