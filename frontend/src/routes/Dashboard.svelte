<script>
  import Link from "../components/Link.svelte";

  /**
   *? Button Styling
   */

  let twcss =
    "w-full h-24 md:h-32 rounded-lg bg-teal-600 flex flex-col justify-center items-center font-bold shadow-md text-white text-md md:text-2xl hover:bg-teal-700 transition duration-300 ease-in-out cursor-pointer text-center";
</script>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-slate-100"
>
  <!-- 
  * Grid
-->
  <div class="flex w-full">
    <div
      class="grid w-full grid-cols-2 grid-rows-2 gap-2 p-4 m-4 rounded-md shadow-lg md:p-8 md:gap-3 md:m-12 text bg-slate-100"
    >
      <Link name="Create Post" {twcss} href="/create-post"></Link>
      <Link name="View Offers" {twcss} href="/view-offers"></Link>
      <Link name="View Services" {twcss} href="/view-services"></Link>
      <Link name="Settings" {twcss} href="/settings"></Link>
    </div>
  </div>
</div>
