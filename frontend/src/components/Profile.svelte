<script>
  import { onMount } from "svelte";
  import { changeView } from "../scripts/viewManager.js";

  onMount(() => {
    changeView("Profile");
  });
  // Profile data
  let profile = {
    name: "Jennifer Doe",
    occupation: "Nail Technician at Nail Salon",
    rating: "4.5",
    posts: [
      {
        content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        date: "April 20, 2024",
      },
      {
        content:
          "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        date: "April 21, 2024",
      },
      {
        content:
          "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        date: "April 22, 2024",
      },
      {
        content:
          "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        date: "April 23, 2024",
      },
    ],
  };
</script>

<div class="container relative flex flex-col h-full mt-6">
  <div class="absolute inset-x-0 top-0 z-10 w-full rounded-2xl banner"></div>

  <div class="grid grid-cols-1 gap-4 Profile">
    <!-- Profile Info -->
    <div class="relative z-20 p-2 rounded-lg mt-44 ProfileContainer">
      <img
        src="https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        alt="Profile"
        class="relative z-20 w-32 h-32 mx-auto mb-4 bg-white rounded-full ProfilePic"
      />
      <div
        class="absolute bottom-0 left-0 flex justify-center w-full pb-[5rem]"
      >
        <button
          class="z-30 RatingsBtn btn btn-sm bg-[#00B59F] text-[#E9ECEC] border-none"
          ><i class="fas fa-star"></i>{profile.rating}</button
        >
      </div>
      <h1 class="mb-2 text-2xl font-bold text-center text-[#E9ECEC]">
        {profile.name}
      </h1>
      <p class="text-center text-gray-500">{profile.occupation}</p>
    </div>
    <div class="flex justify-center gap-4 ProfileBtns">
      <button class="w-full btn"> Follow </button>
      <button class="w-full btn"> Inbox </button>
    </div>
    <div class="w-full pb-2 mx-2 border-b-[3px] opacity-10"></div>

    <!-- Posts -->
    <div class="grid grid-cols-1 gap-4 Posts">
      {#each profile.posts as post}
        <div class="p-4 bg-[#E9ECEC] rounded-lg shadow-md">
          <p class="mb-2 text-gray-800">{post.content}</p>
          <p class="text-gray-500">{post.date}</p>
        </div>
      {/each}
    </div>
  </div>
</div>

<style>
  /* Add custom styles here */
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: calc(100vh - 4.7rem - 4.7rem);
  }

  /* Adjust the position and size of the banner */
  .banner {
    display: flex;
    justify-self: start;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 250px;
    background-image: url("https://images.pexels.com/photos/1577882/pexels-photo-1577882.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    background-position: center;
    z-index: -1; /* Ensure the banner stays behind other content */
  }

  .Profile {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .ProfilePic {
    border: 6px solid #fff;
  }

  .RatingsBtn {
    padding: 0.5rem 1rem;
    font-size: 0.6rem;
  }

  .ProfileBtns {
    width: 49.2%;
  }

  /* Update Posts styles for single column */
  .Posts {
    grid-template-columns: 2fr 2fr; /* Set grid to have one column */
  }
</style>
