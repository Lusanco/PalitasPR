<script>
  import { changeView } from "../scripts/viewManager.js";
</script>

<main>
  <div class="flex justify-between p-3 navbar bg-base-200">
    <div class="ml-4">
      <a class="text-xl" href="/">Logo</a>
    </div>
    <div>
      <ul class="flex flex-row gap-6">
        <li>
          <button on:click={() => changeView("LandingPage")}>Home</button>
        </li>
        <li><button on:click={() => changeView("Feed")}>Feed</button></li>
        <li><button on:click={() => changeView("Profile")}>Profile</button></li>
      </ul>
    </div>
    <div class="mr-2">
      <a class="btn" href="/"> <i class="fas fa-bars"></i></a>
    </div>
  </div>
</main>

<style></style>
