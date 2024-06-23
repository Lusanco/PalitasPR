<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { writable } from "svelte/store";

  let testData = writable(null);
  let objs, objs2;

  onMount(() => {
    axios.get("/api/testing").then((test1) => {
      testData.set(test1.data);
      console.table($testData);
      objs = $testData.results.sent;
      objs2 = $testData.results.received;
    });
  });
</script>

<!-- objs = $testData.results.sent -->
<!-- each -->
{#if $testData}
  <!-- {#each $testData.results as data}
    <h1>{data.sent.age}</h1>
  {/each} -->
  {#each objs2 as obj}
    <h1>{obj.name}</h1>
  {/each}
{/if}
