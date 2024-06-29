<script>
  import { onMount } from "svelte";
  import { userSession } from "../../scripts/stores";
  import axios from "axios";
  import { Link } from "svelte-routing";
  import { writable } from "svelte/store";

  let profileID = writable();

  let twcss =
    "flex flex-col items-center justify-center w-full h-24 font-bold text-center transition duration-200 ease-in-out rounded-lg shadow-md cursor-pointer md:h-32 text- bg-primary text-md md:text-2xl hover:bg-accent hover:text-primary";

  // Check if the user is logged in
  onMount(() => {
    axios
      // Make a GET request to the user status endpoint
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        profileID.set(userStatusRes.data.profile_id);
        console.log(userStatusRes.data);
      })
      // Catch errors
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log(userStatusErr);
        console.log($userSession);
      });
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-base"
>
  <div class="flex w-full max-w-6xl">
    <div
      class="grid w-full grid-cols-2 grid-rows-2 gap-2 p-4 m-4 md:p-8 md:gap-3 md:m-12"
    >
      <!--* Create Service button -->
      <Link class={twcss} to="/create-service">Create Service</Link>
      <!--* Create Request button -->
      <Link class={twcss} to="/create-request">Create Request</Link>
      <!--* Tasks button -->
      <Link class={twcss} to="/tasks">Tasks</Link>
      <!--* Profile button -->
      <Link class={twcss} to={`/profile/${$profileID}`}>Profile</Link>
    </div>
  </div>
</div>
