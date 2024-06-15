<script>
  import Link from "../components/Link.svelte";

  let twcss =
    "w-full h-24 md:h-32 rounded-lg text-stone-600 bg-stone-300  flex flex-col justify-center items-center font-bold shadow-md text-md md:text-2xl hover:bg-stone-400 hover:text-stone-700 transition duration-300 ease-in-out cursor-pointer text-center";
</script>

<head>
  <title>PalitasPR | Dashboard</title>
</head>
<div class="flex flex-col items-center justify-center h-full min-h-screen">
  <div class="flex w-full">
    <div
      class="grid w-full grid-cols-2 grid-rows-2 gap-2 p-4 m-4 md:p-8 md:gap-3 md:m-12"
    >
      <Link name="Create Service" {twcss} href="/create-service"></Link>
      <Link name="Create Request" {twcss} href="/create-request"></Link>
      <Link name="Manage Services" {twcss} href="/manage-services"></Link>
      <Link name="Manage Requests" {twcss} href="/manage-requests"></Link>
      <Link name="Tasks" {twcss} href="/inbox"></Link>
      <Link name="Profile" {twcss} href="/profile"></Link>
    </div>
  </div>
</div>
