<script>
  export let memberNAME;
  export let memberROLE;
  export let imageSRC;
  export let imageALT;
  export let classLIST;
</script>

<div class={classLIST.classDiv1}>
  <img class={classLIST.classImg} src={imageSRC} alt={imageALT} />
  <div class={classLIST.classDiv2}>
    <p class={classLIST.classP1}>{memberNAME}</p>
    <p class={classLIST.classP2}>{memberROLE}</p>
  </div>
</div>

<!-- <div class="flex flex-col items-center justify-center">
  <img
    class="object-cover w-20 h-20 mb-2 rounded-full shadow"
    src="https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=3&amp;h=750&amp;w=1260"
    alt="Person"
  />
  <div class="flex flex-col items-center">
    <p class="text-lg font-bold">Luis Santiago</p>
    <p class="text-sm text-gray-800">Team Lead</p>
  </div>
</div> -->
