<script>
  import townsID from "../townsID";
  import servicesID from "../servicesID";
  import Button from "./Button.svelte";

  // Data points for axiosDATA
  let model = "Promotion",
    title,
    town,
    service_id,
    description,
    price_min,
    price_max,
    imageFile,
    errorMessage;

  // For iterating town and service name and ids
  const towns = Object.entries(townsID);
  const services = Object.entries(servicesID);

  let buttonNAME = "Create Promotion";
  let locationURL = "/api/dashboard/promotion-request";
  let crudVERB = "POST";
  let headerTYPE = {
    "Content-Type": "multipart/form-data",
  };

  let axiosDATA = {
    model,
    title,
    town,
    service_id,
    description,
    price_min,
    price_max,
  };

  function handleFileChange(event) {
    imageFile = event.target.files[0];

    const formData = new FormData();
    formData.append("image", imageFile);

    if (formData && axiosDATA) {
      // Add axiosData object to formData
      const axiosDataString = JSON.stringify(axiosDATA);
      formData.append("axiosDATA", axiosDataString);
    }
  }

  function handleUpload() {
    // if (!imageFile) {
    //   errorMessage = "Please select an image file";
    //   return;
    // }

    const formData = new FormData();
    formData.append("image", imageFile);

    // Add axiosData object to formData
    for (const [key, value] of Object.entries(axiosDATA)) {
      formData.append(key, value);
    }
  }
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
        bind:value={axiosDATA.title}
      />
    </div>

    <!-- Service Filter Start -->
    <label for="service">Seleccione Servicio a Brindar</label>
    <select
      bind:value={axiosDATA.service_id}
      name="service"
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
      bind:value={axiosDATA.town}
      name="town"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value="0">---</option>
      {#each towns as [town, id]}
        <option value={id}>{town}</option>
      {/each}
    </select>
    <!-- Town Filter End -->
    <div class="max-h-96">
      <label for="description">Descripcion de su Oferta</label>
      <textarea
        bind:value={axiosDATA.description}
        class="w-full min-h-20 max-h-20"
        name="description"
        id=""
      ></textarea>
    </div>
    <div>
      <label for="price-min">Precio Minimo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-min"
        id=""
        bind:value={axiosDATA.price_min}
      />
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-max"
        id=""
        bind:value={axiosDATA.price_max}
      />
    </div>
    <div
      class="flex flex-col items-center justify-center w-full m-auto mx-auto space-y-1 text-gray-800"
    >
      <!-- <label for="imageInput" class="block text-sm font-medium">Attachments</label> -->
      <div class="flex w-full">
        <input
          type="file"
          name="image"
          id="imageInput"
          on:change={handleFileChange}
          class="w-full px-8 py-12 text-gray-600 bg-gray-100 border-2 border-gray-300 border-dashed rounded-md"
          accept="image/*"
        />
        <!-- <button
          class="px-8 py-12 bg-teal-800 border-2 border-gray-300 rounded-md shadow-lg text-teal-50"
          on:click={handleUpload}
        >
          Upload
        </button> -->
      </div>
      {#if errorMessage}
        <p class="text-red-500">{errorMessage}</p>
      {/if}
    </div>
    <Button {buttonNAME} {crudVERB} {locationURL} {axiosDATA} {headerTYPE} />
  </div>
</div>
