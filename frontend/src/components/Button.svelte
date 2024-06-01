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
    state.hidden = false;
    state.loaded = false;
    state.reload = true;
    state.error = false;

    axios({
      method: buttonDATA.method,
      url: buttonDATA.url,
      data: axiosDATA,
      headers: buttonDATA.headers,
    })
      .then((response) => {
        state.hidden = false;
        state.loaded = true;
        state.reload = false;
        state.error = false;

        dispatch("results", {
          success: true,
          data: response.data.results,
          state: state,
        });

        console.log(".then() Response Log: ", response);
        console.log(".then() Data Log: ", axiosDATA);
        console.log(".then() Misc Log: ", miscDATA);
        console.log(".then() State Log: ", state);
      })
      .catch((err) => {
        state.hidden = false;
        state.loaded = true;
        state.reload = false;
        state.error = true;

        dispatch("results", {
          success: false,
          err: err,
          state: state,
        });

        console.log(".catch() Error Log: ", err);
        console.log(".catch() Data Log: ", axiosDATA);
        console.log(".catch() Misc Log: ", miscDATA);
        console.log(".catch() State Log: ", state);
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
