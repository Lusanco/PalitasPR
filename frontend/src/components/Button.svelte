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
      });
  }

  function backButton() {
    window.history.back();
    console.log("Back Button");
  }

  // Function to handle button click "Create Review"
  export function buttonLogic() {
    if (button.misc["App Location"] === "Create Review") {
      axiosLogic();
      console.log("Before IF", $response.status);
      if ($response.status === 200) {
        window.location.href = "/create-review-success";
      }
      return;
    }
    if (button.misc["App Location"] === "Crear Servicio") {
      axiosLogic();
      console.log("Before IF", $response.status);
      if ($response.status === 201) {
        window.location.href = "/create-service-success";
      }
      return;
    }
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
    if (button.misc["App Location"] === "Submit Task") {
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
    if (button.misc["App Location"] === "Delete Task") {
      axiosLogic();
      // function reloadTasks() {
      //   if (window.location.pathname === "/tasks") {
      //     window.location.reload();
      //   } else {
      //     window.location.href = "/tasks";
      //   }
      // }
      // reloadTasks();
      return;
    }
    axiosLogic();
  }
</script>

<button on:click={buttonLogic} type="button" class={button.twcss}>
  {button.name}
  <slot />
</button>
