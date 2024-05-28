<!-- List Component -->
<script>
  import Link from "./Link.svelte";

  export let classUL;
  export let linksARRAY;
  export let classLINKS;
</script>

<!-- List Start -->
<ul class={classUL}>
  {#each Object.entries(linksARRAY) as [key, value]}
    <Link linkNAME={key} classLIST={classLINKS[key]} href={value} />
  {/each}
</ul>
<!-- List End -->
