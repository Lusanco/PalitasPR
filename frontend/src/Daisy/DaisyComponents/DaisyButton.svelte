<script>
    import axios from "axios";
    import { createEventDispatcher } from "svelte";
    import { state } from "../../scripts/stateStores";
  
    const dispatch = createEventDispatcher();
  
    export let axiosDATA = {};
    export let miscDATA = {};
    export let buttonDATA = {
      name: "",
      method: "",
      url: "",
      headers: {},
      twcss: "btn btn-primary",
    };
  
    function axiosLogic(buttonDATA, axiosDATA = {}, miscDATA = {}) {
      state.update((s) => ({
        ...s,
        hidden: false,
        loaded: false,
        reload: true,
        error: false,
      }));
  
      axios({
        method: buttonDATA.method,
        url: buttonDATA.url,
        data: axiosDATA,
        headers: buttonDATA.headers,
      })
        .then((response) => {
          setTimeout;
          state.update((s) => ({
            ...s,
            hidden: false,
            loaded: true,
            reload: false,
            error: false,
          }));
  
          dispatch("results", {
            success: true,
            data: response.data.results,
            state: $state,
          });
  
          console.log(".then() Response Log: ", response);
          console.log(".then() Data Log: ", axiosDATA);
          console.log(".then() Misc Log: ", miscDATA);
          console.log(".then() State Log: ", $state);
        })
        .catch((err) => {
          state.update((s) => ({
            ...s,
            hidden: false,
            loaded: true,
            reload: false,
            error: true,
          }));
  
          dispatch("results", {
            success: false,
            err: err,
            state: state,
          });
  
          console.log(".catch() Error Log: ", err);
          console.log(".catch() Data Log: ", axiosDATA);
          console.log(".catch() Misc Log: ", miscDATA);
          console.log(".catch() State Log: ", $state);
        });
    }
  
    function backButton() {
      window.history.back();
      console.log("Back Button");
    }
    // Expose the buttonLogic function to be callable from the parent component
    export function buttonLogic() {
      if (buttonDATA.method && buttonDATA.url) {
        axiosLogic(buttonDATA, axiosDATA, miscDATA);
      } else {
        if (miscDATA["Back Button"] === true) {
          backButton();
        }
      }
    }
  </script>
  
  <!-- on:click|preventDefault={buttonLogic} -->
  <button on:click={buttonLogic} type="button" class={buttonDATA.twcss}>
    {buttonDATA.name}
    <slot />
  </button>
  