<script>
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";
  import { Link } from "svelte-routing";
  import { writable } from "svelte/store";

  let profileID = writable();

  let twcss =
    "flex flex-col items-center justify-center font-bold text-center transition-all duration-200 rounded-lg shadow-md cursor-pointer bg-white min-h-20 text-2xl md:text-4xl h-40 w-40 md:w-80 hover:bg-accent hover:text-primary";

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
        window.location.href = "/login-to-continue";
      });
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen px-2 bg-primary"
>
  <div
    class="flex flex-wrap items-center justify-center w-full max-w-3xl gap-4"
  >
    <div
      class="flex flex-wrap items-center justify-center w-full max-w-3xl gap-4"
    >
      <!--* Create Service button -->
      <Link class={twcss} to="/create-service">Create Service</Link>
      <!--* Create Request button -->
      <Link class={twcss} to="/create-request">Create Request</Link>
    </div>
    <div
      class="flex flex-wrap items-center justify-center w-full max-w-3xl gap-4"
    >
      <!--* Tasks button -->
      <Link class={twcss} to="/tasks">Tasks</Link>
      <!--* Profile button -->
      <Link class={twcss} to={`/profile/${$profileID}`}>Profile</Link>
    </div>
  </div>
</div>
