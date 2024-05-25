<script>
  import axios from "axios";

  export let buttonName;
  export let locationURL;
  export let crudVERB;
  export let axiosDATA;

  //   State Control Variables
  let hidden = true;
  let loaded = false;
  let reload = false;
  let error = false;

  //   console.log(axiosDATA);
  function buttonLogic() {
    hidden = false;
    loaded = false;
    reload = true;
    error = false;
    axios({
      method: crudVERB,
      url: locationURL,
      data: axiosDATA,
    })
      .then((response) => {
        loaded = true;
        reload = false;
        error = false;
        console.log(response);
        console.log(axiosDATA);
      })
      .catch((err) => {
        hidden = false;
        loaded = true;
        reload = false;
        error = true;
        console.log(axiosDATA);
      });
  }
</script>

<button
  on:click={buttonLogic}
  type="button"
  class="px-8 py-3 font-semibold text-teal-100 bg-teal-800 rounded"
  >{buttonName}</button
>
