<script>
  import axios from "axios";
  import townsID from "../townsID";
  import servicesID from "../servicesID";
  //   import { createEventDispatcher } from "svelte";
  //   const dispatch = createEventDispatcher();

  export let buttonName;
  export let locationURL;
  export let crudVERB;
  export let axiosDATA;

  //   console.log(`My axios data in child: ${axiosDATA.town}`);

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
