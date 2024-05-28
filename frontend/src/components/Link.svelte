<!-- Link Component -->
<script>
  import { link } from "svelte-routing";

  export let linkNAME;
  export let classLIST;
  export let href;

  let rel = "noopener noreferrer";
</script>

<!-- Link Start -->
<li class={"list-none " + classLIST}>
  <a {rel} use:link {href}
    >{linkNAME}
    <slot />
  </a>
</li>
<!-- Link End -->
