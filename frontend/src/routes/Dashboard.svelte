<script>
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";
  import { Link } from "svelte-routing";

  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
      })
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log(userStatusErr);
        console.log($userSession);
      });
  });

  let twcss =
    "w-full h-24 md:h-32 rounded-lg text-[#1f1f1f] bg-white flex flex-col justify-center items-center font-bold shadow-md text-md md:text-2xl hover:bg-[#cc2936] hover:text-white transition duration-300 ease-in-out cursor-pointer text-center";
</script>

<head>
  <title>PalitasPR | Dashboard</title>
</head>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-base"
>
  <div class="flex w-full max-w-6xl">
    <div
      class="grid w-full grid-cols-2 grid-rows-2 gap-2 p-4 m-4 md:p-8 md:gap-3 md:m-12"
    >
      <Link
        class="w-full h-24 md:h-32 rounded-lg text-[#1f1f1f] bg-white flex flex-col justify-center items-center font-bold shadow-md text-md md:text-2xl hover:bg-[#cc2936] hover:text-white transition duration-300 ease-in-out cursor-pointer text-center"
        to="/create-service">Create Service</Link
      >
      <Link
        class="w-full h-24 md:h-32 rounded-lg text-[#1f1f1f] bg-white flex flex-col justify-center items-center font-bold shadow-md text-md md:text-2xl hover:bg-[#cc2936] hover:text-white transition duration-300 ease-in-out cursor-pointer text-center"
        to="/create-request">Create Request</Link
      >
      <Link
        class="w-full h-24 md:h-32 rounded-lg text-[#1f1f1f] bg-white flex flex-col justify-center items-center font-bold shadow-md text-md md:text-2xl hover:bg-[#cc2936] hover:text-white transition duration-300 ease-in-out cursor-pointer text-center"
        to="/tasks">Tasks</Link
      >
      <Link
        class="w-full h-24 md:h-32 rounded-lg text-[#1f1f1f] bg-white flex flex-col justify-center items-center font-bold shadow-md text-md md:text-2xl hover:bg-[#cc2936] hover:text-white transition duration-300 ease-in-out cursor-pointer text-center"
        to="/profile">Profile</Link
      >
    </div>
  </div>
</div>
