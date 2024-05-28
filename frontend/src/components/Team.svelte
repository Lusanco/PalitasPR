<script>
  import Member from "./Member.svelte";

  let teamROLES = {
    "Luis Santiago": "Lead Developer",
    "Antonio De Jesus": "Database Developer",
    "Jonathan Perez": "Mobile Developer",
    "Louis Toro": "Backend Developer",
    "Livan Hernandez": "Web Developer",
  };
  let teamCLASSLISTS = {
    classDiv1: "flex flex-col items-center justify-center w-full md:w-1/5",
    classImg: "object-cover w-20 h-20 mb-2 rounded-full shadow",
    classDiv2: "flex flex-col items-center",
    classP1: "text-lg font-bold",
    classP2: "text-sm text-gray-800",
  };
  let teamALTS = "Team Member";
  let teamSRCS = {
    "Luis Santiago":
      "https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=3&amp;h=750&amp;w=1260",
    "Antonio De Jesus":
      "https://images.pexels.com/photos/2381069/pexels-photo-2381069.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260",
    "Jonathan Perez":
      "https://images.pexels.com/photos/3785077/pexels-photo-3785077.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;w=500",
    "Louis Toro":
      "https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260",
    "Livan Hernandez":
      "https://images.pexels.com/photos/3747435/pexels-photo-3747435.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260",
  };
</script>

<div
  class="flex flex-wrap items-center justify-center min-w-full gap-6 mx-auto lg:max-w-screen-2xl"
>
  {#each Object.entries(teamROLES) as [key, value]}
    <Member
      memberNAME={key}
      memberROLE={value}
      classLIST={teamCLASSLISTS}
      imageALT={teamALTS}
      imageSRC={teamSRCS[key]}
    />
  {/each}
</div>
<!-- 
    <Member
  memberNAME="Luis Santiago"
  memberROLE="Lead Developer"
  classLIST={{
    classDiv1: "flex flex-col items-center justify-center",
    classImg: "object-cover w-20 h-20 mb-2 rounded-full shadow",
    classDiv2: "flex flex-col items-center",
    classP1: "text-lg font-bold",
    classP2: "text-sm text-gray-800",
  }}
  imageALT="Person"
  imageSRC="https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=3&amp;h=750&amp;w=1260"
/>
 -->
