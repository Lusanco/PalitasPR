<!-- List Component -->
<script>
  import Link from "svelte-routing";

  export let classUL;
  export let linksARRAY;
  export let classLINKS;
</script>

<!-- List Start -->
<ul class={classUL}>
  {#each Object.entries(linksARRAY) as [key, value]}
    <Link class={classLINKS[key]} to={value}>{key}</Link>
  {/each}
</ul>
<!-- List End -->
