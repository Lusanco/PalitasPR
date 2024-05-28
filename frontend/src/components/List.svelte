<script>
  import { link } from "svelte-routing";

  export let classUL;
  export let linksARRAY;
  export let classLINKS;

  let rel = "noopener noreferrer";
</script>

<ul class={classUL}>
  {#each Object.entries(linksARRAY) as [key, value]}
    <li class={classLINKS[key]}>
      <a {rel} use:link href={value}>{key}</a>
    </li>
  {/each}
</ul>
