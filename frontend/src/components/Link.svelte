<!-- Link Component -->
<script>
  import { link } from "svelte-routing";

  export let name;
  export let twcss;
  export let href;
</script>

<!-- Link Start -->
<a rel="noopener noreferrer" use:link {href}>
  <li class={"list-none " + twcss}>
    <span class="px-2">
      {name}
    </span>
    <slot />
  </li>
</a>
<!-- Link End -->
