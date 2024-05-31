<script>
  import axios from "axios";

  export let axiosDATA;
  export let buttonDATA = {
    name: "",
    twcss: "",
    verb: "",
    url: "",
    headers: {},
  };
  // export let buttonCSS;
  // export let buttonNAME;
  // export let classLIST;
  // export let locationURL;
  // export let crudVERB;
  // export let headerTYPE;

  //   State Control Variables
  let hidden = true;
  let loaded = false;
  let reload = false;
  let error = false;

  function buttonLogic() {
    hidden = false;
    loaded = false;
    reload = true;
    error = false;
    if (buttonDATA.url && buttonDATA.verb) {
      axios({
        method: buttonDATA.verb,
        url: buttonDATA.url,
        data: axiosDATA,
        headers: buttonDATA.headers,
      })
        .then((response) => {
          loaded = true;
          reload = false;
          error = false;
          console.log(".then() Response Log: ", response);
          console.log(".then() Data Log: ", axiosDATA);
        })
        .catch((err) => {
          hidden = false;
          loaded = true;
          reload = false;
          error = true;
          console.log(".catch() Error Log: ", err);
          console.log(".catch() Data Log: ", axiosDATA);
        });
    } else {
      function scrollToTeam() {
        const teamSection = document.getElementById("team");
        teamSection.scrollIntoView({ behavior: "smooth" });
      }
      scrollToTeam();
    }
  }
</script>

<button on:click={buttonLogic} type="button" class={buttonDATA.twcss}>
  {buttonDATA.name}
  <slot />
</button>
