<script>
  import Link from "../components/Link.svelte";
  import { onMount } from "svelte";
  import { userSession } from "../scripts/stores";
  import axios from "axios";

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
    })
  })

  let twcss =
    "w-full h-24 md:h-32 rounded-lg text-[#1f1f1f] bg-white flex flex-col justify-center items-center font-bold shadow-md text-md md:text-2xl hover:bg-[#cc2936] hover:text-white transition duration-300 ease-in-out cursor-pointer text-center";
</script>

<head>
  <title>PalitasPR | Dashboard</title>
</head>

<div class="flex flex-col items-center justify-center h-full min-h-screen bg-base">
  <div class="flex w-full max-w-6xl">
    <div class="grid w-full grid-cols-2 grid-rows-2 gap-2 p-4 m-4 md:p-8 md:gap-3 md:m-12">
      <Link name="Create Service" {twcss} href="/create-service"></Link>
      <Link name="Create Request" {twcss} href="/create-request"></Link>
      <Link name="Tasks" {twcss} href="/inbox"></Link>
      <Link name="Profile" {twcss} href="/profile"></Link>
    </div>
  </div>
</div>
