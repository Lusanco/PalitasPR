<script>
  import axios from "axios";
  import { state, data, image } from "../scripts/stateStores";
  import { get } from "svelte/store";

  export let button = {
    name: "",
    method: "",
    url: "",
    headers: {},
    twcss: "",
    misc: {},
  };

  function logFormData(formData) {
    for (let pair of formData.entries()) {
      console.log(pair[0] + ": " + pair[1]);
    }
  }

  // Function to handle Axios logic
  function axiosLogic() {
    // Update state for loading/error handling
    state.update((s) => ({
      ...s,
      hidden: false,
      loaded: false,
      reload: true,
      error: false,
    }));

    let formData = new FormData();
    const $image = get(image);
    const $data = get(data);

    // Append image if it exists
    if ($image) {
      formData.append("image", $image);
    }

    // Append other data as JSON
    const jsonData = JSON.stringify($data);
    formData.append("data", jsonData);

    // Log formData contents
    logFormData(formData);

    // Make the Axios request
    axios({
      method: button.method,
      url: button.url,
      data: formData,
      headers: button.headers,
    })
      .then((response) => {
        state.update((s) => ({
          ...s,
          hidden: false,
          loaded: true,
          reload: false,
          error: false,
        }));

        console.log(".then() Response Log: ", response);
        console.log(".then() Data Log: ", formData);
        console.log(".then() Misc Log: ", button.misc);
        console.log(".then() State Log: ", get(state));
      })
      .catch((err) => {
        state.update((s) => ({
          ...s,
          hidden: false,
          loaded: true,
          reload: false,
          error: true,
        }));

        console.log(".catch() Error Log: ", err);
        console.log(".catch() Data Log: ", formData);
        console.log(".catch() Misc Log: ", button.misc);
        console.log(".catch() State Log: ", get(state));
      });
  }

  // Function to handle button click
  export function buttonLogic() {
    axiosLogic();
  }
</script>

<button on:click={buttonLogic} type="button" class={button.twcss}>
  {button.name}
  <slot />
</button>
