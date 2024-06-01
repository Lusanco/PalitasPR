<script>
  import axios from "axios";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let axiosDATA = {};
  export let miscDATA = {};
  export let buttonDATA = {
    name: "",
    method: "",
    url: "",
    headers: {},
    twcss: "",
  };

  //   State Control Object
  let state = {
    hidden: true,
    loaded: false,
    reload: false,
    error: false,
  };

  function axiosLogic(buttonDATA, axiosDATA = {}, miscDATA = {}) {
    state = {
      hidden: false,
      loaded: false,
      reload: true,
      error: false,
    };

    axios({
      method: buttonDATA.method,
      url: buttonDATA.url,
      data: axiosDATA,
      headers: buttonDATA.headers,
    })
      .then((response) => {
        state = {
          hidden: false,
          loaded: true,
          reload: false,
          error: false,
        };

        dispatch("results", {
          success: true,
          data: response.data.results,
          state: state,
        });

        console.log(".then() Response Log: ", response);
        console.log(".then() Data Log: ", axiosDATA);
        console.log(".then() Misc Log: ", miscDATA);
      })
      .catch((error) => {
        state = {
          hidden: false,
          loaded: true,
          reload: false,
          error: true,
        };

        dispatch("results", {
          success: false,
          error: error,
          state: state,
        });

        console.log(".catch() Error Log: ", error);
        console.log(".catch() Data Log: ", axiosDATA);
        console.log(".catch() Misc Log: ", miscDATA);
      });
  }

  function buttonLogic() {
    axiosLogic(buttonDATA, axiosDATA, miscDATA);
  }
</script>

<button
  on:click|preventDefault={buttonLogic}
  type="button"
  class={buttonDATA.twcss}
>
  {buttonDATA.name}
  <slot />
</button>
