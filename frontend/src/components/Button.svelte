<script>
  import axios from "axios";
  import { state, data, response } from "../scripts/stores";
  import { get } from "svelte/store";

  export let image = null;
  export let button = {
    name: "Button Component",
    method: "Button Method",
    url: "Button URL",
    headers: "Button Headers", // "application/json"
    twcss: "Button Tailwind Styles",
    misc: { "App Location": "Name of App Location" },
  };
  function logFormData(formData) {
    for (let pair of formData.entries()) {
      console.log(pair[0] + ": " + pair[1]);
    }
  }

  // Function to handle Axios logic
  function axiosLogic() {
    const $data = get(data);

    // Update state for loading/error handling
    state.update((s) => ({
      ...s,
      hidden: false,
      loaded: false,
      reload: true,
      error: false,
    }));

    let formData = new FormData();

    // Append image if it exists
    if (image) {
      formData.append("image", image);
    }

    // Append other data as JSON
    const jsonData = JSON.stringify($data);
    formData.append("data", jsonData);

    // Log formData contents
    logFormData(formData);
    let axiosData =
      image || button.headers === "multipart/form-data" ? formData : $data;

    console.log("Before Axios Response Log: ", $response);
    console.log("Before Axios Data Log: ", axiosData);
    console.log("Before Axios Misc Log: ", button.misc);
    console.log("Before Axios State Log: ", get(state));

    // Make the Axios request
    axios({
      method: button.method,
      url: button.url,
      data: axiosData,
      headers: { "Content-Type": button.headers },
    })
      .then((axiosResponse) => {
        state.update((s) => ({
          ...s,
          hidden: false,
          loaded: true,
          reload: false,
          error: false,
        }));

        response.set(axiosResponse.data);

        console.log(".then() Response Log: ", $response);
        console.log(".then() Data Log: ", axiosData);
        console.log(".then() Misc Log: ", button.misc);
        console.log(".then() State Log: ", $state);
      })
      .catch((axiosError) => {
        state.update((s) => ({
          ...s,
          hidden: false,
          loaded: true,
          reload: false,
          error: true,
        }));

        console.log(".catch() Error Log: ", axiosError);
        console.log(".catch() Data Log: ", axiosData);
        console.log(".catch() Misc Log: ", button.misc);
        console.log(".catch() State Log: ", $state);
      });
  }

  function backButton() {
    window.history.back();
    console.log("Back Button");
  }

  // Function to handle button click
  export function buttonLogic() {
    if (button.misc["App Location"] === "Back Button Component") {
      backButton();
      return;
    }
    axiosLogic();
  }
</script>

<button on:click={buttonLogic} type="button" class={button.twcss}>
  {button.name}
  <slot />
</button>
