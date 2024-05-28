<script>
  import axios from "axios";

  export let buttonNAME;
  export let classLIST;
  export let locationURL;
  export let crudVERB;
  export let axiosDATA;
  export let headerTYPE;

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
    axios({
      method: crudVERB,
      url: locationURL,
      data: axiosDATA,
      headers: headerTYPE,
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
  }
</script>

<button on:click={buttonLogic} type="button" class={classLIST}
  >{buttonNAME}</button
>
