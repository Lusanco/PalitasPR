<script>
  export let memberNAME;
  export let memberROLE;
  export let imageSRC;
  export let imageALT;
  export let classLIST;
</script>

<div class={classLIST.classDiv1}>
  <div class="h-2/3">
    <img class={classLIST.classImg} src={imageSRC} alt={imageALT} />
  </div>
  <div class={classLIST.classDiv2}>
    <p class={classLIST.classP1}>{memberNAME}</p>
    <p class={classLIST.classP2}>{memberROLE}</p>
  </div>
</div>
