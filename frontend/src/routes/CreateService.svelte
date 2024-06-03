<!-- Alfre: It seems button works correctly 
  and missing towns as an array [] making 
  the api request fail with status: 500 -->
<script>
  import townsID from "../scripts/townsID";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";

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

  const axiosDATA = new FormData();
  let miscDATA = { "Create Service": true };
  let buttonDATA = {
    name: "Create Service",
    method: "POST",
    url: "api/dashboard/promotion-request",
    headers: {
      "Content-Type": "multipart/form-data",
    },
    twcss: "px-8 py-3 font-semibold text-teal-100 bg-teal-800 rounded",
  };

  let data = {
    model,
    title,
    town,
    service_id,
    description,
    price_min,
    price_max,
  };

  function handleFileChange(event) {
    console.log("Selected Image");
    imageFile = event.target.files[0];
    axiosDATA.append("image", imageFile);
  }

  function handleInputChange() {
    const allTrue = Object.values(data).every((value) => Boolean(value));
    if (allTrue) {
      console.log("Form Completed");
      for (const [key, value] of Object.entries(data)) {
        axiosDATA.append(key, value);
      }
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
      Crear Servicio
    </h1>
    <!-- Crear Solicitud de Servicio -->
    <div class="">
      <label for="title">Titulo</label>
      <input
        class="w-full"
        type="text"
        name="titulo"
        id=""
        bind:value={data.title}
        on:change={handleInputChange}
      />
    </div>

    <!-- Service Filter Start -->
    <label for="service">Seleccione Servicio a Brindar</label>
    <select
      bind:value={data.service_id}
      on:change={handleInputChange}
      name="service"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value={-1} disabled>---</option>
      {#each services as [service, id]}
        <option value={id}>{service}</option>
      {/each}
    </select>
    <!-- Service Filter End -->

    <!-- Town Filter Start -->
    <label for="town">Seleccione un Pueblo</label>
    <select
      bind:value={data.town}
      on:change={handleInputChange}
      name="town"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value={-1} disabled>---</option>
      {#each towns as [town, id]}
        <option value={id}>{town}</option>
      {/each}
    </select>
    <!-- Town Filter End -->
    <div class="max-h-96">
      <label for="description">Descripcion de su Servicio</label>
      <textarea
        bind:value={data.description}
        on:change={handleInputChange}
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
        bind:value={data.price_min}
        on:change={handleInputChange}
      />
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-max"
        id=""
        bind:value={data.price_max}
        on:change={handleInputChange}
      />
    </div>
    <div
      class="flex flex-col items-center justify-center w-full m-auto mx-auto space-y-1 text-gray-800"
    >
      <label for="imageInput" class="block text-sm font-medium"></label>
      <div class="flex w-full">
        <input
          type="file"
          name="image"
          id="imageInput"
          on:change={handleFileChange}
          class="w-full px-8 py-12 text-gray-600 bg-gray-100 border-2 border-gray-300 border-dashed rounded-md"
          accept="image/*"
        />
      </div>
      {#if errorMessage}
        <p class="text-red-500">{errorMessage}</p>
      {/if}
    </div>
    <Button {buttonDATA} {axiosDATA} {miscDATA} />
  </div>
</div>
