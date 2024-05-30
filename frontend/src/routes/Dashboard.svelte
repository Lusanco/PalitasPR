<script>
  import Link from "../components/Link.svelte";
  let twcss =
    "w-40 h-40 rounded-full bg-white flex flex-col justify-center items-center font-bold";
</script>

<div
  class="flex flex-col items-center justify-center w-full h-full min-h-screen m-auto bg-purple-500"
>
  <Link name={"Test 1"} {twcss} href={"/"}></Link>
</div>
