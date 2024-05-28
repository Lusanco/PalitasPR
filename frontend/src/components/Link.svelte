<!-- Link Component -->
<script>
  import { link } from "svelte-routing";

  export let linkNAME;
  export let classLIST;
  export let href;
</script>

<!-- Link Start -->
<li class={"list-none " + classLIST}>
  <a rel="noopener noreferrer" use:link {href}
    >{linkNAME}
    <slot />
  </a>
</li>
<!-- Link End -->
