<script>
  import Member from "./Member.svelte";
  import {
    teamROLES,
    teamCLASSLISTS,
    teamALTS,
    teamSRCS,
  } from "../scripts/teamMembers";
</script>

<div
  class="flex flex-col items-center justify-center w-full gap-10 mx-auto md:flex-row"
>
  {#each Object.entries(teamROLES) as [key, value]}
    <Member
      memberNAME={key}
      memberROLE={value}
      classLIST={teamCLASSLISTS}
      imageALT={teamALTS[key]}
      imageSRC={teamSRCS[key]}
    />
  {/each}
</div>
