<!-- List Component -->
<script>
  import Link from "./Link.svelte";

  export let classUL = "menu bg-neutral w-56 p-2 rounded-box";
  export let linksARRAY;
  export let classLINKS = {
    home: "menu-item",
    about: "menu-item",
    contact: "menu-item",
  };
</script>

<!-- List Start -->
<ul class={classUL}>
  {#each Object.entries(linksARRAY) as [key, value]}
    <Link name={key} twcss={classLINKS[key]} href={value} />
  {/each}
</ul>
<!-- List End -->