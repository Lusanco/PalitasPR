<script>
  import axios from "axios";
  import { state, data, response } from "../scripts/stores";
  import { get, writable } from "svelte/store";

  let SDResponse = writable(null);

  export let image = null;
  export let button = {
    name: "Button Component",
    method: "Button Method",
    url: "Button URL",
    headers: "Button Headers", // "application/json"
    twcss: "Button Tailwind Styles",
    misc: { "App Location": "Name of App Location" },
  };
  function logFormData(data) {
    for (let pair of data.entries()) {
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

    const $data = get(data);
    let axiosData;
    // let headers;
    if (image || button.headers === "multipart/form-data") {
      let formData = new FormData();
      for (const key in $data) {
        formData.append(key, $data[key]);
      }
      if (image) {
        formData.append("image", image);
      }
      axiosData = formData;
    } else {
      axiosData = $data;
    }

    // Log data contents
    if (axiosData instanceof FormData) {
      logFormData(axiosData);
    } else {
      console.log("JSON Data:", axiosData);
    }

    // data.set(new FormData());
    // console.log("after data.set", $data);

    // Append image if it exists

    // Append other data as JSON
    // const jsonData = JSON.stringify($data);
    // $data.append("data", jsonData);
    // console.log("after data.set", $data);
    // Log data contents
    // logFormData(data);
    // let axiosData =
    //   image || button.headers === "multipart/form-data" ? data : $data;
    // console.log("after data.set", $data);
    // console.log("Before Axios Response Log: ", $response);
    // console.log("Before Axios Data Log: ", axiosData);
    // console.log("Before Axios Misc Log: ", button.misc);
    // console.log("Before Axios State Log: ", get(state));

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

        response.set(axiosResponse);

        console.log(".then() Response Log: ", $response);
        // console.log(".then() Data Log: ", axiosData);
        // console.log(".then() Misc Log: ", button.misc);
        // console.log(".then() State Log: ", $state);
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
        // console.log(".catch() Data Log: ", axiosData);
        // console.log(".catch() Misc Log: ", button.misc);
        // console.log(".catch() State Log: ", $state);
      });
  }

  function backButton() {
    window.history.back();
    console.log("Back Button");
  }

  // Function to handle button click
  export function buttonLogic() {
    if (button.misc["App Location"] === "Service Details") {
      axiosLogic();
      $SDResponse = get(response);
      console.log("Before IF", $SDResponse);
      if ($SDResponse.status === 200) {
        console.log("IN IF", $SDResponse);
        window.location.href = "/initial-contact-success";
      }
      console.log("After IF", $SDResponse);
      return;
    }
    if (button.misc["App Location"] === "Back Button Component") {
      backButton();
      return;
    }
    if (button.misc["App Location"] === "Tasks") {
      axiosLogic();
      function reloadTasks() {
        if (window.location.pathname === "/tasks") {
          window.location.reload();
        } else {
          window.location.href = "/tasks";
        }
      }
      reloadTasks();
      return;
    }
    axiosLogic();
  }
</script>

<button on:click={buttonLogic} type="button" class={button.twcss}>
  {button.name}
  <slot />
</button>
