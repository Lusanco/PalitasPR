<script>
  export let memberNAME;
  export let memberROLE;
  export let imageSRC;
  export let imageALT;
  export let classLIST = {
    classDiv1: "card shadow-lg w-full md:w-1/5",
    classImg: "object-cover rounded-full w-20 h-20 mb-2 shadow transition transform hover:scale-110 duration-300",
    classDiv2: "card-body flex flex-col items-center",
    classP1: "card-title text-lg font-bold",
    classP2: "card-text text-sm text-gray-800",
  };
</script>

<div class={classLIST.classDiv1}>
  <img class={classLIST.classImg} src={imageSRC} alt={imageALT} />
  <div class={classLIST.classDiv2}>
    <p class={classLIST.classP1}>{memberNAME}</p>
    <p class={classLIST.classP2}>{memberROLE}</p>
  </div>
</div>
