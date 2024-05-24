<script>
  import UploadImage from "./UploadImage.svelte";
  import { onMount, afterUpdate } from "svelte";
  import { link } from "svelte-routing";
  import axios from "axios";
  import LoadingSpinnerFull from "./LoadingSpinnerFull.svelte";
  import townsID from "../townsID";
  import servicesID from "../servicesID";

  let imageFile = null;
  let errorMessage;

  function handleFileChange(event) {
    imageFile = event.target.files[0];
  }

  async function handleLogic() {
    if (!imageFile) {
      errorMessage = "Please select an image file";
      return;
    }

    const formDataImage = new FormData();
    formDataImage.append("image", imageFile);

    try {
      const response = await axios.post("/api/pic", formDataImage, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log("Image uploaded successfully:", response.data);
    } catch (error) {
      console.error("Error uploading image:", error);
      errorMessage = "An error occurred while uploading the image";
      console.log(formDataImage);
    }
  }
  async function handleUpload() {
    handleLogic();
  }

  // let errorMessage = "";
  const model = "Promotion";
  let title,
    serviceID,
    description,
    priceMin,
    priceMax = "";
  const towns = Object.entries(townsID);
  const services = Object.entries(servicesID);
  let town = "all";
  let service = "";

  let image = null;

  let hidden = true;
  let loaded = false;
  let reload = false;
  let error = false;

  function createLogic() {
    hidden = false;
    loaded = false;
    reload = true;
    error = false;

    const data = {
      model,
      title,
      town,
      serviceID,
      description,
      priceMin,
      priceMax,
    };

    axios
      .post("/api/dashboard/promotion-request", data)
      .then((response) => {
        loaded = true;
        reload = false;
        error = false;
        console.log(response);
        // if (response.status === 201) {
        //   window.location.href = "/success";
        // }
      })
      .catch((err) => {
        hidden = false;
        loaded = true;
        reload = false;
        error = true;
        console.log(err);
        errorMessage = err;
      });
  }

  async function handleCreate() {
    createLogic();
    // handleUpload();
  }

  onMount(() => {
    errorMessage = ""; // Clear any previous error messages on component mount
  });
  afterUpdate(() => {
    if (error) {
      const errorElement = document.getElementById("err-msg");
      errorElement.scrollIntoView({ behavior: "smooth" });
    }
  });
</script>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-teal-50 md:bg-none"
>
  <div
    class="w-full h-full max-w-2xl p-2 font-semibold rounded-lg md:shadow-lg md:p-8 bg-teal-50"
  >
    <h1 class="pt-4 text-2xl text-center md:text-3xl lg:text-4xl">
      Crear Oferta de Servicio
    </h1>
    <!-- Crear Solicitud de Servicio -->
    <div class="">
      <label for="title">Titulo de su Oferta</label>
      <input
        class="w-full"
        type="text"
        name="titulo"
        id=""
        bind:value={title}
      />
    </div>
    <div class="">
      <label for="service">Tipo de Servicio</label>
      <input class="w-full" type="text" name="service" bind:value={serviceID} />
    </div>

    <!-- Service Filter Start -->
    <label for="service">Seleccione Servicio a Brindar</label>
    <select
      name="service"
      bind:value={service}
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value="">---</option>
      {#each services as [service, id]}
        <option value={id}>{service}</option>
      {/each}
    </select>
    <!-- Service Filter End -->

    <!-- Town Filter Start -->
    <label for="town">Seleccione un Pueblo</label>
    <select
      name="town"
      bind:value={town}
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value="all">---</option>
      {#each towns as [town, id]}
        <option value={id}>{town}</option>
      {/each}
    </select>
    <!-- Town Filter End -->
    <div class="max-h-96">
      <label for="description">Descripcion de su Oferta</label>

      <textarea class="w-full min-h-20 max-h-20" name="description" id=""
      ></textarea>
    </div>
    <div>
      <label for="price-min">Precio Minimo (Opcional)</label>
      <input class="w-full" type="number" name="price-min" id="" />
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input class="w-full" type="number" name="price-max" id="" />
    </div>
    <!-- <div>
      <label for="imageInput">Subir Imagenes (Opcional)</label>
      <UploadImage></UploadImage>
    </div> -->
    <button
      on:click={handleCreate}
      type="button"
      class="w-full px-8 py-3 font-semibold bg-teal-600 rounded-md text-teal-50"
      >Crear</button
    >
  </div>
</div>
