<script>
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let buttonName;
  export let locationURL;
  export let crudVERB;
  export let axiosDATA;

  import axios from "axios";
  import townsID from "../townsID";
  import servicesID from "../servicesID";

  let errorMessage;
  let title, town, serviceID, description, priceMin, priceMax;
  const towns = Object.entries(townsID);
  const services = Object.entries(servicesID);
  let service = "";

  //   State Control Variables
  let hidden = true;
  let loaded = false;
  let reload = false;
  let error = false;
  let data;
  console.log(`My data axios: ${axiosDATA} here`);
  //   console.log(axiosDATA);

  function createLogic() {
    hidden = false;
    loaded = false;
    reload = true;
    error = false;

    axios({
      method: crudVERB,
      url: locationURL,
      data: data,
    })
      .then((response) => {
        // Handle successful response
        console.log(response.data);
      })
      .catch((error) => {
        // Handle error
        console.error(error);
      });
  }

  //   if (crudVERB) {
  //     console.log(crudVERB);
  //     console.log(axiosDATA);
  //   }
  function clickedEvent(event) {
    dispatch("clicked", { eventResponse: axiosDATA });
    console.log();
  }
</script>

<button
  on:click={clickedEvent}
  type="button"
  class="px-8 py-3 font-semibold text-teal-100 bg-teal-800 rounded">Test</button
>
